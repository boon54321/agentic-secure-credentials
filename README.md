# README.md
# Agentic Secure Credentials

A Python package to store and retrieve encrypted usernames, passwords, and resource details using Fernet encryption.

## Installation
Install directly from GitHub:
```bash
pip install git+https://github.com/yourusername/agentic-secure-credentials.git
```

## Usage
```python
from agentic_secure_credentials import CredentialManager

# Initialize the credential manager
cm = CredentialManager()

# Save the encryption password (call this once before saving/loading credentials)
cm.save_encryption_password("mysecretpassword")

# Save credentials
cm.save_credentials(
    username="my_username",
    password="my_password",
    resource_type="database",
    resource_name="prod_db",
    resource_description="Production database for app",
    server="localhost",
    port="5432"
)

# Load credentials
creds = cm.load_credentials()
if creds:
    print(f"Username: {creds['username']}")
    print(f"Password: {creds['password']}")
    print(f"Resource Type: {creds['resource_type']}")
    print(f"Resource Name: {creds['resource_name']}")
    print(f"Resource Description: {creds['resource_description']}")
    print(f"Server: {creds['server']}")
    print(f"Port: {creds['port']}")
```

## Requirements
- Python 3.6+
- cryptography>=36.0.0

## Notes
- Credentials are encrypted using Fernet (symmetric encryption) and stored in `credentials.enc`.
- The encryption key is stored in `key.key`, and the encrypted password is stored in `encryption_password.key`. Keep these files secure.
- Call `save_encryption_password` once to set the encryption password before saving or loading credentials.

## License
MIT License