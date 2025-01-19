import time


break_time_miutes=5
second_pre_minutes=60

break_second=break_time_miutes*second_pre_minutes

while break_second > 0:
    time.sleep(1)
    break_second=break_second-1
    print('resumming in ' + str(break_second)+ 'second')