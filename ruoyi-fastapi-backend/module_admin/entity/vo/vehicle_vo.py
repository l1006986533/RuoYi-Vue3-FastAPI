from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class VehicleModel(BaseModel):
    """
    车辆表对应pydantic模型
    """

    model_config = ConfigDict(alias_generator=to_camel, from_attributes=True)

    vehicle_id: int | None = Field(default=None, description='车辆id')
    vin: str | None = Field(default=None, description='VIN码')
    brand: str | None = Field(default=None, description='品牌')
    model: str | None = Field(default=None, description='车型')
    config: str | None = Field(default=None, description='配置')
    status: Literal['online', 'offline', 'unknown'] | None = Field(default=None, description='状态（online在线 offline离线 unknown未知）')
    create_time: datetime | None = Field(default=None, description='创建时间')
    update_time: datetime | None = Field(default=None, description='更新时间')


class VehicleQueryModel(BaseModel):
    """
    车辆管理分页查询模型
    """

    model_config = ConfigDict(alias_generator=to_camel)

    page_num: int = Field(default=1, description='当前页码')
    page_size: int = Field(default=10, description='每页条数')
    keyword: str | None = Field(default=None, description='关键词（VIN码等）')
    brand: str | None = Field(default=None, description='品牌')
    status: str | None = Field(default=None, description='状态')
