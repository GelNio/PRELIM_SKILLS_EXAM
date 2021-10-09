from TempTest import Temperature
import unittest

print(Temperature)

class test_temp(unittest.TestCase):
    def celsius_test(self):
        self.assertEqual(Temperature(celsius=17).kelvin,293.15)
    
    def fahrenheit_test(self):
        self.assertEqual(Temperature(fahrenheit=17).kelvin,264.1)
    
    def kelvin_test(self):
        self.assertEqual(Temperature(kelvin=10).kelvin,20)

    def neg_test(self):
        self.assertEqual(Temperature(kelvin=-10).kelvin,-10)



if __name__== '_main_':
    unittest.main()