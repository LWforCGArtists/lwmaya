import pymel.core as pm
from render import Renderer
import utils

class MRayConfig(Renderer):
    """
    This class responsible for linear workflow
    Mental Ray configurtaion
    """
    def __init__(self):
        pass

    def set_linear_settings(self):
        # TODO(Kirill): Toni please implement
        # this function
        pass
        current_renderer = pm.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

        #1. Turn on Enable Color Management
        pm.setAttr("defaultRenderGlobals.colorProfileEnabled", 1)
        # update the other widgets accordingly
        pm.mel.updateCommonColorProfile()

        #2. Swich Image Format to EXR and Image compression to PIZ
        pm.setAttr('defaultRenderGlobals.imageFormat', 51)
        pm.setAttr('defaultRenderGlobals.imfPluginKey','exr', type='string')  
        pm.setAttr("mentalrayGlobals.imageCompression", 3)      

        #3.Switch Date Type to RGBA(Float) 4*32 Bit under Framebuffer in Quality tab
        pm.setAttr("miDefaultFramebuffer.datatype", 5)

        #Set the Default View Color Manager 
        pm.setAttr("defaultViewColorManager.imageColorProfile", 2)

    def gammaCorrect_node(self):

        #create a shader
        shader=pm.shadingNode("gammaCorrect",asShader=True)
        #a file texture node
        file_node=pm.shadingNode("file",asTexture=True)
        # a shading group
        shading_group= pm.sets(renderable=True,noSurfaceShader=True,empty=True)
        #connect shader to sg surface shader
        pm.connectAttr('%s.value' %shader ,'%s.surfaceShader' %shading_group)
        #connect file texture node to shader's color
        pm.connectAttr('%s.outColor' %file_node, '%s.value' %shader)
        #set the gamma value to 0.454
        pm.setAttr("%s.gamma" %shader, 0.454, 0.454, 0.454, type='double3')
                
def main():
    mray_conf = MRayConfig()
    mray_conf.set_linear_settings()







