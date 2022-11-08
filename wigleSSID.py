import requests

#Insert encoded API key below
apiKey="redacted"

ssid=input("What SSID? \n")

#Prompt user for SSID and format/send request
apiKeyHeader={"Authorization": "Basic {0}".format(apiKey)}
url= 'https://api.wigle.net/api/v2/network/search?onlymine=false&latrange1=-90&latrange2=90&longrange1=-180&longrange2=180&closestLat=37&closestLong=-77&freenet=false&paynet=false&ssid=%s&resultsPerPage=5' %ssid
req=requests.get(url, headers=apiKeyHeader)

#Convert to json to make searchable
ret=req.json()
jsonFormatted = json.dumps(ret, indent=4)
jsonSearch = json.loads(jsonFormatted)

#Show number of results. If too many, inform of result limit.
results= jsonSearch['results']
print("Number of results: " + str(len(results)))
if len(results) > 4:
    print("Search was limited to 5 results")
    
#Print SSID, then print each address found    
print(results[0]['ssid'])
for i in range (0, (len(results))):
    print("--------Address:--------")
    print(results[i]['housenumber']+" "+results[i]['road'])
    print(str(results[i]['city'])+", "+results[i]['region']+" " +results[i]['postalcode'])
    print(results[i]['country'])
    print("Last update: "+results[i]['lastupdt'] + "\n")

#TO-DO: add option for lat/long restriction or country/region search