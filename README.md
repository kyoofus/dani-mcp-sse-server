# dani-mcp-sse MCP server

FastAPI-MCP는FastAPI 엔드포인트를 MCP(Model Context Protocol) 도구로 자동 노출하기 위한 구성이 필요 없는 도구입니다.   FastAPI를 MCP 서버로 사용하는 방법을 설명합니다. 


FastAPI MCP  서버 테스트용 프로젝트 구조는 다음과 같습니다. 
```bash 
.
├─ README.md
├─ pyproject.toml
└─ src
   └─ dani_mcp_sse_server
       ├─ __init__.py
       └─ server.py
```


## 1. 설치 
FastAPI를 MCP Server로 사용하기 위해서는 클라이언트에서 mcp-proxy를 사용해야 합니다. 
```bash
# fastapi-mcp 설치 
uv add fastapi-mcp
# mcp-proxy 설치 
# Option 1: With uv (recommended)
uv tool install mcp-proxy
```



## 2. cluade_desktop_config.json
claude_desktop_config.json에 다음을 추가합니다.
```json
{
  "mcpServers": {
    "my-api-mcp-proxy": {
        "command": "mcp-proxy",
        "args": ["http://127.0.0.1:8000/mcp"]
    }
  }
}
```


## 3. Server 실행 
uvicorn을 사용하여 server를 따로 실행해야 합니다.
pyproject.toml에 scripts를 등록합니다. 
```toml
[project.scripts]
dani-mcp-sse-server = "dani_mcp_sse_server:main"
```
다음을 실행합니다. 
```bash
uv run dani-mcp-sse-server
```

# 4. 참고 
* [mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) 
* [Connecting a client to the MCP server](https://github.com/tadata-org/fastapi_mcp/blob/main/docs/02_connecting_to_the_mcp_server.md)
* [Tool Naming](https://github.com/tadata-org/fastapi_mcp/blob/main/docs/01_tool_naming.md)