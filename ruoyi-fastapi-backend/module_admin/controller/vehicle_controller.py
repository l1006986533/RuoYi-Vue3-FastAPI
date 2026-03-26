from typing import Annotated

from fastapi import Query, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from common.aspect.db_seesion import DBSessionDependency
from common.router import APIRouterPro
from common.vo import ResponseBaseModel
from module_admin.entity.vo.vehicle_vo import VehicleQueryModel
from module_admin.service.vehicle_service import VehicleService
from utils.log_util import logger
from utils.response_util import ResponseUtil

vehicle_controller = APIRouterPro(
    prefix='/system/vehicle', order_num=7, tags=['系统管理-车辆管理']
)


@vehicle_controller.get(
    '/list',
    summary='获取车辆列表接口',
    description='用于获取车辆列表（支持分页、关键词、品牌、状态筛选）',
    response_model=ResponseBaseModel,
)
async def get_system_vehicle_list(
    request: Request,
    query: Annotated[VehicleQueryModel, Query()],
    query_db: Annotated[AsyncSession, DBSessionDependency()],
) -> Response:
    vehicle_list, total = await VehicleService.get_vehicle_list_services(query_db, query)
    logger.info('获取车辆列表成功')
    
    return ResponseUtil.success(rows=vehicle_list, dict_content={'total': total})
