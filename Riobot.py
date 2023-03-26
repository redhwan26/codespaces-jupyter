import numpy as np
import requests
import json
#REPEATE INFLATION SHOULD NOT BE A PERCENTAGE
#address = input('address? street number, street name, state, zip code *spaces no commas\n')
inflation = 0.0297 
years = 0
city = ""
state = ""
zipcode = ""
street = ""

   
def requestInf0():
    years = input('number of years you will be holding onto the property\n')
    street = input('street number and name\n')
    city = input('city?\n')
    state = input('state abriviated *check for proper abriviation\n')
    zipcode = input('zipcode\n')
def getUrl(addy):
    result = [x.strip() for x in addy.split(' ')] #splits all the data into spaces
    st=result[0]
    if(len(result) > 1 ):
        for i in range(1,len(result)-1):
            st += ("%20" + result[i]) 
    url2 ="https://us-autocomplete-pro.api.smartystreets.com/lookup?key=21102174564513388&search=" + st + "&auth-id=&license=us-autocomplete-pro-cloud"
def getROI(p1,p2,p3,p4,p5, years, inflation): #!!! Inflation should a ration or a fraction NOT a Percentage
    v1 = (p2-p1)/p1
    
    v2 = (p3-p2)/p2
    
    v3 = (p4-p3)/p3
    
    v4 = (p5-p4)/p4
    
    avg = (v1+v2+v3+v4)/4
    print(avg)
    Roi = ((1+(avg-inflation))**(years))*100
    
    return Roi
def addressValidation():
    response2 = requests.get(getUrl(address))
    data2 = json.loads(response2.text)
    querystring2 = {"address":"" + data2["suggestions"][0]["street_line"]+", "+ data2["suggestions"][0]["city"]+", "+  data2["suggestions"][0]["state"]+ ", "+ data2["suggestions"][0]["zipcode"]}
    return querystring2

url = "https://realty-mole-property-api.p.rapidapi.com/properties"
querystring = {"address":"" + street + ", " + city + ", " + state + ", " + zipcode} #formate: "5500 Grand Lake Dr, San Antonio, TX, 78244"
headers = {
	"X-RapidAPI-Key": "62959f209fmsh6c0b0dfaca63f84p1576dfjsn4d2ad5113f2b",
	"X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
#print(response.text)
data = json.loads(response.text)
#print(response.json())

dp1 = (data[0]['taxAssessment']['2018']['value'])
dp2 = (data[0]['taxAssessment']['2019']['value'])
dp3 = (data[0]['taxAssessment']['2020']['value'])
dp4 = (data[0]['taxAssessment']['2021']['value'])
dp5 = (data[0]['taxAssessment']['2022']['value'])

print(dp1, dp2, dp3, dp4, dp5)
print(getROI(dp1,dp2,dp3,dp4,dp5, years, inflation))