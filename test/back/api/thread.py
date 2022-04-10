import threading
import time
from datetime import datetime

#sleeptime = input()
sleeptime = 0.5

class Tread1(threading.Thread):
    def run(self) -> None:
        for i in range(10):
            now=datetime.now()
            print(now)
            time.sleep(int(sleeptime))


class Tread2(threading.Thread):
    def run(self) -> None:
        for i in range(100):
            print(i)
#            time.sleep(int(sleeptime)*2)

t1 = Tread1()
t1.start()
t2 = Tread2()
#t2.daemon = True
t2.start()