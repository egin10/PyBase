#VirusTotal API
import requests

class vT():
	#initial for define api key first
	def __init__(self, api_key):
		self.api_key = api_key
		return

	#sending and scanning file
	def _sendFile(self, file):
		params = self.api_key
		files = {'file': (file, open(file, 'rb'))}
		response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
		json_response = response.json()
		return json_response

	#rescan md5/sha1/sha256 hash
	def _rescan(self, resource):
		params = {'apikey': self.api_key, 'resource': resource}
		headers = {
		  "Accept-Encoding": "gzip, deflate",
		  "User-Agent" : "gzip,  My Python requests library example client or username"
		}
		response = requests.post('https://www.virustotal.com/vtapi/v2/file/rescan',
		 params=params)
		json_response = response.json()
		return json_response

	

