import json
import os
import webbrowser
from oauth2client import client

REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
OAUTH_SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
GSC_JSON_FILE = "path_to_save_credentials"

def generate_authorize_url(client_id, client_secret):
    flow = client.OAuth2WebServerFlow(client_id, client_secret, OAUTH_SCOPE, REDIRECT_URI)
    authorize_url = flow.step1_get_authorize_url()
    return authorize_url

def generate_json_credentials(client_id, client_secret, authorization_code, file_name):
    flow = client.OAuth2WebServerFlow(client_id, client_secret, OAUTH_SCOPE, REDIRECT_URI)
    credentials = flow.step2_exchange(authorization_code)

    file_path = os.path.join(GSC_JSON_FILE, file_name + '.json')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, "w") as f:
        json.dump(json.loads(credentials.to_json()), f)
    
    print(f"Credentials saved to {file_path}")

def main():
    client_id = input("Enter your Client ID: ")
    client_secret = input("Enter your Client Secret: ")

    authorize_url = generate_authorize_url(client_id, client_secret)
    print(f"Authorize URL: {authorize_url}")
    webbrowser.open(authorize_url)

    authorization_code = input("Enter Authorization Code: ")
    file_name = input("Enter File Name (without extension): ")

    generate_json_credentials(client_id, client_secret, authorization_code, file_name)

if __name__ == "__main__":
    main()