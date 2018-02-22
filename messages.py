import json
import requests
from converter import convert_one_unit

def process_message(messageString):
    """
    Returns a text message
    """
    messageWords = list(messageString.strip().split())
    
    #-----------Help commands----------#
    helpString = "Available commands:\n >Help [x]\n >Convert [x] to [y]"
    if messageWords[0].strip().upper() == "HELP":
        return helpString
    #----------------------------------#
    
    
    #---------Convert commands---------#
    if messageWords[0].strip().upper() == "CONVERT":
        if len(messageWords) == 2:
            return convert_one_unit(messageWords[1])
            
        if len(messageWords) == 4:
            if messageWords[2].strip().upper() == "TO":
                return convert_one_unit(messageWords[1], messageWords[3])
    #----------------------------------#
    
    return "Sorry, I did not get that."