from setuptools import setup, find_packages

VERSION = '26.02.09'
DESCRIPTION = 'Convert MESA data into magnitudes.'
LONG_DESCRIPTION = 'Convert MESA data into magnitudes.'

setup(
    name='mesa-mag',
    version=VERSION,
    author="Kuo-Chuan Pan",
    author_email="<kuochuan.pan@gapp.nthu.edu.tw>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license='MIT',
    packages=find_packages(),
    package_data={'mesa_mag': ['filters/*.dat']},
    install_requires=['numpy','matplotlib'],

    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ],  
)
