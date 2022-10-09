import pyboy
from setuptools import setup
import platform

############################
# CHANGE THESE PARAMETERS

# The full name of the package, and the name it will get on PyPi. I.e. the name for pip install: "pip install pyboy-auto-pause"
# It's recommended to prefix PyBoy plugins with "pyboy-".
PLUGIN_NAME = "pyboy-auto-pause"

# The URL to put in the plugin package
PLUGIN_URL = "https://github.com/Baekalfen/pyboy-auto-pause"

# The version of your plugin package
VERSION = "1.0"

# The Python module name. name or Python filename (omitting ".py")
MODULE_NAME = "auto_pause"

# The author name and email to put on the package
AUTHOR_NAME = "Mads Ynddal"
AUTHOR_EMAIL = "mads@ynddal.dk"

# List the filepaths for the Python files for Cython to compile. Or just an empty list if none.
CYTHONIZE_FILES = ["auto_pause.py"]
############################

is_pypy = platform.python_implementation() == "PyPy"
if (not is_pypy) and CYTHONIZE_FILES:
    from Cython.Build import cythonize
    ext_modules = cythonize(
        CYTHONIZE_FILES,
        include_path=[pyboy.get_include()],
        language_level=3,
    )
else:
    ext_modules = []

setup(
    name=PLUGIN_NAME,
    classifiers=["Framework :: PyBoy"],
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    url=PLUGIN_URL,
    py_modules=[
        MODULE_NAME,
    ],
    install_requires=[
        'pyboy',
    ],
    entry_points={
        'pyboy': [
            f"{PLUGIN_NAME.replace('-','_')} = {MODULE_NAME}",
        ],
    },
)