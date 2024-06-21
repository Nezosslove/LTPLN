import io
import os
import sys

from setuptools import setup,find_packages

# Package meta-data.
NAME = "LTPLN"
VERSION="0.0.1"
DESCRIPTION = "LTPLN model keras implementation, and simple application"
URL = "https://github.com/Nezosslove/LTPLN"
EMAIL = "nezo2cs@gmail.com"
AUTHOR = "liu feng"
REQUIRES_PYTHON = "<=3.7.9"

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as f:
        REQUIRED = f.read().split("\n")
except:
    REQUIRED = []

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("miniset")),
    # If your package is a single module, use this instead of 'packages':
    #py_modules=['mypackage'],
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    #extras_require=EXTRAS,
    include_package_data=True,
    license="Apache License 2.0",
 )
