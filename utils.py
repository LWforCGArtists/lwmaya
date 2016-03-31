import pymel.core as pm

def set_attrs(node, attr_dict):
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
