# 金融产品查询工具参考文档

## 1. query_product_by_prompt — 产品查询

根据提示词查询股票、公募基金等产品列表。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| prompt | string | 是 | 查询短语，例如"名字带健康的股票"、"持有农业银行的基金"。不能带空格，多关键词需分别请求 |
| type | string | 是 | 查询类别：stock(A股)、fund(公募基金)、HK_stock(港股)、US_stock(美股)、NEEQ(新三板) |

**示例：**
```json
{"tool_name": "query_product_by_prompt", "params": {"prompt": "白酒场外基金", "type": "fund"}}
```

---

## 2. search_stock_base — 股票基础信息查询

根据股票代码查询股票基本信息和日行情。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| codes | string | 是 | 股票代码，格式"xxxx.xx"，多个用英文逗号分隔，如"600519.SH,1810.HK" |

**示例：**
```json
{"tool_name": "search_stock_base", "params": {"codes": "600519.SH"}}
```

---

## 3. search_base_fund — 公募基金基础信息查询

查询指定基金代码的公募基金基本信息。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |

**示例：**
```json
{"tool_name": "search_base_fund", "params": {"fundcode": "000001"}}
```

---

## 4. search_fund_stock_portfolio — 公募基金股票持仓查询

查询指定基金代码的最新前十大重仓股票。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |

**示例：**
```json
{"tool_name": "search_fund_stock_portfolio", "params": {"fundcode": "000001"}}
```

---

## 5. search_fund_history_stock_portfolio — 公募基金历史股票持仓查询

查询指定基金历期的前十大重仓股票信息。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |

**示例：**
```json
{"tool_name": "search_fund_history_stock_portfolio", "params": {"fundcode": "000001"}}
```

---

## 6. search_fund_benchmark — 公募基金业绩基准查询

查询指定基金代码对应的业绩比较基准。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |

**示例：**
```json
{"tool_name": "search_fund_benchmark", "params": {"fundcode": "000001"}}
```

---

## 7. search_fund_bond_portfolio — 公募基金债券持仓查询

查询指定基金代码最新一期的债券持仓。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |

**示例：**
```json
{"tool_name": "search_fund_bond_portfolio", "params": {"fundcode": "000001"}}
```

---

## 8. search_fund_history_bond_portfolio — 公募基金历史债券持仓查询

查询指定基金历史所有报告期的债券持仓。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |

**示例：**
```json
{"tool_name": "search_fund_history_bond_portfolio", "params": {"fundcode": "000001"}}
```

---

## 9. search_currency_net_history — 货币基金历史净值查询

根据基金代码查询货币基金历史净值（仅支持货币基金）。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码，仅支持货币基金 |
| net_start_date | string | 是 | 净值开始日期，格式 Ymd，如 20250101 |
| net_end_date | string | 是 | 净值结束日期，格式 Ymd，如 20250131 |

**示例：**
```json
{"tool_name": "search_currency_net_history", "params": {"fundcode": "000009", "net_start_date": "20250101", "net_end_date": "20250131"}}
```

---

## 10. search_fund_net_history — 公募基金历史净值查询

根据基金代码查询公募基金（不含货币基金）历史净值。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |
| net_start_date | string | 是 | 净值开始日期，格式 Ymd，如 20250101 |
| net_end_date | string | 是 | 净值结束日期，格式 Ymd，如 20250131 |

**示例：**
```json
{"tool_name": "search_fund_net_history", "params": {"fundcode": "000001", "net_start_date": "20250101", "net_end_date": "20250131"}}
```

---

## 11. search_fund_dividend — 公募基金分红查询

根据基金代码查询公募基金分红信息。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |

**示例：**
```json
{"tool_name": "search_fund_dividend", "params": {"fundcode": "000001"}}
```

---

## 12. search_fund_notice_file — 公募基金公告查询

根据基金代码查询公募基金公告信息。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |

**示例：**
```json
{"tool_name": "search_fund_notice_file", "params": {"fundcode": "000001"}}
```

---

## 13. search_fund_history_manager — 公募基金历任基金经理查询

根据基金代码查询公募基金历任基金经理信息。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |

**示例：**
```json
{"tool_name": "search_fund_history_manager", "params": {"fundcode": "000001"}}
```

---

## 14. search_fund_interval_return — 公募基金区间收益查询

根据基金代码查询公募基金区间收益指标和业绩表现。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |

**示例：**
```json
{"tool_name": "search_fund_interval_return", "params": {"fundcode": "000001"}}
```

---

## 15. search_fund_invest_advisor — 公募基金管理人信息查询

根据基金管理人代码或名称查询公募基金管理人信息。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| value | string | 是 | 基金管理人代码或名称，优先通过代码查询 |

**示例：**
```json
{"tool_name": "search_fund_invest_advisor", "params": {"value": "华夏基金"}}
```

---

## 16. search_fund_trustee — 公募基金托管人信息查询

根据基金托管人代码或名称查询公募基金托管人信息。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| value | string | 是 | 基金托管人代码或名称，优先通过代码查询 |

**示例：**
```json
{"tool_name": "search_fund_trustee", "params": {"value": "工商银行"}}
```

---

## 17. search_fund_manager — 公募基金经理信息查询

根据基金经理代码或名称查询公募基金经理信息。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| value | string | 是 | 基金经理代码或名称，优先通过代码查询，仅支持单个代码 |

**示例：**
```json
{"tool_name": "search_fund_manager", "params": {"value": "张坤"}}
```

---

## 18. search_fund_rate — 公募基金费率查询

根据基金代码查询公募基金费率信息。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |

**示例：**
```json
{"tool_name": "search_fund_rate", "params": {"fundcode": "000001"}}
```

---

## 19. search_fund_trade_limit — 公募基金交易限额查询

根据基金代码查询公募基金交易限制信息。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fundcode | string | 是 | 基金代码 |

**示例：**
```json
{"tool_name": "search_fund_trade_limit", "params": {"fundcode": "000001"}}
```
