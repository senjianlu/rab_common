# rab_common

## 依赖
*不依赖于任何模块。*

## 配置片段
```toml
# 外部模块
[external]
  [external.rab_common]
    [external.rab_common.switch]
      [external.rab_common.switch.base]
      # 基础服务启动控制
      [external.rab_common.switch.optional]
      # 可选服务启动控制
    [external.rab_common.config]
    # 环境: dev/test/pre/prod
    env = "dev"
    [external.rab_common.logger]
    # 日志级别
    level = "info"
    # 日志输出路径
    dir_path = "../logs"
    [external.rab_common.orm]
      [external.rab_common.orm.user]
      id = "test_id"
      name = "test_name"
      [external.rab_common.orm.database]
      # 暂时只支持 PostgreSQL 数据库
      host = "127.0.0.1"
      port = 5432
      username = "postgres"
      password = "postgres"
      database = "postgres"
    [external.rab_common.redis]
    host = "127.0.0.1"
    port = 6379
    password = "my_redis_password"
    database = 0
```