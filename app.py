import pymel.core as pm

class VRayConfig(object):
    """
    This class responsible for linear workflow
    VRaya configurtaion
    """
    def __init__(self):
        pass

    def set_attrs(self, node, attr_dict):
        """
        param node: PyMel note to assign attributes to.
        param attr_dict: Dictionary of attributes.
        """
        for name, value in attr_dict.items():
            if (value is not None):
                node.setAttr(name, value)
            else:
                # self.log.debug('Attribute %s is %s. Skipped!' % (name, value))
                pass

    def set_linear_settings(self):

        # Make sure that VRay plugin loaded
        # and render tab set to vray
        pm.mel.loadPlugin('vrayformaya')
        current_renderer = pm.Attribute('defaultRenderGlobals.currentRenderer')
        current_renderer.set('vray')

        vray_settings = pm.PyNode('vraySettings')

        self.set_attrs(vray_settings, {
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
