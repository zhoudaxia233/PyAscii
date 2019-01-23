import os
import sys
import io
import re
import pyascii
from setuptools import setup


# "setup.py publish" shortcut.
if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist')
    os.system('twine upload dist/*')
    os.system('rm -rf dist py_wtf.egg-info')
    sys.exit()

setup(
    name='pyascii',
    version=pyascii.__version__,
    description="A tool for converting images or gifs or videos to ASCII.",
    keywords='asciiart',
    url='https://github.com/zhoudaxia233/PyAscii',
    license='MIT',
    packages=['pyascii'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Pillow>=5.1.0'],
    python_requires='>=3.5',
    dependency_links=[],
    entry_points={
        'console_scripts': [
          'pyascii=pyascii.main:main',
      ]
    }

)