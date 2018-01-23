# !/user/bin/python3
# -*-coding:UTF-8-*-

import threading
from time import sleep
from datetime import datetime

loops = [1, 2, 3, 2, 1]
date_time_format = '%y-%M-%d %H:%M:%S'


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)


def loop(n_loop, n_sec):
    print('Thread NO. ', n_loop, ' Started',
          date_time_str(datetime.now()), 'Sleep now ', n_sec, 's')
    sleep(n_sec)
    print('Thread No. ', n_loop, ' End ', date_time_str(datetime.now()))


def main():
    print('All threads starting :', datetime.now())
    threads = []
    nloops = range(len(loops))
    print(nloops)

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('ALL threads end', datetime.now())


if __name__ == '__main__':
    main()
