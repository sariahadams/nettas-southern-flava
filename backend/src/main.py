from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import Dict


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:3000"],  # TODO: Add frontend url -- get from a config?
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def ping() -> Dict[str, str]:
    """
    Endpoint for health checks
    """
    return {"ping": "pong"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # TODO: Get host and port from config?
