import threading
import datetime
import time
import threads_control
import wave
import json
import query

import server_example


class test_arguments:
    def __init__(self, current_speed, id):
        self.current_speed = current_speed
        self.id = id


def _send_query(speed, test_id):
    '''
    function that access the server
    '''
    args = test_arguments(speed, test_id)
    get_server_results(args)


def get_server_results(args):
    '''
    Access the server, and if there was an error log the information
    '''
    try:
        print(args.current_speed)
        server_example.test(args.current_speed)
    except:
        print("SERVER ERROR")
        file_path = 'logs/'+args.id+'.txt'
        f_log = open(file_path,'w')
