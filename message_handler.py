import json
import requests
import re 
from converter import convert_one_unit
from message_processor import simplify_message
from weather import get_weather_for_city

def handle_message(messageString):
    """
        Given a message, handles the user request from the message and returns the a response
        Input: the text message from the user (string)
        Output: the response text message for the user (string)
    """
    
    messageWords = simplify_message(messageString)
    
    #-----------Help commands----------#
    '''
    More commands can be added here over time
    '''
    helpString = "Hello!"
    helpString += "Available commands:\n"
    helpString += " >Help\n"
    helpString += " >Convert <base_currency> [to] [<result_currency>]\n"
    helpString += " >Weather [for] <city> <country>\n"
    
    if messageWords[0].strip().lower() == "help":
        return helpString
    #----------------------------------#
    
    #---------Convert commands---------#
    if messageWords[0].strip().lower() == "convert":
        if len(messageWords) == 2:
            return convert_one_unit(messageWords[1])
            
        if len(messageWords) == 3:
            return convert_one_unit(messageWords[1], messageWords[2])
    #----------------------------------#
    
    #---------Weather commands---------#
    if messageWords[0].strip().lower() == "weather":
        return get_weather_for_city(messageWords[1], messageWords[2])
    #----------------------------------#
    
    return "Sorry, I did not get that."