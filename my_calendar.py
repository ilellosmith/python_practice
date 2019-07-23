'''Functions from
RealPython tutorial on mocking @ https://realpython.com/python-mock-library/'''

import datetime
import requests

def is_weekday():
    '''Returns true if today is a weekday'''
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

def get_holidays():
    '''Gets holidays from API'''
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None
