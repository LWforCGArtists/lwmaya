# This is the main file to start the application

import vray

# Reload procedures
# Disable this for release!
reload(vray)

from vray import VRayConfig

def run():
    vray_config = VRayConfig()
    vray_config.set_linear_settings()
