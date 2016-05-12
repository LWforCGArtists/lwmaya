import pymel.core as pm
from modules.pathlib import Path
from modules.logger import Logger
from render import Renderer
import utils

# Reload procedures
# Disable this for release!
reload(utils)

# Constants
NON_LEANEAR_FORMATS = ['.jpg', '.png']

DEFAULT_MATERIAL_TYPES = ['lambert', 'blinn']
VRAY_MATERIAL_TYPES = ['VRayMtl', 'VRayLightMtl']
ALL_MATERIAL_TYPES = DEFAULT_MATERIAL_TYPES + VRAY_MATERIAL_TYPES

log = Logger()

class VRayConfig(Renderer):
    """
    This class responsible for linear workflow
    VRaya configurtaion
    """
    def __init__(self):
        # Some initialization work here
        pass

    def _get_types(self, types):
        """
        :param types: (list) List of Maya types
        :returns: (PyNode iterator) of all Maya objects of this types
        """
        for mat_type in types:
            for mat in pm.ls(type=mat_type):
                yield mat

    def _linearize_color(self, color_attr):
        """
        Connect gamma node to the given attribute with inverse gamma curve
        :param color_attr: (pm.Attribute) Color attribute to connect gamma node to
        """
        # Create gamma node
        gamma_node = pm.createNode('gammaCorrect')
        # Set gamma to inverse gamma curve
        gamma_node.setAttr('gamma', (0.4545, 0.4545, 0.4545))
        # Copy color from material to gamma node
        gamma_node.setAttr('value', color_attr.get())
        # Connect gamma node to material color
        pm.connectAttr('%s.outValue' % gamma_node, color_attr)

    def linearize_solid_materils(self):
        """
        For every material that use solid color apply inverse
        gamma curve to this color by supplying the attribute
        with gamma node
        """

        for mat in self._get_types(ALL_MATERIAL_TYPES):

            color_attr = pm.Attribute('%s.color' % mat)

            if color_attr.get() == (0.0, 0.0, 0.0):
                # Our material has no color, continue
                continue

            # Color attr already has a connection
            if color_attr.isConnected():
                color_input = color_attr.inputs()[0]

                # User already have gamma correction on his solid color
                if color_input.type() == 'gammaCorrect':
                    continue # Skip
                    # Do settings checks
                else:
                    # Something else is connected to the color input
                    continue # Skip

            self._linearize_color(color_attr)

    def set_linear_settings(self):
        """
        Sets global renderer setting for the VRay linear workflow
        """

        # Make sure that VRay plugin loaded
        # and render tab set to vray
        pm.mel.loadPlugin('vrayformaya')
        pm.mel.vrayRegisterRenderer()
        pm.mel.vrayCreateVRaySettingsNode()
        current_renderer = pm.Attribute('defaultRenderGlobals.currentRenderer')
        current_renderer.set('vray')
        # Get scene VRay settngs node
        vray_settings = pm.PyNode('vraySettings')

        utils.set_attrs(vray_settings, {
            # Image File Output
            'imageFormatStr': 'exr',
            # Color mapping
            'cmap_adaptationOnly': 1, # Don't affect colors, only adaptation
            # Add your attribute here...
        })

    def linearize_texture(self, file_node):
        """
        Given a file node as PyNode object
        treat it to comply to proper linear workflow
        :params file_node: (PyNode) File node object
        """

        texture_path = Path(file_node.getAttr('fileTextureName'))

        # File node use texture that needs to be gamma corrected
        if texture_path.suffix in NON_LEANEAR_FORMATS:

            # http://docs.chaosgroup.com/display/VRAY3MAYA/Texture+Attributes
            attr_group = 'vray_file_gamma'
            state = 1 # 0 to delete, 1 to create

            # Create VRay input gamma attribute group
            pm.vray('addAttributesFromGroup', file_node, attr_group, state)

            # Set color space to sRGB
            file_node.setAttr('vrayFileColorSpace', 2)

    def linearize_all_textures(self):

        # List all Maya file nodes
        file_nodes = pm.ls(type='file')

        for file_node in file_nodes:
            self.linearize_texture(file_node)


def main():
    vr_conf = VRayConfig()
    vr_conf.linearize_solid_materils()
