import request from '@/utils/request'

// 查询车辆列表
export function listVehicle(query) {
  return request({
    url: '/system/vehicle/list',
    method: 'get',
    params: query
  })
}
