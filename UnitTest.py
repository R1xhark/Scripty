import unittest
import logging
import datetime
import os
from exchange import exchangeable_value

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

log_dir = "/Users/macbook/Library/Application Support/JetBrains/PyCharm2023.2/scratches/Exersism/ExchangePackage/TestLogs"
os.makedirs(log_dir,exist_ok=True)

log_file_name = f"exchange_test_{timestamp}.log"

logging.basicConfig(
    level=logging.DEBUG,
    filename=log_file_name,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
class TestExchangeFunctions(unittest.TestCase):
    def test_exchangeable_value(self):
        logging.debug("Starting test_exchangeable_value")
        inputs = [
            (100000, 10.61, 10, 1),
            (1500, 0.84, 25, 40),
            (470000, 1050, 30, 10000000000),
            (470000, 0.00000009, 30, 700),
            (425.33, 0.0009, 30, 700)
        ]
        output_data = [8568, 1400, 0, 4017094016600, 363300]

        for variant, (input_data, expected_output) in enumerate(zip(inputs, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, expected_output=expected_output):
                self.assertEqual(exchangeable_value(*input_data), expected_output)
        logging.info("Test completed successfully")

if __name__ == '__main__':
    unittest.main()
