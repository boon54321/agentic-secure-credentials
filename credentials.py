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

