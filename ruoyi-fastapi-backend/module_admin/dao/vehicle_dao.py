from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from module_admin.entity.do.vehicle_do import SysVehicle
from module_admin.entity.vo.vehicle_vo import VehicleQueryModel


class VehicleDao:
    """
    车辆管理模块数据库操作层
    """

    @classmethod
    async def get_vehicle_list(cls, db: AsyncSession, query: VehicleQueryModel):
        """
        获取车辆列表（分页）

        :param db: orm对象
        :param query: 查询参数对象
        :return: 车辆列表和总数
        """
        # 构建查询条件
        query_filter = []
        
        if query.keyword:
            query_filter.append(SysVehicle.vin.like(f'%{query.keyword}%'))
        
        if query.brand:
            query_filter.append(SysVehicle.brand == query.brand)
        
        if query.status:
            query_filter.append(SysVehicle.status == query.status)
        
        # 查询总数
        count_stmt = select(func.count()).select_from(SysVehicle).where(*query_filter)
        total = (await db.execute(count_stmt)).scalar()
        
        # 查询列表
        list_stmt = (
            select(SysVehicle)
            .where(*query_filter)
            .order_by(SysVehicle.create_time.desc())
            .offset((query.page_num - 1) * query.page_size)
            .limit(query.page_size)
        )
        result = await db.execute(list_stmt)
        vehicle_list = result.scalars().all()
        
        return list(vehicle_list), total
