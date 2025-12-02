from setuptools import setup

VERSION = "1.0.0"
DESCRIPTION = "A personal toolbox for Advent of Code"
LONG_DESCRIPTION = "A work-in-progress collection of useful tools (snippets, functions) for Advent of Code"

setup(
    name = "aoc_tools",
    version = VERSION,
    author = "Edoardo Baldi",
    author_email = "hi@edobld.me",
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    packages = ["aoc_tools"],
    install_requires = [],
    classifiers = [],
)
