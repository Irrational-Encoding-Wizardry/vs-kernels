#!/usr/bin/env python3

import setuptools

with open("README.md") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    install_requires = fh.read()

name = "vs-kernels"
version = "1.0.0"
release = "1.0.0"

setuptools.setup(
    name=name,
    version=release,
    author="LightArrowsEXE",
    author_email="lightarrowsreboot@gmail.com",
    description="Kernel objects for scaling and format conversion within VapourSynth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["vskernels"],
    package_data={
        'vskernels': ['py.typed'],
    },
    install_requires=install_requires,
    project_urls={
        "Source Code": 'https://github.com/Irrational-Encoding-Wizardry/vs-kernels',
        "Documentation": 'https://vskernels.encode.moe/en/latest/',
        "Contact": 'https://discord.gg/qxTxVJGtst',
    },
    classifiers=[
        "Natural Language :: English",

        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",

        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed",

        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Video :: Display",
    ],
    python_requires='>=3.9',
    command_options={
        "build_sphinx": {
            "project": ("setup.py", name),
            "version": ("setup.py", version),
            "release": ("setup.py", release),
            "source_dir": ("setup.py", "docs")
        }
    }
)
