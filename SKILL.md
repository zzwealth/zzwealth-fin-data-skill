---
name: zzwealth-fin-data
description: 基于中正达广基金金融数据库查询股票、公募基金等金融产品数据。当用户需要查询股票行情、公募基金净值、持仓、分红、费率、基金经理等金融数据时使用。
---

# 金融产品数据查询

提供 19 个金融数据查询工具，覆盖股票基础信息、公募基金基础信息、持仓、净值、分红、费率、基金经理等数据维度。

## 可用工具概览

| 工具名 | 功能 |
|---------|------|
| query_product_by_prompt | 根据提示词搜索股票/公募基金产品 |
| search_stock_base | 股票基础信息和日行情查询 |
| search_base_fund | 公募基金基础信息查询 |
| search_fund_stock_portfolio | 公募基金最新重仓股查询 |
| search_fund_history_stock_portfolio | 公募基金历史重仓股查询 |
| search_fund_benchmark | 公募基金业绩基准查询 |
| search_fund_bond_portfolio | 公募基金最新债券持仓查询 |
| search_fund_history_bond_portfolio | 公募基金历史债券持仓查询 |
| search_currency_net_history | 货币基金历史净值查询 |
| search_fund_net_history | 公募基金历史净值查询 |
| search_fund_dividend | 公募基金分红信息查询 |
| search_fund_notice_file | 公募基金公告查询 |
| search_fund_history_manager | 公募基金历任基金经理查询 |
| search_fund_interval_return | 公募基金区间收益/业绩表现查询 |
| search_fund_invest_advisor | 公募基金管理人信息查询 |
| search_fund_trustee | 公募基金托管人信息查询 |
| search_fund_manager | 公募基金经理信息查询 |
| search_fund_rate | 公募基金费率查询 |
| search_fund_trade_limit | 公募基金交易限额查询 |

## 使用方式

通过 `scripts/query.py` 调用远程 API：

```bash
# 列出所有可用工具
python scripts/query.py list

# 调用指定工具查询
python scripts/query.py query search_base_fund '{"fundcode": "000001"}'
python scripts/query.py query search_stock_base '{"codes": "600519.SH"}'
python scripts/query.py query search_fund_net_history '{"fundcode": "000001", "net_start_date": "20250101", "net_end_date": "20250131"}'
```

## 详细参数文档

每个工具的完整参数定义和调用示例，参见 [references/tools-reference.md](references/tools-reference.md)。

## 提供方

由 **中正达广基金** 提供数据服务。
