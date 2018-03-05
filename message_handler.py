import json
import requests
import re 
from converter import convert_one_unit
from message_processor import simplify_message

def handle_message(messageString):
    """
    Returns a text message based on the messageString
    """
    
    messageWords = simplify_message(messageString)
    
    '''
    Alternatively, the previous line can be replaced with the following,
    but this comes with 
       
     messageWords = list(messageString.strip().split())
    '''
    
    #-----------Help commands----------#
    helpString = "Available commands:\n >Help [x]\n >Convert [x] to [y]"
    
    if messageWords[0].strip().lower() == "help":
        return helpString
    #----------------------------------#
    
    
    #---------Convert commands---------#
    if messageWords[0].strip().lower() == "convert":
        if len(messageWords) == 2:
            return convert_one_unit(messageWords[1])
            
        if len(messageWords) == 4:
            if messageWords[2].strip().lower() == "to":
                return convert_one_unit(messageWords[1], messageWords[3])
    #----------------------------------#
    
    #---------Weather commands---------#
    if messageWords[0].strip().lower() == "weather":
        return "It's raining somewhere."
    #----------------------------------#
    
    return "Sorry, I did not get that."