import requests
import json

#Insert API key below
apiKey='redacted'

apiKeyHeader = {'Content-Type': "application/json", 'X-api-key': '{0}'.format(apiKey)}
targetLI=input("Enter target LinkedIn URL \n e.g. linkedin.com/in/target-person-012345 \n")
url='https://api.peopledatalabs.com/v5/person/enrich?pretty=True&profile={0}'.format(targetLI)
req=requests.get(url, headers=apiKeyHeader)
result=req.json()
json_formatted_str = json.dumps(result, indent=4)
print(json_formatted_str)