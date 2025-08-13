# 更新日志

## [v2.4.2] - 2025-08-13
 - 同步easytier官方版本


## [v2.2.4.1] - 2025-05-07
 - 支持自定义机器名

## [v2.2.2] - 2025-02-24

## 鸣谢：https://github.com/mrtian2016 帮我排错

### 新增
- 首次发布 EasyTier 插件
- 支持 ARM64 和 AMD64 架构
- 自动生成 config.yaml 文件
- 网络配置选项：
  - 实例名称 (instance_name)
  - 实例ID (instance_id)
  - RPC 门户 (rpc_portal)
  - 网络名称 (network_name)
  - 网络密钥 (network_secret)
  - URI
  - CIDR

### 变更
- 基础镜像更新至 easytier/easytier:v2.2.2
- 添加了用于 JSON 解析的 jq 包

### 修复
- 初始化脚本改进
- 配置文件处理优化
