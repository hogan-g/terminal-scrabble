#!/usr/bin/env python3
import requests
import json

class dictionary(): # class to hold the word checker
    API_KEY = "8bf6844a-eabc-480b-a1b6-3525e94e247b"

    def check_word(self, word) -> bool:
        URL = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=" + self.API_KEY
        response = requests.get(URL)
        
        if type(json.loads(response.content)[0]) == type({1:2}):
            return True
        else:
            return False
        
    def check_valid(file): # we wanted to implement a custom dictionary, this method would have checked the dictionary file was valid
        pass