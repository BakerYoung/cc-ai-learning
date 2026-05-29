import asyncio
import sys
from pathlib import Path

# 复用 MCPToolCaller
sys.path.insert(0, str(Path(__file__).parent.parent / "demo"))
from client_demo import MCPToolCaller


async def main():
    caller = MCPToolCaller("python3", ["notes_server.py"])
    await caller.connect()
    print("✅ 已连接到备忘录 Server\n")

    # 添加几条备忘录
    r = await caller.call_tool("add_note", {
        "title": "买水果",
        "content": "苹果、香蕉、橙子各一斤",
        "tags": "生活,购物",
    })
    print(r)

    r = await caller.call_tool("add_note", {
        "title": "周五开会",
        "content": "下午3点讨论Q2规划，提前准备PPT",
        "tags": "工作,会议",
    })
    print(r)

    # 列出所有备忘录
    r = await caller.call_tool("list_notes", {})
    print(r)

    # 按标签筛选
    r = await caller.call_tool("list_notes", {"tag": "工作"})
    print(r)

    # 搜索
    r = await caller.call_tool("search_notes", {"keyword": "水果"})
    print(r)

    await caller.close()

if __name__ == "__main__":
    asyncio.run(main())