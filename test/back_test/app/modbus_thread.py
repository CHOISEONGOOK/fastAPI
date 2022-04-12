import time
from threading import Thread, Lock
from pyModbusTCP.client import ModbusClient

# Database
from database.db_test import session
from models.model_test import SolardataTable, Solardata

import codecs

SERVER_HOST = "192.168.0.158"
SERVER_PORT = 502

# set global
regs = []

# init a thread lock
regs_lock = Lock()

class data_conversion():
    def int2hex(intdata):
        hexdata = hex(intdata)[2:]

        return hexdata
    
    def hex2asscii(hexdata):
        assciidata = codecs.decode(hexdata, "hex")
        assciidata = assciidata.decode('ASCII')

        return assciidata


class polling_thread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """Modbus polling thread."""
        global regs, regs_lock

        try:
            c = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, auto_open=True)
        except ValueError:
            print("Error with host or port params")

        # polling loop
        while True:
            # do modbus reading on socket
            reg_list = c.read_holding_registers(0, 34)

            # if read is ok, store result in regs (with thread lock)
            if reg_list:
                with regs_lock:
                    regs = list(reg_list)

                    conversion_hexdata = []
                    conversion_data = []

                    for i in range(len(regs)):
                        conversion_hexdata.append(data_conversion.int2hex(regs[i]))
                        conversion_data.append(data_conversion.hex2asscii(conversion_hexdata[i]))

                    out_data = []
                    out_data.append("".join(conversion_data[0]))
                    out_data.append("".join(conversion_data[1:3]))
                    out_data.append("".join(conversion_data[3:5]))
                    out_data.append("".join(conversion_data[5:7]))
                    out_data.append("".join(conversion_data[7:9]))
                    out_data.append("".join(conversion_data[9:11]))
                    out_data.append("".join(conversion_data[11:13]))
                    out_data.append("".join(conversion_data[13:15]))
                    out_data.append("".join(conversion_data[15:17]))
                    out_data.append("".join(conversion_data[17:19]))
                    out_data.append("".join(conversion_data[19:21]))
                    out_data.append("".join(conversion_data[21:23]))
                    out_data.append("".join(conversion_data[23:25]))
                    out_data.append("".join(conversion_data[25:27]))
                    out_data.append("".join(conversion_data[27:31]))
                    out_data.append("".join(conversion_data[31]))
                    out_data.append("".join(conversion_data[32]))
                    out_data.append("".join(conversion_data[33]))

                    Solardata = SolardataTable()
                    Solardata.phase                 = out_data[0]
                    Solardata.power_capacity        = out_data[1]
                    Solardata.rated_line_voltage    = out_data[2]
                    Solardata.pv_voltage            = out_data[3]
                    Solardata.pv_current            = out_data[4]
                    Solardata.pv_generated_power    = out_data[5]
                    Solardata.RS_voltage            = out_data[6]
                    Solardata.ST_voltage            = out_data[7]
                    Solardata.TR_voltage            = out_data[8]
                    Solardata.frequency             = out_data[9]
                    Solardata.R_current             = out_data[10]
                    Solardata.S_current             = out_data[11]
                    Solardata.T_current             = out_data[12]
                    Solardata.generated_power       = out_data[13]
                    Solardata.Total_generated_power = out_data[14]
                    Solardata.line_power_loss       = out_data[15]
                    Solardata.run_stop              = out_data[16]
                    Solardata.fault_number          = out_data[17]

                    session.add(Solardata)
                    session.commit()


                    print(out_data)
            # 1s before next polling
            time.sleep(10)


# start polling thread
tp = polling_thread()

# set daemon: polling thread will exit if main thread exit
tp.daemon = True
tp.start()

# # display loop (in main thread)
# while True:
#     # print regs list (with thread lock synchronization)
#     with regs_lock:
#         print(regs)
#     # 1s before next print
#     time.sleep(1)
