# Necessary Imports
from SharekhanApi.sharekhanConnect import SharekhanConnect
from config import *

def generate_request_token():
    """
    Generates a request token for Sharekhan API.

    This script initializes a SharekhanConnect instance and generates a login URL.
    """
    # Initialize SharekhanConnect
    login = SharekhanConnect(api_key)

    # Generate the login URL
    login_url = login.login_url(vendor_key, version_id)
    print("Login URL:", login_url)
    print("Login using the above URL and get the request_token from the URL you are redirected to after signin. "
          "Update the request_token in config.py")

if __name__ == "__main__":
    generate_request_token()
