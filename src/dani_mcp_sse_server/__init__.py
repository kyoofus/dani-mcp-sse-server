from . import server
import uvicorn
import os


def main():
    """Main entry point for the package.
    메인 모듈로 직접 실행될 때 uvicorn 서버를 시작합니다.
    
    호스트는 모든 네트워크 인터페이스(0.0.0.0)에서 접속을 허용하며,
    포트 8000에서 실행됩니다.
    
    실행 방법: python main.py
    """
    uvicorn.run("dani_mcp_sse_server.server:app", host="0.0.0.0", port=8000)


# Optionally expose other important items at package level
__all__ = ['main', 'server']