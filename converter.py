import requests

def convert_one_unit(base_currency, result_currency = "USD"):
    """
        Gets the value of 1 unit of base_currency converted to result_currency
        Input: base currency (string) and result currency (string)
               the standard result currency is USD
        Output: the converted value from base currency to result currency
    """
    
    #CryptoCompare API accepts only uppercase strings for currency names
    #It returns the needed data in form of a json file, which after being parsed becomes a dictionary
    
    base_currency = base_currency.strip().upper()
    result_currency = result_currency.strip().upper()
    
    request = "https://min-api.cryptocompare.com/data/price?fsym="+ base_currency + "&tsyms=" + result_currency
    response = requests.get(request)
    data = response.json()
    
    #If we encountered an error, we handle it
    if "Error" in data.values():
        #TO DO: Handle error properly
        for error_report in data.values():
            if "There is no data for the symbol" in error_report:
                return "Invalid currency"
        
        return list(data.values())
        
    return data[result_currency]

