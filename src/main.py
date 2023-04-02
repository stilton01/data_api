from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/owl/v1/health")
async def get_health() -> dict:
    return {
    'Database': 'Status is up',
    'Application:': 'Status is up',
    'Networking': '0.99 ms latency'}

if __name__ == '__main__':
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)