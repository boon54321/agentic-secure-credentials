# README.md
# Secure Credentials

A simple Python package to store and retrieve usernames, passwords, and resource details in JSON format.

## Installation
```bash
pip install secure-credentials
```

## Usage
```python
from secure_credentials import CredentialManager

# Initialize the credential manager
cm = CredentialManager()

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

## License
MIT License