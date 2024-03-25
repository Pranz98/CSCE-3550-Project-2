import requests
import json

# Define the server URL
server_url = 'http://localhost:8080'

# Define the fake user credentials
credentials = ('userABC', 'password123')

# Define the payload for the POST request
payload = {
    'username': credentials[0],
    'password': credentials[1]
}

# Define headers for HTTP Basic Auth
headers = {
    'Content-Type': 'application/json'
}

# Perform HTTP Basic Auth
response = requests.post(f'{server_url}/auth', headers=headers, data=json.dumps(payload), auth=credentials)

# Check if the request was successful
if response.status_code == 200:
    print('Authentication successful!')
    print('JWT:', response.text)
else:
    print('Authentication failed!')

# Perform GET request for JWKS
response = requests.get(f'{server_url}/.well-known/jwks.json')

# Check if the request was successful
if response.status_code == 200:
    print('JWKS fetched successfully!')
    print('JWKS:', response.json())
else:
    print('Failed to fetch JWKS!')
