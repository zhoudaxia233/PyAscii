import os
import sys
import platform
import pyascii
from setuptools import setup

# "setup.py publish" shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist')
    os.system('twine upload dist/*')
    if platform.system() == 'Windows':
        os.system('powershell rm –path dist, pyascii.egg-info –recurse –force')
    else:
        os.system('rm -rf dist pyascii.egg-info')
    sys.exit()

setup(
    name='pyascii',
    version=pyascii.__version__,
    description="A tool for converting images or videos to ASCII.",
    keywords='asciiart',
    url='https://github.com/zhoudaxia233/PyAscii',
    license='MIT',
    packages=['pyascii'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['opencv-python>=4.0.0'],
    python_requires='>=3.6',
    dependency_links=[],
    entry_points={
        'console_scripts': [
            'pyascii=pyascii.main:main',
        ]
    }

)
