## System
import time

## Database
from database.db_test import session
from models.model_test import UserTable, User

## Thread (modbus)
from app.modbus_thread import polling_thread


while True:
    time.sleep(10)