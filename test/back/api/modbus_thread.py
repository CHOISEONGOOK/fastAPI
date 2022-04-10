import time
from threading import Thread, Lock
from pyModbusTCP.client import ModbusClient

SERVER_HOST = "121.179.67.14"
SERVER_PORT = 15899

# set global
regs = []

# init a thread lock
regs_lock = Lock()


def polling_thread():
    """Modbus polling thread."""
    global regs, regs_lock
    c = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, auto_open=True)
    # polling loop
    while True:
        # do modbus reading on socket
        reg_list = c.read_holding_registers(0, 10)
        # if read is ok, store result in regs (with thread lock)
        if reg_list:
            with regs_lock:
                regs = list(reg_list)
        # 1s before next polling
        time.sleep(1)


# start polling thread
tp = Thread(target=polling_thread)
# set daemon: polling thread will exit if main thread exit
tp.daemon = True
tp.start()

# display loop (in main thread)
while True:
    # print regs list (with thread lock synchronization)
    with regs_lock:
        print(regs)
    # 1s before next print
    time.sleep(1)

#try:
#    c = ModbusClient (host = SERVER_HOST, port = SERVER_PORT, auto_open=True, auto_close=True)
#except ValueError:
#    print("Error with host or port params")