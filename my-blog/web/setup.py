import os
from setuptools import setup, find_packages

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="mb",
    version="0.1",
    packages=find_packages("."),
    include_package_data=True,
    entry_points="""
        [console_scripts]
        my-blog-app=mb.cli:main
        django=mb.manage:main
    """,
)
