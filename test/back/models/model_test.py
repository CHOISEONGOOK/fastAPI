# coding: utf-8
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from database.db_test import Base
from database.db_test import ENGINE


class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=True)
    age = Column(Integer)


class User(BaseModel):
    id   : int
    name : str
    age  : int

class SolardataTable(Base):
    __tablename__ = 'solardata'
    data_id                 = Column(Integer, primary_key=True, autoincrement=True)
    phase                   = Column(Integer, nullable=True)
    power_capacity          = Column(Integer, nullable=True)
    rated_line_voltage      = Column(Integer, nullable=True)
    pv_voltage              = Column(Integer, nullable=True)
    pv_current              = Column(Integer, nullable=True)
    pv_generated_power      = Column(Integer, nullable=True)
    RS_voltage              = Column(Integer, nullable=True)
    ST_voltage              = Column(Integer, nullable=True)
    TR_voltage              = Column(Integer, nullable=True)
    frequency               = Column(Integer, nullable=True)
    R_current               = Column(Integer, nullable=True)
    S_current               = Column(Integer, nullable=True)
    T_current               = Column(Integer, nullable=True)
    generated_power         = Column(Integer, nullable=True)
    Total_generated_power   = Column(Integer, nullable=True)
    line_power_loss         = Column(Integer, nullable=True)
    run_stop                = Column(Integer, nullable=True)
    fault_number            = Column(Integer, nullable=True)
    

class Solardata(BaseModel):
    data_id                 : int
    phase                   : int
    power_capacity          : int
    rated_line_voltage      : int
    pv_voltage              : int
    pv_current              : int
    pv_generated_power      : int
    RS_voltage              : int
    ST_voltage              : int
    TR_voltage              : int
    frequency               : int
    R_current               : int
    S_current               : int
    T_current               : int
    generated_power         : int
    Total_generated_power   : int
    line_power_loss         : int
    run_stop                : int
    fault_number            : int


def main():
    # Table 없으면 생성
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main()