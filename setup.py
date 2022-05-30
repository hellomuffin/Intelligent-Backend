from setuptools import setup

setup(
    name='backend',
    version='0.1.0',
    packages=['backend'],
    include_package_data=True,
    install_requires=[
        'arrow',
        'bs4',
        'Flask',
        'requests',
        'pathlib'
    ],
    python_requires='>=3.6',
)