'''File for testing my_calendar.py

Function definition and testing based on
RealPython tutorial on mocking @ https://realpython.com/python-mock-library/'''

import unittest
import datetime
from requests.exceptions import Timeout
from unittest.mock import Mock
from unittest.mock import patch
import my_calendar

class TestCalendar(unittest.TestCase):
    '''Tests Calendar for:

        - is_weekday returns True if it's a weekday
        - is_weekday returns False if it's not a weekday
        - get_holidays http request raises timeout
        - get_holidays returns correct dictionary format'''

    def setUp(self):
        self.weekday = datetime.datetime(year=2019, month=1, day=1)
        self.weekend = datetime.datetime(year=2019, month=1, day=5)
        
    #==================================================================
    # is_weekday tests
    
    @patch('my_calendar.datetime')
    def test_is_weekday_true_false(self, mock_date):
        '''test is_weekday() returns true on weekdays and false on weekends'''
        mock_date.datetime.today.return_value = self.weekday
        assert my_calendar.is_weekday()
        mock_date.datetime.today.return_value = self.weekend
        assert not my_calendar.is_weekday()

    #==================================================================
    # get_holidays tests

    def log_request(self, url):
        # Log a fake request for test output purposes
        print(f'Making a request to {url}.')
        print('Request received!')

        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        return response_mock

    @patch('my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests):
        '''test call to get_holidays raises timeout'''
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            my_calendar.get_holidays()
            mock_requests.get.assert_called_once()

    @patch('my_calendar.requests')
    def test_get_holidays_retry(self, mock_requests):
        '''test that get_holidays:
                - raises timeout
                - returns correct value
                - calls .get() the correct number of times'''
        # Create a new Mock to imitate a connection and response
        response_mock = self.log_request('http://localhost/api/holidays')
        # Set the side effect of .get()
        mock_requests.get.side_effect = [Timeout, response_mock]
        # Test that the first request raises a Timeout
        with self.assertRaises(Timeout):
            my_calendar.get_holidays()
        # Now retry, expecting a successful response
        assert my_calendar.get_holidays()['12/25'] == 'Christmas'
        # Finally, assert .get() was called twice
        assert mock_requests.get.call_count == 2


    def tearDown(self):
        self.weekday
        self.weekend

if __name__ == '__main__':
    unittest.main()
