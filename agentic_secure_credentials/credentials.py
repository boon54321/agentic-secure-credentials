# agentic_secure_credentials/credentials.py
import os
import json
from cryptography.fernet import Fernet

class CredentialManager:
    def __init__(self, encrypted_file='credentials.enc', key_file='key.key', encryption_password_file='encryption_password.key'):
        self.encrypted_file = encrypted_file
        self.key_file = key_file
        self.encryption_password_file = encryption_password_file

    def _load_or_generate_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as f:
                key = f.read()
                try:
                    return Fernet(key)
                except ValueError:
                    raise ValueError("Invalid encryption key in key.key. Please remove or replace the file.")
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as f:
            f.write(key)
        return Fernet(key)

    def save_encryption_password(self, encryption_password):
        """Encrypt and save the encryption password."""
        
        self.encrypted_file = f"{encryption_password}_{self.encrypted_file}"
        self.key_file = f"{encryption_password}_{self.key_file}"
        self.encryption_password_file = f"{encryption_password}_{self.encryption_password_file}"
           
        self.fernet = self._load_or_generate_key()

        encrypted_password = self.fernet.encrypt(encryption_password.encode())
        with open(self.encryption_password_file, 'wb') as f:
            f.write(encrypted_password)


    def read_encryption_topic(self, encryption_password):
        """Encrypt and save the encryption password."""
        
        self.encrypted_file = f"{encryption_password}_{self.encrypted_file}"
        self.key_file = f"{encryption_password}_{self.key_file}"
        self.encryption_password_file = f"{encryption_password}_{self.encryption_password_file}"
        self.fernet = self._load_or_generate_key()
        
        
    def _load_encryption_password(self):
        """Load and decrypt the encryption password."""
        if not os.path.exists(self.encryption_password_file):
            raise ValueError("Encryption password not set. Call save_encryption_password first.")
        with open(self.encryption_password_file, 'rb') as f:
            encrypted_password = f.read()
        return self.fernet.decrypt(encrypted_password).decode()

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
        # Encrypt the credentials JSON
        credentials_json = json.dumps(credentials).encode()
        encrypted_data = self.fernet.encrypt(credentials_json)
        
        # Write encrypted data to file
        with open(self.encrypted_file, 'wb') as f:
            f.write(encrypted_data)

    def load_credentials(self):
        if not os.path.exists(self.encrypted_file):
            return None
        
        # Read and decrypt credentials
        with open(self.encrypted_file, 'rb') as f:
            encrypted_data = f.read()
        try:
            decrypted_data = self.fernet.decrypt(encrypted_data)
            credentials = json.loads(decrypted_data.decode())
            return credentials
        except Exception as e:
            raise ValueError(f"Failed to decrypt credentials: {str(e)}")
