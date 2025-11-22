import psutil
import datetime

class MetricsCollector():

    def get_cpu_usage(self):
        try:
            return(
                {
                    "Percentage":psutil.cpu_percent(interval=1),
                }
            )
        except Exception as e:
            return{"Error": str(e)}
    
    def get_ram_usage(self):
        try:
            ram_info = psutil.virtual_memory()
            return(
                {
                    "Total":round(ram_info.total / (1024**3), 2), 
                    "Free":round(ram_info.free / (1024**3), 2), 
                    "Used":round(ram_info.used / (1024**3), 2), 
                    "Percentage":ram_info.percent
                }
            )
        except Exception as e:
            return{"Error": str(e)}
    
    def get_disk_usage(self):
        try:
            disk_info = psutil.disk_usage('/')
            return(
                {
                    "Total":round(disk_info.total / (1024**3), 2), 
                    "Used":round(disk_info.used / (1024**3), 2), 
                    "Free":round(disk_info.free / (1024**3), 2), 
                    "Percentage":disk_info.percent
                }
            )
        except Exception as e:
            return{"Error": str(e)}
    def get_all_metrics(self):
        return(
            {
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "cpu":self.get_cpu_usage(),
                "memory":self.get_ram_usage(),
                "disk":self.get_disk_usage()
            }
        )