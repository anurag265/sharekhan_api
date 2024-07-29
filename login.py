from SharekhanApi.sharekhanConnect import SharekhanConnect
from config import *

# Initialize SharekhanConnect
login = SharekhanConnect(api_key)

# Test Import from pycryptodome directly
try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad, unpad
    print("pycryptodome import successful.")
except ImportError as e:
    print("Error importing pycryptodome:", e)

# Print the initial request token and secret key for debugging
print("Initial Request Token:", request_token)
print("Secret Key:", secret_key)

# Generate session and access token
if version_id:
    session = login.generate_session(request_token, secret_key)
    print("Generated Session:", session)
    access_token_response = login.get_access_token(api_key, session, state, versionId=version_id)
else:
    session_without_version_id = login.generate_session_without_versionId(request_token, secret_key)
    print("Generated Session without Version ID:", session_without_version_id)
    access_token_response = login.get_access_token(api_key, session_without_version_id, state)
    print(f"access_token_response: {access_token_response}")

# Print the full response for debugging
print("Access Token Response:", access_token_response)

# Extract access token from the response
access_token = access_token_response.get('data', {}).get('token')

# Initialize SharekhanConnect with access token
sharekhan = SharekhanConnect(api_key=api_key, access_token=access_token)
print(sharekhan.requestHeaders())       # for printing request headers
print(access_token)


# Fetch holdings
holdings = sharekhan.holdings(customer_id)
print("Holdings:", holdings)