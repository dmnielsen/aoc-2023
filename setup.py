import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='aoc2023',
    packages=['aoc2023'],
    version='0.1.0',
    description='2023 Advent of Code',
    long_description=README,
    long_description_content_type="text/markdown",
    author='dmnielsen',
    license='MIT',
)
