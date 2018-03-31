from message_processor import simplify_message
import unittest

class TestCaseSimplifyMessage(unittest.TestCase):
    def setUp(self):
        #Preparation phase
        pass
        
    def tearDown(self):
        #Cleanup phase
        pass
    
    def testConvert(self):
        #Convert with base currency and result currency
        inputString = "Hey, convert btc to eur for me, please"
        actualWordList = simplify_message(inputString)
        expectedWordList = ["convert", "btc", "eur"]
        
        self.assertEqual(actualWordList, expectedWordList, "Test 1: Failed. Invalid conversion simplification")
        
        #Convert only with base currency
        inputString = "Hey, convert btc"
        actualWordList = simplify_message(inputString)
        expectedWordList = ["convert", "btc"]
        
        self.assertEqual(actualWordList, expectedWordList, "Test 2: Failed. Invalid conversion simplification")
        
        #Incomplete conversion request
        inputString = "Do convert"
        actualWordList = simplify_message(inputString)
        expectedWordList = ["error"]
        
        self.assertEqual(actualWordList, expectedWordList, "Test 3: Failed. Invalid conversion simplification")
        
        
    def testHelp(self):
        #Simple help request
        inputString = "Hello, i would need some help"
        actualWordList = simplify_message(inputString)
        expectedWordList = ["help"]
        
        self.assertEqual(actualWordList, expectedWordList, "Test 4: Failed. Invalid help simplification")

    def testWeather(self):
        #Request with 'for'
        inputString = "Hello, I would need to know the weather for Bucharest, Romania."
        actualWordList = simplify_message(inputString)
        expectedWordList = ["weather", "bucharest", "romania"]
        
        self.assertEqual(actualWordList, expectedWordList, "Test 5: Failed. Invalid weather simplification")
        
        #Request without 'for'
        inputString = "Weather bucharest romania"
        actualWordList = simplify_message(inputString)
        expectedWordList = ["weather", "bucharest", "romania"]
        
        self.assertEqual(actualWordList, expectedWordList, "Test 6: Failed. Invalid weather simplification")
        
        #Incomplete weather request 
        inputString = "Can you tell me the weather"
        actualWordList = simplify_message(inputString)
        expectedWordList = ["error"]
        
        self.assertEqual(actualWordList, expectedWordList, "Test 7: Failed. Invalid weather simplification")
        
if __name__ == '__main__':
    unittest.main()