<template>
  <div class="app-container">
    <!-- 搜索区域 -->
    <el-form :model="queryParams" ref="queryRef" :inline="true" v-show="showSearch">
      <el-form-item label="关键词" prop="keyword">
        <el-input
          v-model="queryParams.keyword"
          placeholder="输入VIN码等信息"
          clearable
          style="width: 200px"
          @keyup.enter="handleQuery"
        />
      </el-form-item>
      <el-form-item label="品牌" prop="brand">
        <el-select v-model="queryParams.brand" placeholder="请选择" clearable style="width: 200px">
          <el-option
            v-for="item in brandOptions"
            :key="item"
            :label="item"
            :value="item"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="状态" prop="status">
        <el-select v-model="queryParams.status" placeholder="请选择" clearable style="width: 200px">
          <el-option
            v-for="item in statusOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="Search" @click="handleQuery">搜索</el-button>
        <el-button icon="Refresh" @click="resetQuery">重置</el-button>
      </el-form-item>
    </el-form>

    <!-- 操作按钮区域 -->
    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button
          type="primary"
          plain
          icon="Plus"
          @click="handleImport"
        >批量导入</el-button>
      </el-col>
      <right-toolbar v-model:showSearch="showSearch" @queryTable="getList"></right-toolbar>
    </el-row>

    <!-- 表格区域 -->
    <el-table v-loading="loading" :data="vehicleList" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55" align="center" />
      <el-table-column label="序号" type="index" width="80" align="center" />
      <el-table-column label="VIN码" align="center" prop="vin" :show-overflow-tooltip="true" />
      <el-table-column label="品牌" align="center" prop="brand" width="120" />
      <el-table-column label="车型" align="center" prop="model" width="150" />
      <el-table-column label="配置" align="center" prop="config" width="120" />
      <el-table-column label="状态" align="center" prop="status" width="100">
        <template #default="scope">
          <el-tag :type="getStatusType(scope.row.status)">
            {{ getStatusLabel(scope.row.status) }}
          </el-tag>
        </template>
      </el-table-column>
    </el-table>

    <!-- 分页区域 -->
    <pagination
      v-show="total > 0"
      :total="total"
      v-model:page="queryParams.pageNum"
      v-model:limit="queryParams.pageSize"
      @pagination="getList"
    />
  </div>
</template>

<script setup name="Vehicle">
import { listVehicle } from "@/api/system/vehicle";

const { proxy } = getCurrentInstance();

const vehicleList = ref([]);
const loading = ref(true);
const showSearch = ref(true);
const total = ref(0);
const ids = ref([]);

// 品牌选项（预定义）
const brandOptions = ['吉利', '零跑'];

// 状态选项
const statusOptions = [
  { label: '在线', value: 'online', tagType: 'success' },
  { label: '离线', value: 'offline', tagType: 'danger' },
  { label: '未知', value: 'unknown', tagType: 'info' }
];

const data = reactive({
  queryParams: {
    pageNum: 1,
    pageSize: 10,
    keyword: undefined,
    brand: undefined,
    status: undefined
  }
});

const { queryParams } = toRefs(data);

/** 查询车辆列表 */
function getList() {
  loading.value = true;
  listVehicle(queryParams.value).then(res => {
    vehicleList.value = res.rows;
    total.value = res.total;
    loading.value = false;
  });
}

/** 搜索按钮操作 */
function handleQuery() {
  queryParams.value.pageNum = 1;
  getList();
}

/** 重置按钮操作 */
function resetQuery() {
  proxy.resetForm("queryRef");
  handleQuery();
}

/** 多选框选中数据 */
function handleSelectionChange(selection) {
  ids.value = selection.map(item => item.vehicleId);
}

/** 批量导入按钮操作 */
function handleImport() {
  console.log("todo");
}

/** 获取状态标签类型 */
function getStatusType(status) {
  const option = statusOptions.find(item => item.value === status);
  return option ? option.tagType : 'info';
}

/** 获取状态标签文本 */
function getStatusLabel(status) {
  const option = statusOptions.find(item => item.value === status);
  return option ? option.label : status;
}

getList();
</script>
