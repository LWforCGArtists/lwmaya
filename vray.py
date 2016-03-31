import pymel.core as pm
from render import Renderer
import utils

# Reload procedures
# Disable this for release!
reload(utils)

class VRayConfig(Renderer):
    """
    This class responsible for linear workflow
    VRaya configurtaion
    """
    def __init__(self):
        pass

    def set_linear_settings(self):

        # Make sure that VRay plugin loaded
        # and render tab set to vray
        pm.mel.loadPlugin('vrayformaya')
        current_renderer = pm.Attribute('defaultRenderGlobals.currentRenderer')
        current_renderer.set('vray')

        vray_settings = pm.PyNode('vraySettings')

        utils.set_attrs(vray_settings, {
            # Image File Output
            'imageFormatStr': 'exr',
            # Color mapping
            'cmap_adaptationOnly': 1, # Don't affect colors, only adaptation
            # Add your attribute here...
        })

    def linearize_texture(self, file_node):
        pass

    def linearize_all_textures(self):
        pass

def main():
    vr_conf = VRayConfig()
    vr_conf.set_linear_settings()
