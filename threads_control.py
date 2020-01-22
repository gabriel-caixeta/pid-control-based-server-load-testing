import threading
import glob, os
from math import exp
import pid_control

class myThread:
    def __init__(self, function, arg):
        self._thread = threading.Thread(target=function,args = arg)
        self._thread.start()

    def isAlive(self):
        return self._thread.isAlive()

def kill_threads(threads_list):
    for thread in threads_list:
        if not thread.isAlive():
            thread._thread.join()
            threads_list.remove(thread)
    return threads_list

def check_errors():
    os.chdir("logs/")
    err_list = []
    for err_item in glob.glob("*.txt"):
        err_list.append(err_item.replace(".txt",""))
        os.remove(err_item)
    os.chdir("..")
    return err_list


def adjust_speed(speed,limit,counter,prev_err,prev_int):
    '''
    If there are any error files in the log, decrease the testing frequency,
    otherwise, increase the speed
    '''
    # counter = 1 if counter==0 else counter
    errors = check_errors()
    err = len(errors)
    pid_error = -err if err>=1 else counter

    speed, integral  = pid_control.response(pid_error, speed, limit, prev_err, prev_int)


    # if errors:
    #     print("errors:", len(errors) )
    #     speed = speed*(1 + 0.5*len(errors))
    # else:
    #     # speed = 0.95*speed
    #     print("no error, counter:", counter)
    #     speed = 0.95*limit + speed*exp(-2*counter)
    #     # speed = limit/(1-exp(-counter/10))
    # if counter > 10:
    #     speed = speed*0.9

    return speed, errors, integral
