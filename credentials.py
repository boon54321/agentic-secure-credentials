# agentic_secure_credentials/credentials.py
import os
import json

class CredentialManager:
    def __init__(self, data_file='credentials.json'):
        self.data_file = data_file

    def save_credentials(self, username, password, resource_type, resource_name, resource_description, server, port):
        credentials = {
            'username': username,
            'password': password,
            'resource_type': resource_type,
            'resource_name': resource_name,
            'resource_description': resource_description,
            'server': server,
            'port': port
        }
        with open(self.data_file, 'w') as f:
            json.dump(credentials, f, indent=4)

    def load_credentials(self):
        if not os.path.exists(self.data_file):
            return None
        with open(self.data_file, 'r') as f:
            return json.load(f)

# setup.py
from setuptools import setup, find_packages

setup(
    name="secure-credentials",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple package to store and retrieve credentials with resource details",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/secure-credentials",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

