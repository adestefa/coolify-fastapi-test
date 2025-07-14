from fastapi import FastAPI
from datetime import datetime
import os
import platform

app = FastAPI(title="Stage Server Test", version="1.0.0")

@app.get("/")
async def root():
    return {
        "message": "Hello Stage Server! 🚀",
        "status": "operational",
        "timestamp": datetime.now().isoformat(),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "server": {
            "platform": platform.system(),
            "python_version": platform.python_version(),
            "hostname": platform.node()
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "stage-test-app",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/info")
async def info():
    return {
        "app_name": "Stage Server Test Application",
        "version": "1.0.0",
        "description": "Simple FastAPI test application for Coolify deployment validation",
        "endpoints": [
            {"path": "/", "method": "GET", "description": "Root endpoint with server info"},
            {"path": "/health", "method": "GET", "description": "Health check endpoint"},
            {"path": "/info", "method": "GET", "description": "Application information"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6502)