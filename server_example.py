'''
This simulates a server that takes up to 3s to respond to an inquiry,
but will not respond when there are 5 simultaneous queries (one query every 0.2 seconds)
'''

from random import random
import time

#SERVER SETTINGS
CRASH_FREQUENCY = 0.5
MAX_RESPONSE_TIME = 1

def test(query_frequency):
    if query_frequency < CRASH_FREQUENCY:
        time.sleep(MAX_RESPONSE_TIME)
        raise Exception('There was no response from the server')
    else:
        time.sleep(random()*MAX_RESPONSE_TIME)
    return
