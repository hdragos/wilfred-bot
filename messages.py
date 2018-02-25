import json
import requests
import re 
from converter import convert_one_unit

def process_message(messageString):
    """
    Returns a text message based on the messageString
    """
    messageWords = list(messageString.strip().split())
    
    #-----------Help commands----------#
    match = re.search("HELP", messageWords[0].strip().upper())
    helpString = "Available commands:\n >Help [x]\n >Convert [x] to [y]"
    
    if match:
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
    
    #---------Weather commands---------#
    """
    TO DO
    """
    #----------------------------------#
    
    return "Sorry, I did not get that."