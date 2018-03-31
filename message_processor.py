import json
import requests 
import re

def simplify_message(messageString):
    """
    Gets as a parameter a message string
    And returns a simplified expression of that message string
    Ex: input: "Hello! Can you convert BTC to EUR for me?"
        output: "convert btc to eur"
    """
    keyWords = ["weather", "convert", "help"]
    errorMessage = ["error"]
    simplifiedMessage = []
    
    messageString = messageString.lower()
    messageWords = re.split('\W+',messageString)
    
    
    for kw in keyWords: #kw stands for keyword
        for mw in messageWords: #mw stands for messageword
            if kw == mw:
                simplifiedMessage.append(kw)
    
    '''
    This handles cases where there are 2 requests
    (Ex: Help! I need to convert EUR to USD)
    and also cases where the same command is repeated twice
    '''
    if len(simplifiedMessage) is not 1:
        return errorMessage
    
    commandIndex = messageWords.index(simplifiedMessage[0])
    
    #-----------Help pattern----------#
    if simplifiedMessage[0].strip().lower() == "help":
        return simplifiedMessage
    #---------------------------------#
    
    #----------Convert pattern--------#
    if simplifiedMessage[0].strip().lower() == "convert":
        matchObj = re.search(r'convert[, ]*(\w+)[, ]*(to)?[, ]*(\w+)?', messageString)
        if matchObj:
            baseCurrency = None
            resultCurrency = None
            if len(matchObj.groups(0)) == 1:
                baseCurrency = matchObj.group(1)
            elif len(matchObj.groups(0)) == 3:
                baseCurrency = matchObj.group(1)
                resultCurrency = matchObj.group(3)
            
            simplifiedMessage.append(baseCurrency)
            if resultCurrency:
                simplifiedMessage.append(resultCurrency)
        else:
            return errorMessage
    #---------------------------------#
    
    #----------Weather pattern--------#
    if simplifiedMessage[0].strip().lower() == "weather":
        matchObj = re.search(r'weather[, ]*(for)?[, ]*(\w+)[, ]*(\w+)', messageString)
        if matchObj:
            if len(matchObj.groups(0)) == 3:
                weatherCity = matchObj.group(2)
                weatherCountry = matchObj.group(3)
            else:
                weatherCity = matchObj.group(1)
                weatherCountry = matchObj.group(2)
            
            simplifiedMessage.append(weatherCity)
            simplifiedMessage.append(weatherCountry)
        else:
            return errorMessage
    #---------------------------------#

    return simplifiedMessage