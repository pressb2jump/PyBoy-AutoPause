# PyBoy-AutoPause Plugin

This is a very simple example of creating a plugin for [PyBoy](https://github.com/Baekalfen/PyBoy). It contains the boilerplate code necessary to create, build and register the plugin.

Steps to create a plugin:
 1. Fork this repo, or copy the files.
 2. Rename the `auto_pause.py`/`.pxd` file to your plugin name.
 3. Rename the AutoPause class in the `.py` and `.pxd` files to your plugin class.
 4. Add your plugin code. You can see the available methods to override in the [PyBoyPlugin class](https://github.com/Baekalfen/PyBoy/blob/master/pyboy/plugins/base_plugin.py#L33). Or subclass from one of the other plugin types.
 5. Build the code with Cython: `python3 setup.py build_ext sdist bdist_wheel` or without Cython: `python3 setup.py sdist`
 6. Install the package: `python3 -m pip install dist/*.whl` or `python3 -m pip install dist/*.tar.gz`
 7. Run PyBoy: `pyboy ... --autopause`

If you don't want to build the plugin with Cython, you can remove the `.pxd` file and set `CYTHONIZE_FILES = []` in the `setup.py` file.