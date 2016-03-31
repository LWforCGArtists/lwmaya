# Maya Linear Workflow

## Developers notes

This section contains some tips how to get started with this module as a developer.

### How to run for development

Place this repo folder in one of your default Maya script directory:

```
Windows: <drive>:\Documents and Settings\<username>\My Documents\maya\<Version>\scripts
Mac OS X: ~/Library/Preferences/Autodesk/maya/<version>/scripts
Linux: ~/maya/<version>/scripts
```

Or clone this repo to *"your_path"* amd then in Maya console do:

```python
import sys
sys.path.append("your_path")

import lwmaya
reload(lwmaya)

lwmaya.main.run()
```

### Developers guidline

The functionality split per render. Each render has it own class and file.
Every render class follows <render_name>Config patern and must inherit from abstract base class Render.

For example 
``` python
class MRayConfig(Render)
class VRayConfig(Render)
class ArnoldConfig(Render)
```

The entry point for user to launch the application is `main.py` file that contains `run()` function.

### Folders
> docs

Contains any documentation or manual files related to the project.

> tests

Contains Maya project scenes, test images, unit test scripts etc.
