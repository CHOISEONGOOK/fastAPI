from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


# coding: utf-8


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