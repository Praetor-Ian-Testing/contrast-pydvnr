from io import open
from os import path

from setuptools import setup

root_dir = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(root_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='contrast-pydvnr',

    version='0.0.1',

    description='Contrast Python Diviner',
    long_description=long_description,

    # The project's main homepage.
    url='',

    # Author details
    author='Contrast Security, Inc.',
    author_email='justin.leo@contrastsecurity.com',

    # Choose your license
    license='MIT',

    classifiers=[
        # Audience
        'Intended Audience :: Developers',

        # supported languages
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='security development',

    packages=['pydvnr'],
    package_dir={'pydvnr': 'pydvnr'},
    include_package_data=True,

    requires=['psutil'],

    install_requires=[],

    extras_require={},

    package_data={},

    data_files=[],
    entry_points={
        'console_scripts': [
            'contrast-pydvnr = pydvnr.__main__:main'
        ]
    },
)
