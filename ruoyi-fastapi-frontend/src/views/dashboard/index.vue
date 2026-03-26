<template>
  <div class="app-container">
    <!-- 统计卡片区域 -->
    <el-row :gutter="20" class="panel-group">
      <el-col :xs="12" :sm="12" :lg="8" class="card-panel-col">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-total">
            <el-icon class="card-panel-icon"><Van /></el-icon>
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">车辆总数</div>
            <div class="card-panel-num">{{ statistics.total }}</div>
          </div>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :lg="8" class="card-panel-col">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-online">
            <el-icon class="card-panel-icon"><CircleCheck /></el-icon>
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">在线车辆总数</div>
            <div class="card-panel-num">{{ statistics.online }}</div>
            <div class="card-panel-trend down">
              <el-icon><ArrowDown /></el-icon>
              <span>比上月 12%</span>
            </div>
          </div>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :lg="8" class="card-panel-col">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-offline">
            <el-icon class="card-panel-icon"><CircleClose /></el-icon>
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">离线车辆总数</div>
            <div class="card-panel-num">{{ statistics.offline }}</div>
            <div class="card-panel-trend up">
              <el-icon><ArrowUp /></el-icon>
              <span>比上月 24%</span>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>

    <!-- 图表区域 -->
    <el-row :gutter="20" class="chart-group">
      <el-col :xs="24" :sm="24" :lg="8">
        <el-card class="chart-card">
          <template #header>
            <div class="chart-header">
              <span>品牌</span>
            </div>
          </template>
          <div ref="brandChart" class="chart-container"></div>
        </el-card>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="8">
        <el-card class="chart-card">
          <template #header>
            <div class="chart-header">
              <span>车型</span>
            </div>
          </template>
          <div ref="modelChart" class="chart-container"></div>
        </el-card>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="8">
        <el-card class="chart-card">
          <template #header>
            <div class="chart-header">
              <span>配置</span>
            </div>
          </template>
          <div ref="configChart" class="chart-container"></div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup name="Dashboard">
import * as echarts from 'echarts'
import { getBrandStatistics, getModelStatistics, getConfigStatistics } from '@/api/system/vehicle'
import { Van, CircleCheck, CircleClose, ArrowUp, ArrowDown } from '@element-plus/icons-vue'

// Mock 统计数据
const statistics = ref({
  total: '1,098,500',
  online: '693,700',
  offline: '404,800'
})

// 图表引用
const brandChart = ref(null)
const modelChart = ref(null)
const configChart = ref(null)

// 图表实例
let brandChartInstance = null
let modelChartInstance = null
let configChartInstance = null

// 初始化品牌饼图
function initBrandChart(data) {
  brandChartInstance = echarts.init(brandChart.value, 'macarons')
  brandChartInstance.setOption({
    tooltip: {
      trigger: 'item',
      formatter: '{b}: {c} ({d}%)'
    },
    legend: {
      show: false
    },
    series: [
      {
        name: '品牌',
        type: 'pie',
        radius: ['40%', '70%'],
        center: ['50%', '45%'],
        avoidLabelOverlap: true,
        itemStyle: {
          borderRadius: 10,
          borderColor: '#fff',
          borderWidth: 2
        },
        label: {
          show: true,
          position: 'outside',
          formatter: '{b}'
        },
        labelLine: {
          show: true,
          length: 10,
          length2: 10
        },
        data: data
      }
    ]
  })
}

// 初始化车型柱状图
function initModelChart(data) {
  modelChartInstance = echarts.init(modelChart.value, 'macarons')
  const xData = data.map(item => item.name)
  const yData = data.map(item => item.value)
  
  modelChartInstance.setOption({
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      top: '10%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: xData,
      axisTick: {
        alignWithLabel: true
      }
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        name: '数量',
        type: 'bar',
        barWidth: '60%',
        data: yData,
        itemStyle: {
          borderRadius: [4, 4, 0, 0]
        }
      }
    ]
  })
}

// 初始化配置饼图
function initConfigChart(data) {
  configChartInstance = echarts.init(configChart.value, 'macarons')
  
  // 颜色映射：高配=蓝色, 中配=红色, 低配=黄色
  const colorMap = {
    '高配': '#409EFF',
    '中配': '#F56C6C',
    '低配': '#E6A23C'
  }
  
  // 为数据添加颜色
  const coloredData = data.map(item => ({
    ...item,
    itemStyle: {
      color: colorMap[item.name] || undefined
    }
  }))
  
  configChartInstance.setOption({
    tooltip: {
      trigger: 'item',
      formatter: '{b}: {c} ({d}%)'
    },
    legend: {
      show: false
    },
    series: [
      {
        name: '配置',
        type: 'pie',
        radius: ['20%', '65%'],
        center: ['50%', '45%'],
        avoidLabelOverlap: true,
        itemStyle: {
          borderRadius: 8,
          borderColor: '#fff',
          borderWidth: 2
        },
        label: {
          show: true,
          position: 'outside',
          formatter: '{b}'
        },
        labelLine: {
          show: true,
          length: 10,
          length2: 10
        },
        data: coloredData
      }
    ]
  })
}

// 获取统计数据
async function loadStatistics() {
  try {
    const [brandRes, modelRes, configRes] = await Promise.all([
      getBrandStatistics(),
      getModelStatistics(),
      getConfigStatistics()
    ])
    
    if (brandRes.code === 200) {
      initBrandChart(brandRes.data)
    }
    if (modelRes.code === 200) {
      initModelChart(modelRes.data)
    }
    if (configRes.code === 200) {
      initConfigChart(configRes.data)
    }
  } catch (error) {
    console.error('加载统计数据失败:', error)
  }
}

// 窗口大小改变时重新调整图表大小
function handleResize() {
  brandChartInstance?.resize()
  modelChartInstance?.resize()
  configChartInstance?.resize()
}

onMounted(() => {
  loadStatistics()
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  brandChartInstance?.dispose()
  modelChartInstance?.dispose()
  configChartInstance?.dispose()
})
</script>

<style lang="scss" scoped>
.panel-group {
  margin-bottom: 20px;

  .card-panel-col {
    margin-bottom: 20px;
  }

  .card-panel {
    height: 140px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
    padding: 0 20px;
    cursor: pointer;
    transition: all 0.3s;

    &:hover {
      box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.15);
      transform: translateY(-2px);
    }

    .card-panel-icon-wrapper {
      width: 60px;
      height: 60px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-right: 16px;

      &.icon-total {
        background: rgba(64, 158, 255, 0.1);
        color: #409eff;
      }

      &.icon-online {
        background: rgba(103, 194, 58, 0.1);
        color: #67c23a;
      }

      &.icon-offline {
        background: rgba(245, 108, 108, 0.1);
        color: #f56c6c;
      }

      .card-panel-icon {
        font-size: 32px;
      }
    }

    .card-panel-description {
      flex: 1;

      .card-panel-text {
        font-size: 14px;
        color: #909399;
        margin-bottom: 8px;
      }

      .card-panel-num {
        font-size: 28px;
        font-weight: bold;
        color: #303133;
        margin-bottom: 4px;
      }

      .card-panel-trend {
        font-size: 12px;
        display: flex;
        align-items: center;
        gap: 4px;

        &.up {
          color: #f56c6c;
        }

        &.down {
          color: #67c23a;
        }
      }
    }
  }
}

.chart-group {
  .chart-card {
    margin-bottom: 20px;

    .chart-header {
      font-size: 16px;
      font-weight: bold;
      color: #303133;
    }

    .chart-container {
      height: 320px;
    }
  }
}
</style>
