# Fin Data Skill

查询股票、公募基金等金融产品数据的 Agent Skill，支持在 Claude Code、OpenClaw 等 AI 工具中安装使用。

## 功能

提供 19 个金融数据查询工具：

- **股票** — 基础信息、日行情
- **公募基金** — 基础信息、重仓股、债券持仓、净值、分红、公告、费率、交易限额
- **基金经理/管理人/托管人** — 详细信息查询
- **产品搜索** — 根据提示词智能检索股票和基金

## 安装

### OpenClaw

直接和 OpenClaw 对话：

> 帮我安装 https://github.com/zzwealth/zzwealth-fin-data-skill 这个 skill

### Claude Code

```bash
/install-github-skill https://github.com/zzwealth/zzwealth-fin-data-skill
```

### 手动安装

```bash
git clone https://github.com/zzwealth/zzwealth-fin-data-skill.git
```

克隆仓库后参照 `SKILL.md` 中的说明使用。

## 命令行使用

```bash
# 列出所有可用工具
python scripts/query.py list

# 查询基金基础信息
python scripts/query.py query search_base_fund '{"fundcode": "000001"}'

# 查询股票行情
python scripts/query.py query search_stock_base '{"codes": "600519.SH"}'

# 查询基金历史净值
python scripts/query.py query search_fund_net_history '{"fundcode": "000001", "net_start_date": "20250101", "net_end_date": "20250131"}'
```

## 工具列表

| 工具名 | 功能 |
|--------|------|
| query_product_by_prompt | 根据提示词搜索股票/公募基金 |
| search_stock_base | 股票基础信息和日行情 |
| search_base_fund | 公募基金基础信息 |
| search_fund_stock_portfolio | 公募基金最新重仓股 |
| search_fund_history_stock_portfolio | 公募基金历史重仓股 |
| search_fund_benchmark | 公募基金业绩基准 |
| search_fund_bond_portfolio | 公募基金最新债券持仓 |
| search_fund_history_bond_portfolio | 公募基金历史债券持仓 |
| search_currency_net_history | 货币基金历史净值 |
| search_fund_net_history | 公募基金历史净值 |
| search_fund_dividend | 公募基金分红信息 |
| search_fund_notice_file | 公募基金公告 |
| search_fund_history_manager | 公募基金历任基金经理 |
| search_fund_interval_return | 公募基金区间收益/业绩表现 |
| search_fund_invest_advisor | 公募基金管理人信息 |
| search_fund_trustee | 公募基金托管人信息 |
| search_fund_manager | 公募基金经理信息 |
| search_fund_rate | 公募基金费率 |
| search_fund_trade_limit | 公募基金交易限额 |

各工具的完整参数定义见 [references/tools-reference.md](references/tools-reference.md)。

## 依赖

- Python 3.8+
- requests (`pip install requests`)

## 提供方

由 **中正达广基金** 提供数据服务。