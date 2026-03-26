from sqlalchemy.ext.asyncio import AsyncSession

from module_admin.dao.vehicle_dao import VehicleDao
from module_admin.entity.vo.vehicle_vo import VehicleQueryModel
from utils.common_util import CamelCaseUtil


class VehicleService:
    """
    车辆管理模块服务层
    """

    @classmethod
    async def get_vehicle_list_services(cls, query_db: AsyncSession, query: VehicleQueryModel):
        """
        获取车辆列表信息service

        :param query_db: orm对象
        :param query: 查询参数对象
        :return: 车辆列表和总数
        """
        vehicle_list, total = await VehicleDao.get_vehicle_list(query_db, query)
        
        # 使用 CamelCaseUtil 转换 SQLAlchemy 对象
        vehicle_list_result = CamelCaseUtil.transform_result(vehicle_list)
        
        return vehicle_list_result, total

    @classmethod
    async def get_brand_statistics_services(cls, query_db: AsyncSession):
        """
        获取品牌分布统计service

        :param query_db: orm对象
        :return: 品牌统计列表
        """
        return await VehicleDao.get_brand_statistics(query_db)

    @classmethod
    async def get_model_statistics_services(cls, query_db: AsyncSession):
        """
        获取车型分布统计service

        :param query_db: orm对象
        :return: 车型统计列表
        """
        return await VehicleDao.get_model_statistics(query_db)

    @classmethod
    async def get_config_statistics_services(cls, query_db: AsyncSession):
        """
        获取配置分布统计service

        :param query_db: orm对象
        :return: 配置统计列表
        """
        return await VehicleDao.get_config_statistics(query_db)
