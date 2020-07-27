from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="yatrex",

    version='0.1.0',

    description="Yet Another TRansmission EXporter",
    long_description=long_description,

    url="https://github.com/w1kl4s/yatrex",

    author="w1kl4s",
    author_email="w1kl4s@protonmail.com",
    license="BSD 2-Clause",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: System Administrators",

        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

    ],
    python_requires=">=3.6, <4",
    keywords="transmission monitoring metrics exporter",
    packages=["src"],
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": ["yatrex=src.commandline:start"]
    }
)
