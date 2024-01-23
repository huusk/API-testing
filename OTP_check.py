import random

otp = random.randrange(100000, 1000000)
print(otp)
user = int(input("enter the otp"))
if user == otp:
    print("access granted")
else:
    print("access")

import json
import unittest
import json
import unittest
#
# class TestResponse(unittest.TestCase):
#     def setUp(self):
#         # Load the response.json file with 'utf-8' encoding
#         with open('expect_json.json', 'r', encoding='utf-8') as file:
#             self.response_data = json.load(file)
#
#     def test_response_contains_request_keys(self):
#         # Check if the "request" key is present in response.json
#         self.assertIn("request", self.response_data)
#
#         # If "request" key is present, check if "cmd" and "msisdn" keys are present within it
#         if "request" in self.response_data:
#             request_data = self.response_data["request"]
#             self.assertIn("cmd", request_data)
#             self.assertIn("msisdn", request_data)
#
