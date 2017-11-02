#VirusTotal API
import requests

#Ip Report
def ipReport(ip, api_key):
	url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
	params = { 'apikey':api_key, 'ip':ip }
	response = requests.get(url, params=params)
	return response.json()

def domainReport(domain, api_key):
	url = 'https://www.virustotal.com/vtapi/v2/domain/report'
	params = {'apikey':api_key,'domain':domain}
	response = requests.get(url, params=params)
	return response.json()

def urlScan(url, api_key):
	url = 'https://www.virustotal.com/vtapi/v2/url/scan'
	params = {'apikey': api_key, 'url':url}
	response = requests.post(url, data=params)
	return response.json()

def urlReport(resource, api_key):
	url = 'https://www.virustotal.com/vtapi/v2/url/report'
	params = {'apikey': api_key, 'resource':resource}
	response = requests.get(url, params=params)
	return response.json()

def fileScan(file, api_key):
	url = 'https://www.virustotal.com/vtapi/v2/file/scan'
	params = {'apikey': api_key}
	files = {'file': file}
	response = requests.post(url, files=files, params=params)
	return response.json()

def fileReport(resource, api_key):
	url = 'https://www.virustotal.com/vtapi/v2/file/report'
	params = {'apikey': api_key, 'resource': resource}
	response = requests.get(url, params=params)
	return response.json()