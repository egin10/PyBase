# CONSTANT
# OS
import platform
VERSION = platform.version()
OS = platform.system()
PLATFORM = platform.platform()

#Virus Total
VT_API_KEY = '2b53193d40bb6f730b7b0899ce31cfeb530450684a080b5226e15115cbcb4c77'

#Kicom Anti Virus
KICOMAV = 'python app/tools/kicomav/Release/kAV.py'

#Kibana URL
KIBANA = 'http://localhost:5601'

#ClamAV
CLAMAV = 'clamscan -r --bell -v -i '