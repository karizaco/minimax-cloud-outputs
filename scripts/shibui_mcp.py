#!/usr/bin/env python3
"""Shibui MCP client for the cloud cron.

Calls the shibui-finance MCP server over streamable-HTTP
(https://mcp.shibui.finance/mcp) using the stock_data_query tool.

Per the server contract, get_database_schema and get_query_patterns must be
called (in that order) before stock_data_query in a fresh session.
"""
import json
import subprocess
import sys

ENDPOINT = "https://mcp.shibui.finance/mcp"


def _rpc(payload: dict, timeout: int = 180) -> dict:
    proc = subprocess.run(
        ["curl", "-sL", "-X", "POST", ENDPOINT,
         "-H", "Content-Type: application/json",
         "-H", "Accept: application/json, text/event-stream",
         "--data", json.dumps(payload)],
        capture_output=True, text=True, timeout=timeout,
    )
    for line in proc.stdout.splitlines():
        if line.startswith("data: "):
            return json.loads(line[6:])
    return {"error": {"message": f"no data line in {len(proc.stdout)}B response",
                      "raw": proc.stdout[:300], "stderr": proc.stderr[:300]}}


def _tool(name: str, args: dict, id_: int, timeout: int = 180):
    r = _rpc({"jsonrpc": "2.0", "id": id_, "method": "tools/call",
              "params": {"name": name, "arguments": args}}, timeout=timeout)
    if "error" in r:
        print(f"MCP ERROR [{name}]: {r['error']}", file=sys.stderr)
        return None
    content = r.get("result", {}).get("content", [{}])
    text = content[0].get("text", "") if content else ""
    return text


def bootstrap():
    """Call get_database_schema then get_query_patterns (required order)."""
    s = _tool("get_database_schema", {}, 1)
    p = _tool("get_query_patterns", {}, 2)
    print(f"schema: {'ok' if s else 'FAIL'} ({len(s) if s else 0} chars); "
          f"patterns: {'ok' if p else 'FAIL'} ({len(p) if p else 0} chars)",
          file=sys.stderr)
    return s is not None and p is not None


def query(sql: str, prompt: str, id_: int = 10, timeout: int = 180) -> list:
    text = _tool("stock_data_query", {"user_prompt": prompt, "query": sql}, id_, timeout)
    if text is None:
        return []
    text = text.strip()
    if not text:
        return []
    try:
        rows = json.loads(text)
    except json.JSONDecodeError:
        print(f"NON-JSON RESPONSE: {text[:400]}", file=sys.stderr)
        return []
    return rows if isinstance(rows, list) else [rows]


if __name__ == "__main__":
    if bootstrap():
        print("bootstrap ok")
