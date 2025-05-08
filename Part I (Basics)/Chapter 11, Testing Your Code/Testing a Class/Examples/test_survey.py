import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """Create a survey and a set of responses for use n all the methods"""
        question = "What language did you first learn?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Kiswahili', 'English', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single name is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.responses)

    def test_store_multiple_responses(self):
        """Test that multiple responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()