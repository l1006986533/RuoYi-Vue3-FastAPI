import request from '@/utils/request'

// 查询车辆列表
export function listVehicle(query) {
  return request({
    url: '/system/vehicle/list',
    method: 'get',
    params: query
  })
}

// 获取品牌分布统计
export function getBrandStatistics() {
  return request({
    url: '/system/vehicle/statistics/brand',
    method: 'get'
  })
}

// 获取车型分布统计
export function getModelStatistics() {
  return request({
    url: '/system/vehicle/statistics/model',
    method: 'get'
  })
}

// 获取配置分布统计
export function getConfigStatistics() {
  return request({
    url: '/system/vehicle/statistics/config',
    method: 'get'
  })
}
