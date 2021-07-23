import requests
import json

""" 
Here are some sample API sources to test with. Please note, the dad-joke API is limited capacity (for free)
and requires registration 
"""

URL = "http://api.icndb.com/jokes/random?exclude=[explicit]"
#URL = "http://api.icndb.com/jokes/random?limitTo=[nerdy]"
URL2 = "https://dad-jokes.p.rapidapi.com/joke/type/knock-knock"
#URL2 = "https://dad-jokes.p.rapidapi.com/joke/type/programming"
headers = {
    'x-rapidapi-key': "9fbf30bc6amsh6613788b5a52723p13d9a4jsna3b45112690b",
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
    }


# r = requests.get(url = URL)
# data = r.json()
# #print (r.json())
# joke = data['value']['joke']
# #['joke']
# print ()
# print ()
# print (joke)
# print ()
# print ()


r = requests.get(url = URL2, headers = headers)
data = r.json()
#print (data)
setup = data['body'][0]['setup']
punchline = data['body'][0]['punchline']
print ()
print ("Q: " + setup)
print ()
print ("A: " + punchline)
print ()
