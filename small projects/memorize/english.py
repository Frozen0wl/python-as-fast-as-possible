import requests
import json
class word_definiton:
    def __init__(self, word):
        self.word = word
        self.res = json.loads(self.get_response().text) # gets the json with information about the word
        #print((self.res))
        if not self.word_exists():     # checks if the word exists
            print("No Definitions Found")
            return
        

    def get_response(self): 
        return requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + self.word)

    def word_exists(self):
        try:
            if self.res['title'] == "No Definitions Found":
                return False
        except:
            return True

    def get_all(self):
        return [self.get_definition(), self.get_synonyms(), self.get_example()]
        

    def get_definition(self):
        return(self.res[0]["meanings"][0]["definitions"][0]["definition"])

    def get_synonyms(self):
        try:
            return(self.res[0]["meanings"][0]["definitions"][0]["synonyms"])
        except:
            return None
    def get_example(self):
        try:
            return(self.res[0]["meanings"][0]["definitions"][0]["example"])
        except:
            return None

    

        
    



            
