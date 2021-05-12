from oauth2client.client import OAuth2WebServerFlow





__OAUTH_SCOPE = ['https://www.googleapis.com/auth/drive']
__REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

__CLIENT_ID = input("Enter the client id: ")
__CLIENT_SECRET = input("Enter the client secret: ")

flow = OAuth2WebServerFlow(
        __CLIENT_ID,
        __CLIENT_SECRET,
        __OAUTH_SCOPE,
        redirect_uri=__REDIRECT_URI
        )
auth_url = flow.step1_get_authorize_url()
print("Open this URL in any browser and get the refersh token: \n" + auth_url)
refresh_token = input("Enter the Refresh token: ")
auth = flow.step2_exchange(refresh_token).to_json()
print(auth)
