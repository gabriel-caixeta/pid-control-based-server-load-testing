#coding:utf-8

from multiprocessing import Pool
# import _thread
import threading
import datetime
import time
import threads_control
import csv
# import json
import query

# Send a query every x seconds
TEST_FREQUENCY = 1
CRASH_FREQUENCY = 0.5
# Number of simultaneous threads
SIMULTANEOUS_THREAD_COUNT = 50


if __name__ == '__main__':
    last_test = datetime.datetime.now()
    now = last_test
    running_threads = []

    counter = 0
    test_set = []
    input_file = "input_test.csv"
    with open(input_file,'r') as f_input:
        reader = csv.reader(f_input)
        for row in reader:
            if not row[0] == 'test_id':
                test_set.append(row[0])

    test_speed = TEST_FREQUENCY
    max_frequency = CRASH_FREQUENCY
    prev_err = 0
    prev_int = 0
    counter = 1
    next_test_id = test_set[0]
    while True:
        while len(running_threads) < SIMULTANEOUS_THREAD_COUNT:
            while now < last_test + datetime.timedelta(seconds=test_speed):
                now = datetime.datetime.now()
            # print(len(running_threads))

            time_diff = now - last_test
            print(next_test_id,"New thread started after " + str(time_diff.total_seconds()) + "seconds", threading.activeCount(), len(running_threads),max_frequency)
            # counter += 1
            last_test = now
            new_thread = threads_control.myThread(query._send_query,(test_speed,next_test_id))
            running_threads.append(new_thread)
            test_set.remove(next_test_id)

            with open("data.csv","a+") as f_data:
                f_data.write(str(test_speed)+'\n')

            # adjust testing speed
            test_speed, err, prev_int = threads_control.adjust_speed(test_speed, max_frequency,counter, prev_int, prev_err)
            prev_err = len(err)

            # add error cases for later testing
            if err:
                for item in err:
                    test_set.append(item)
                err = []
                # max_frequency = test_speed
                counter = 1
            else:
                # max_frequency = test_speed if test_speed < max_frequency else max_frequency
                counter += 1

            # count += 0 if err else 1

            if test_set:
                next_test_id = test_set[0]
            else:
                while(threading.activeCount()>1):
                    running_threads = threads_control.kill_threads(running_threads)
                print("FINISHED")
                exit()

            # kill unused threads
            if threading.activeCount() <= len(running_threads):
                running_threads = threads_control.kill_threads(running_threads)

        # reached the limit for local parallel threads,
        # try and kill threads as they finish so it can start new threads
        if threading.activeCount() <= SIMULTANEOUS_THREAD_COUNT:
            running_threads = threads_control.kill_threads(running_threads)
