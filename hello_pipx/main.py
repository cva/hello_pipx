import requests

__version__ = "0.0.0.2"

def main():
    print(f"Hello world! v{__version__}")
    print("Change without bumping version")
    print()
    print(f"Your Public IP address is: {requests.get('https://ifconfig.me').text}")
