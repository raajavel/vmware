import requests
from prometheus_client import start_http_server, Summary, Gauge
import prometheus_client as prom

prom.REGISTRY.unregister(prom.PROCESS_COLLECTOR)
prom.REGISTRY.unregister(prom.PLATFORM_COLLECTOR)
prom.REGISTRY.unregister(prom.GC_COLLECTOR)

endpoint_guage_status_1 = Gauge('endpoint_503_status', 'Monitor https://httpstat.us/503 status code')
endpoint_guage_time_1 = Gauge('endpoint_503_resp', 'Monitor https://httpstat.us/503  response time')

endpoint_guage_status_2 = Gauge('endpoint_200_status', 'Monitor https://httpstat.us/200 status code')
endpoint_guage_time_2 = Gauge('endpoint_200_resp', 'Monitor https://httpstat.us/200 response time')

def generate_metrics():
    """A dummy function that takes some time."""
    resp_1 = requests.get("https://httpstat.us/503")
    status_code_1 = resp_1.status_code
    resp_time_1 = resp_1.elapsed.total_seconds()

    resp_2 = requests.get("https://httpstat.us/200")
    status_code_2 = int(resp_2.status_code)
    resp_time_2 = resp_2.elapsed.total_seconds()
    
    endpoint_guage_status_1.set(status_code_1)
    endpoint_guage_time_1.set(resp_time_1)

    endpoint_guage_status_2.set(status_code_2)
    endpoint_guage_time_2.set(resp_time_2)

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        generate_metrics()
