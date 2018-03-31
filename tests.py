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
        inputString = "Hey, convert btc to eur for me, please"
        actualWordList = simplify_message(inputString)
        expectedWordList = ["convert", "btc", "to", "eur"]
        
        self.assertEqual(actualWordList, expectedWordList, "Test 1: Failed. Invalid conversion simplification")
        
    def testHelp(self):
        inputString = "Hello, i would need some help"
        actualWordList = simplify_message(inputString)
        expectedWordList = ["help"]
        
        self.assertEqual(actualWordList, expectedWordList, "Test 2: Failed. Invalid help simplification")

    def testWeather(self):
        inputString = "Hello, I would need to know the weather for Bucharest, Romania."
        actualWordList = simplify_message(inputString)
        expectedWordList = ["weather", "bucharest", "romania"]
        
        self.assertEqual(actualWordList, expectedWordList, "Test 3: Failed. Invalid weather simplification")
        
        inputString = "Weather bucharest romania"
        actualWordList = simplify_message(inputString)
        expectedWordList = ["weather", "bucharest", "romania"]
        
        self.assertEqual(actualWordList, expectedWordList, "Test 4: Failed. Invalid weather simplification")
        
if __name__ == '__main__':
    unittest.main()