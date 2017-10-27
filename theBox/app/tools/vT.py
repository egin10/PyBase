#VirusTotal API
import requests
import json
import urllib

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

	#Rescanning already submitted files
	def _rescan(self, resource):
		params = {'apikey': self.api_key, 'resource': resource}
		response = requests.post('https://www.virustotal.com/vtapi/v2/file/rescan', params=params)
		json_response = response.json()
		return json_response

	#Retrieving file scan reports
	def _retriev(self, resource):
		params = {'apikey': self.api_key, 'resource': resource}
		headers = {
		  "Accept-Encoding": "gzip, deflate",
		  "User-Agent" : "gzip,  My Python requests library example client or username"
		  }
		response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers)
		json_response = response.json()
		return json_response

	#Sending and scanning URLs
	def _sendUrl(self, url):
		params = {'apikey': self.api_key, 'url':url}
		response = requests.post('https://www.virustotal.com/vtapi/v2/url/scan', data=params)
		json_response = response.json()
		return json_response

	#Retrieving URL scan reports
	def _retrievUrl(self, url):
		params = {'apikey': self.api_key, 'resource':url}
		headers = {
		  "Accept-Encoding": "gzip, deflate",
		  "User-Agent" : "gzip,  My Python requests library example client or username"
		  }
		response = requests.post('https://www.virustotal.com/vtapi/v2/url/report', params=params, headers=headers)
		json_response = response.json()
		return json_response

	#Retrieving IP address reports
	def _retrievIp(self, ip):
		url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
		parameters = {'ip': ip, 'apikey': self.api_key}
		response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
		response_dict = json.loads(response)
		return response_dict

	#Retrieving domain reports
	def _retrievDomain(self, domain):
		url = 'https://www.virustotal.com/vtapi/v2/domain/report'
		parameters = {'domain': domain, 'apikey': self.api_key}
		response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
		response_dict = json.loads(response)
		return response_dict