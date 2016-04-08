import pymel.core as pm
from render import Renderer
import utils

reload(utils)

class MRayConfig(Renderer):
    """
    This class responsible for linear workflow
    Mental Ray configurtaion
    """
    def __init__(self):
        pass

    def set_linear_settings(self):
        
        # Make render tab set to Mentalray
        current_renderer = pm.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

        # Turn on Enable Color Management and update the other widgets accordingly
        Enable_color_managment = pm.setAttr('defaultRenderGlobals.colorProfileEnabled', 1)
        pm.mel.updateCommonColorProfile()

        utils.set_attrs( pm, {
            # Swich Image Format to EXR and Image compression to PIZ
            'defaultRenderGlobals.imageFormat': 51,
            'defaultRenderGlobals.imfPluginKey':'exr',
            'mentalrayGlobals.imageCompression': 3,
            # Switch Date Type to RGBA(Float) 4*32 Bit under Framebuffer in Quality tab
            'miDefaultFramebuffer.datatype': 5,
            #Set the Default View Color Manager 
            'defaultViewColorManager.imageColorProfile': 2,
        })

    def gammaCorrect_node(self):

        # Create a GammaCorrect node to correct the gamma value of color of the Materials shader

        # Create a GammaCorrect node
        shader = pm.shadingNode('gammaCorrect', asShader = True)
        # Create a file texture node
        file_node = pm.shadingNode('file', asTexture = True)
        # a shading group
        shading_group = pm.sets(renderable = True, noSurfaceShader = True, empty = True)
        # Connect shader to sg surface shader
        pm.connectAttr('%s.value' % shader ,'%s.surfaceShader' % shading_group)
        # Connect file texture node to shader's color
        pm.connectAttr('%s.outColor' % file_node, '%s.value' % shader)
        # Set the gamma value to 0.454
        pm.setAttr('%s.gamma' % shader, 0.454, 0.454, 0.454, type = 'double3')
                
def main():
    mray_conf = MRayConfig()
    mray_conf.set_linear_settings()
