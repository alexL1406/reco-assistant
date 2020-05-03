import requests
import json
import pathlib
from urllib.parse import urlencode
import base64
import simplejson


class GoogleHandle(object):

    def __init__(self):
        self.connection_token = ""
        self.refresh_token = ""
        self.expiration_timestamp = 0
        self.HOST_URL = "https://www.googleapis.com"
        self.RECO_API = "/v1p1beta1/speech:recognize"
        self.AUTH_API = "/o/oauth2/auth"
        self.client_id = ""
        self.redirect_uri = ""
        self.response_type = "code"
        self.scope = "email%20profile&"

        self.key = "AIzaSyAsdGz-RdH5mAoN7yYOK2FjAIjC4vO95Tk"

        # self.read_credentials()

    def read_credentials(self):
        with open(str(pathlib.Path.home()) + "/Téléchargements/credentials.json", 'r') as json_file:
            json_data = json.load(json_file)["installed"]
            self.client_id = json_data["client_id"]
            self.redirect_uri = json_data["redirect_uris"][0]

    def certification(self):
        # auth_url = self.HOST_URL + self.AUTH_API
        auth_url = "https://accounts.google.com/o/oauth2/"
        cert_params = {"client_id": self.client_id,
                       "redirect_uri": self.redirect_uri,
                       "response_type": self.response_type,
                       "scope": self.scope,
                       "login_hint": "alexis.leurent1994@gmail.com"}
        print(cert_params)
        # cert_request = requests.get(url=auth_url, params=cert_params, allow_redirects=False)
        cert_request = requests.get(auth_url + "auth?%s" % urlencode(cert_params))

        print("code: " + str(cert_request.status_code))
        print(cert_request.reason)

        if cert_request.status_code == 200:
            headers = cert_request.headers
            print(headers)
            # Popen(["open", url])

            # authorization_code = input("\nAuthorization Code >>> ")
            # print(authorization_code)

    def speech_to_text_api(self, speech_byte, fs):

        stt_params = {
                      'audio': {'content': speech_byte.decode('ascii')},
                      'config': {
                          'enableAutomaticPunctuation': False,
                          "sampleRateHertz": fs,
                          'encoding': 'LINEAR16',
                          'languageCode': 'fr-FR',
                          'alternativeLanguageCodes': ['en-US', 'es-MX'],
                          'model': 'default'}
                      }

        print("send Speech To Text request")
        stt_request = requests.post(url='https://speech.googleapis.com/v1p1beta1/speech:recognize?key='+self.key,
                                    json=stt_params)

        return stt_request
