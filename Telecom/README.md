# Telcom - 中国电信 话费、通话、流量 套餐用量监控

## 概述
该项目旨在监控中国电信的用户话费、通话和流量使用情况。用户可以通过该工具获取实时的套餐用量信息。
这是一个初版，根据https://github.com/Cp0204/ChinaTelecomMonitor 而来


## 配置

- `options`: 其他选项，如 `WHITELIST_NUM`，示例值为 `18912345678,13312345678`。
- `schema`: 配置的模式，定义了 `WHITELIST_NUM` 的类型。

## 接口
以下是可用的接口及其功能其中127.0.0.1改为你的Home Assistant IP：

1. **登录**
   - URL: `http://127.0.0.1:10000/login`
   - 方法: POST/GET
   - 描述: 登录并返回用户信息，token长期有效，用于后续请求。

2. **查询主要信息**
   - URL: `http://127.0.0.1:10000/qryImportantData`
   - 方法: POST/GET
   - 描述: 返回主要信息，包括总用量、话费、通话、流量等。

3. **流量包明细**
   - URL: `http://127.0.0.1:10000/userFluxPackage`
   - 方法: POST/GET
   - 描述: 返回流量包的详细信息。

4. **共享套餐用量**
   - URL: `http://127.0.0.1:10000/qryShareUsage`
   - 方法: POST/GET
   - 描述: 返回共享套餐各号码的用量。

5. **简化数据接口**
   - URL: `http://127.0.0.1:10000/summary`
   - 方法: POST/GET
   - 描述: `/qryImportantData` 的数据简化接口，返回格式如下：
   ```json
   {
     "phonenum": "18912345678",
     "balance": 0,
     "voiceUsage": 39,
     "voiceTotal": 2250,
     "flowUse": 7366923,
     "flowTotal": 7366923,
     "flowOver": 222222,
     "commonUse": 7273962,
     "commonTotal": 25550446,
     "commonOver": 222222,
     "specialUse": 92961,
     "specialTotal": 215265280,
     "createTime": "2024-05-12 14:13:28",
     "flowItems": [
       {
         "name": "国内通用流量(达量降速)",
         "use": 10241024,
         "balance": 0,
         "total": 10241024
       },
       {
         "name": "国内通用流量(非畅享)",
         "use": 1,
         "balance": 10241023,
         "total": 10241024
       },
       {
         "name": "专用流量",
         "use": 1,
         "balance": 10241023,
         "total": 10241024
       }
     ]
   }
   ```

## 使用示例
- GET 请求示例：
   ```bash
   http://127.0.0.1:10000/summary?phonenum=18912345678&password=123456
   ```

- POST 请求示例：
   ```bash
   curl --request POST \
     --url http://127.0.0.1:10000/summary \
     --header 'Content-Type: application/json' \
     --data '{"phonenum": "18912345678","password": "123456"}'
   ```

## 注意事项
登录成功后，账号敏感信息将记录在 `/data/login_info.json` 文件中。程序请求数据时将优先使用记录的 token，以避免重复登录。

## ☕ 赞助支持

如果您觉得我花费大量时间维护这个库对您有帮助，欢迎请我喝杯奶茶，您的支持将是我持续改进的动力！

<div style="display: flex; justify-content: space-between;">
  <img src="https://gitee.com/desmond_GT/hassio-addons/raw/main/1_readme/Ali_Pay.jpg" height="350px" />
  <img src="https://gitee.com/desmond_GT/hassio-addons/raw/main/1_readme/WeChat_Pay.jpg" height="350px" />
</div> 💖

感谢您的支持与鼓励！


