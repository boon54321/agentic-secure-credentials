# setup.py
from setuptools import setup, find_packages

setup(
    name="agentic-secure-credentials",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    author="BoonAgentic",
    author_email="boon54321@gmail.com",
    description="A simple package to store and retrieve credentials with resource details",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/boon54321/agentic-secure-credentials",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)