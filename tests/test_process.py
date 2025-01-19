"""
Unit test for the process module.
"""

import dotenv
dotenv.load_dotenv('.env')
import unittest
import logging
import process


class Test(unittest.TestCase):
    """
    collection of test related to event processing

    """

    # def test_data_quality_check(self):
    #     """
    #     Try the process to check data quality
    #     """
    #     test_event = {
    #         'type': 'CHECK_DATA_QUALITY'
    #     }
    #     process.event_processor(test_event)
    
    def test_get_candidates(self):
        """
        Try the process to get candidates
        """
        test_event = {
        "type": "GET_NUMBER_OF_CANDIDATES",
        "medical_problem": "Diabetes",
        "medical_medication": "Ibuprofen",
        "medical_vaccine": "Varicella"
        }
        process.event_processor(test_event)
    