import  json
import  requests
app_id = "33fe3d85"
app_key = "6468f3d65c1c01d34c874074fea2e4ef"

endpoint = "entries"
language_code = "en-us"
word_id = "depletion"

url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()+"?"+"fields=examples&strictMatch=false"

r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})

print(json.loads(r.text)["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["examples"]) # prints the examples
