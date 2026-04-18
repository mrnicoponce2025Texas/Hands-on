import asyncio
from fastmcp import Client

async def main():
    async with Client("coursera_mcp.py") as client:
        tools = await client.list_tools()

        print(f"Connected to MCP server — {len(tools)} tools found:\n")
        for tool in tools:
            print(f"Tool: {tool.name}")
            print(f"  Description: {tool.description}")
            print(f"  Parameters:  {list(tool.inputSchema.get('properties', {}).keys())}")
            print()

if __name__ == "__main__":
    asyncio.run(main())
