import requests
import json
from bs4 import BeautifulSoup

#Add VirusTotal API key below
vtApiKey='redacted'

targetIp=str(input("What IP Address? \n"))

###VPN Attribution via Spur.us###

#Query spur.us for the target IP, format HTML result
SpurUrl='https://spur.us/context/{0}'.format(targetIp)
req=requests.get(SpurUrl)
html=req.content
soup=BeautifulSoup(html, "html.parser")

#Carve the relevant HTML segments and print the first one
htmlClass = soup.find('div', class_='col-lg-10 col-xl-8 white-card')
lines = htmlClass.find_all('p') 
print("--------Spur.us VPN Attribution-------- ")
print(lines[0].text.strip(" \n\t\r"))

###Virus Total IP Information###

#Request info from Virus Total API
VtUrl='https://www.virustotal.com/vtapi/v2/ip-address/report?apikey={0}&ip={1}'.format(vtApiKey, targetIp)
req2=requests.get(VtUrl)

#Convert to json to make searchable
result=req2.json()
jsonFormatted = json.dumps(result, indent=4)
jsonSearch = json.loads(jsonFormatted)

#Print relevant fields
print("--------IP info from Virus Total--------")
try:
    print("ASN: " + str(jsonSearch['asn']))
    print("AS Owner: " + jsonSearch['as_owner'])
    print("Country: " + jsonSearch['country'])
except:
    print("Error finding ASN/Geolocation")
try:
    print("Associated domains:")
    for i in range (0, (len(jsonSearch['resolutions']))):
        print("    " + jsonSearch['resolutions'][i]['hostname'])
except:
    print("Error finding associated domains")