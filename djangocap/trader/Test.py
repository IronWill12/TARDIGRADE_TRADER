import requests

url = "https://amazon-products1.p.rapidapi.com/search"

querystring = {"country":"US","query":"MacBook+Pro","page":"1","categoryId":"165793011"}

headers = {
	"X-RapidAPI-Host": "amazon-products1.p.rapidapi.com",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)