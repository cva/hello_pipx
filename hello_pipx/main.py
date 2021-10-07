import requests

__version__ = "0.0.0.1"

def main():
    print("Hello world!")
    print()
    print(f"Your Public IP address is: {requests.get('https://ifconfig.me').text}")