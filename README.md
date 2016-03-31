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

Or clone this repo to *<your_path>* amd then in Maya console do:

```python
import sys
sys.path.append(<your_path>)
import lwmaya
reload(lwmaya)
lwmaya.ui.main()
lwmaya.app.main()
```
# LWMaya
