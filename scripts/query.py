#!/usr/bin/env python3
"""
金融产品数据查询脚本
通过 OneAgent 开放接口查询股票、公募基金等金融产品数据

依赖: requests (pip install requests)
"""

import json
import sys

import requests

BASE_URL = "https://oneagent.zhongzhengfund.com/api"


def list_tools():
    """列出所有可用工具"""
    url = f"{BASE_URL}/open/product/tools/"
    try:
        resp = requests.post(url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if not data.get("success"):
            print(f"错误: {data.get('message', '未知错误')}")
            sys.exit(1)

        tools = data["data"]
        print(f"共 {len(tools)} 个可用工具:\n")
        for t in tools:
            params_desc = ", ".join(
                f"{p['name']}({'必填' if p.get('required') else '可选'})"
                for p in t.get("parameters", [])
            )
            print(f"  {t['name']}")
            print(f"    {t.get('title', '')} - {t['description'][:80]}")
            print(f"    参数: {params_desc}")
            print()
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        sys.exit(1)


def query_tool(tool_name: str, params_json: str):
    """调用指定工具执行查询"""
    url = f"{BASE_URL}/open/product/query/"

    try:
        params = json.loads(params_json)
    except json.JSONDecodeError as e:
        print(f"参数 JSON 解析失败: {e}")
        sys.exit(1)

    payload = {"tool_name": tool_name, "params": params}
    try:
        resp = requests.post(url, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        if not data.get("success"):
            print(f"错误: {data.get('message', '未知错误')}")
            sys.exit(1)

        print(json.dumps(data["data"], ensure_ascii=False, indent=2))
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  python query.py list                          列出所有可用工具")
        print("  python query.py query <tool_name> <params>    调用工具查询")
        print()
        print("示例:")
        print('  python query.py query search_base_fund \'{"fundcode": "000001"}\'')
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        list_tools()
    elif command == "query":
        if len(sys.argv) < 4:
            print("用法: python query.py query <tool_name> <params_json>")
            sys.exit(1)
        query_tool(sys.argv[2], sys.argv[3])
    else:
        print(f"未知命令: {command}")
        print("可用命令: list, query")
        sys.exit(1)


if __name__ == "__main__":
    main()
