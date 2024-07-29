# Necessary Imports
from SharekhanApi.sharekhanConnect import SharekhanConnect
from config import *


def generate_access_token():
    """
    Generates an access token for Sharekhan API.

    This script uses the request token to generate a session and obtain an access token.
    """
    # Print the initial request token and secret key for debugging
    print("Initial Request Token:", request_token)
    print("Secret Key:", secret_key)

    # Initialize SharekhanConnect
    login = SharekhanConnect(api_key)

    # Generate session and access token
    if version_id:
        # Generate session with version ID
        session = login.generate_session(request_token, secret_key)
        print("Generated Session:", session)

        # Obtain access token response
        access_token_response = login.get_access_token(api_key, session, state, versionId=version_id)
    else:
        # Generate session without version ID
        session_without_version_id = login.generate_session_without_versionId(request_token, secret_key)
        print("Generated Session without Version ID:", session_without_version_id)

        # Obtain access token response
        access_token_response = login.get_access_token(api_key, session_without_version_id, state)

    # Print the full response for debugging
    print("Access Token Response:", access_token_response)

    # Extract access token from the response
    access_token = access_token_response.get('data', {}).get('token')
    print("Token:", access_token)
    # Add access_token to config.py

    # Initialize SharekhanConnect with access token to test if everything is set up correctly
    sharekhan = SharekhanConnect(api_key=api_key, access_token=access_token)
    print("Request Headers:", sharekhan.requestHeaders())  # For printing request headers

    # Fetch and print holdings
    holdings = sharekhan.holdings(customer_id)
    print("Holdings:", holdings)


if __name__ == "__main__":
    generate_access_token()
