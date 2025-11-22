from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from app.metrics_collector import MetricsCollector

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

@app.get("/metrics/prometheus", response_class=PlainTextResponse)
async def metrics_prometheus():
    collector = MetricsCollector()
    metrics_data = collector.get_all_metrics()
    
    prometheus_metrics = []
    
    cpu_percent = metrics_data["cpu"].get("Percentage", 0)
    prometheus_metrics.append(f"cpu_usage_percent {cpu_percent}")
    
    memory = metrics_data["memory"]
    prometheus_metrics.append(f"memory_total_gb {memory.get('Total', 0)}")
    prometheus_metrics.append(f"memory_free_gb {memory.get('Free', 0)}")
    prometheus_metrics.append(f"memory_used_gb {memory.get('Used', 0)}")
    prometheus_metrics.append(f"memory_usage_percent {memory.get('Percentage', 0)}")
    
    disk = metrics_data["disk"]
    prometheus_metrics.append(f"disk_total_gb {disk.get('Total', 0)}")
    prometheus_metrics.append(f"disk_free_gb {disk.get('Free', 0)}")
    prometheus_metrics.append(f"disk_used_gb {disk.get('Used', 0)}")
    prometheus_metrics.append(f"disk_usage_percent {disk.get('Percentage', 0)}")
    
    return "\n".join(prometheus_metrics)