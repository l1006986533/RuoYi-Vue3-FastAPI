from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from config.database import Base


class SysVehicle(Base):
    """
    车辆信息表
    """

    __tablename__ = 'sys_vehicle'
    __table_args__ = {'comment': '车辆信息表'}

    vehicle_id = Column(Integer, primary_key=True, autoincrement=True, comment='车辆id')
    vin = Column(String(50), nullable=False, unique=True, comment='VIN码')
    brand = Column(String(50), nullable=False, comment='品牌')
    model = Column(String(100), nullable=False, comment='车型')
    config = Column(String(50), nullable=False, comment='配置')
    status = Column(String(20), nullable=False, server_default='unknown', comment='状态（online在线 offline离线 unknown未知）')
    create_time = Column(DateTime, nullable=True, default=datetime.now, comment='创建时间')
    update_time = Column(DateTime, nullable=True, default=datetime.now, comment='更新时间')
