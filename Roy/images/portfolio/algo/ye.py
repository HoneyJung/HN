
# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://yeseul.wisen.space/data.json"
  

  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
print("eiheihei")
# extracting data in json format 
data = r.json() 
print(data)