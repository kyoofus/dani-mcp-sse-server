import asyncio
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

async def run():
    server_params = StdioServerParameters(
        command="mcp-proxy",
        args=["http://127.0.0.1:8000/mcp"]  
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print("Available Tools:", tools)
            print("-" * 3)
            # Call a tool
            # operation_id = "get_user_info"을 사용하여 호출 
            result = await session.call_tool("get_user_info", arguments={"user_id": "apple"})
            print("Tool Result:", result)

def main():
    asyncio.run(run())

if __name__ == "__main__":
    main()
    
