from unittest.mock import Mock
from lib.time_error import *

def test_error_time():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {'abbreviation': 'GMT', 
                                        'client_ip': '82.163.117.26', 
                                        'datetime': '2023-11-21T10:53:05.220996+00:00', 
                                        'day_of_week': 2, 
                                        'day_of_year': 325, 
                                        'dst': False, 
                                        'dst_from': None, 
                                        'dst_offset': 0, 
                                        'dst_until': None, 
                                        'raw_offset': 0, 
                                        'timezone': 'Europe/London', 
                                        'unixtime': 1700563985, 
                                        'utc_datetime': '2023-11-21T10:53:05.220996+00:00', 
                                        'utc_offset': '+00:00', 
                                        'week_number': 47}
    
    time_mock = Mock(name="time")
    time_mock.time.return_value = 1700563985.1

    time_error = TimeError(requester_mock, time_mock)
    
    assert time_error.error() == 1700563985 - 1700563985.1
