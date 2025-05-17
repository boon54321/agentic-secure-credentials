# setup.py
from setuptools import setup, find_packages

setup(
    name="agentic-secure-credentials",
    version="0.1.6",
    packages=find_packages(),
    install_requires=['cryptography>=36.0.0'],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package to store and retrieve encrypted credentials with resource details for Agentic",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/boon12345/agentic-secure-credentials",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

