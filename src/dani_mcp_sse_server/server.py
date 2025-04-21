from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()

# FastAPI-MCP는 FastAPI 경로의 operation_id MCP 도구 이름으로 사용합니다. 
# operation_id 지정하지 않으면 FastAPI가 자동으로 생성하지만 이는 이해하기 어려울 수 있습니다.

# # Auto-generated operation_id (something like "read_user_users__user_id__get")
# @app.get("/users/{user_id}")
# async def read_user(user_id: int):
#     return {"user_id": user_id}

# Explicit operation_id (tool will be named "get_user_info")
@app.get("/users/{user_id}", operation_id="get_user_info")
async def read_user(user_id: str):
    return {"user_id": user_id}


mcp = FastApiMCP(app)

# Mount the MCP server directly to your FastAPI app
mcp.mount()

