from fastapi import FastAPI
from metrics_collector import MetricsCollector

app = FastAPI()

@app.get("/")
async def status():
    return {"status": "System Monitor is running"}

@app.get("/metrics")
async def metrics():
    collector = MetricsCollector()
    return collector.get_all_metrics()

@app.get("/health")
async def health():
    return {"status": "healthy"}