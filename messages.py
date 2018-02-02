import json
import requests
from converter import PriceConverter

class MessageHandler():
    def __init__(self, priceConverter):
        self.__priceConverter = priceConverter
    
    def process_message(self, messageString):
        messageWords = list(messageString.strip().split())
        
        if len(messageWords) == 2:
            if messageWords[0].strip().upper() == "GET":
                return self.__priceConverter.convert_one_unit(messageWords[1])
            else:
                return "Sorry, I did not get that."
            
        if len(messageWords) == 4:
            if messageWords[0].strip().upper() == "GET" and messageWords[2].strip().upper() == "IN":
                return self.__priceConverter.convert_one_unit(messageWords[1], messageWords[3])
            else:
                return "Sorry, I did not get that."
        
        else:
            return "Sorry, I did not get that."