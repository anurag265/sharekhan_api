# Configuration file for setting up API keys and necessary parameters for Sharekhan API access

# Customer ID assigned by Sharekhan for identifying the user
customer_id = 'add_customer_id_here'

# API Key provided by Sharekhan for authentication
api_key = "add_api_key_here"

# Secret key provided by Sharekhan for secure access
secret_key = "add_secret_key_here"

# Vendor key for vendor login; if not applicable, keep it null
vendor_key = ""  # leave it blank.

# Version ID for the API, if specified; otherwise, keep it null
version_id = ""  # leave it blank.

# State parameter used in the login URL for state management (unique identifier)
state = 11111  # set a unique identifier

# URL for login authentication, constructed with the API key and state parameter
login_url = f'https://api.sharekhan.com/skapi/auth/login.html?api_key={api_key}&state={state}'
print(login_url)

# Request token received after the initial authentication request
request_token = "copy_paste_request_token_here"

# Access token received after successful authentication, used for subsequent API requests
access_token = 'copy_paste_access_token_here'  # you would need to generate it on daily basis.
