import time
from ping3 import ping
from prometheus_client import start_http_server, Gauge

IP_ADDRESSES = ["IP 1", "IP 2"]

PING_GAUGE = Gauge('ping_status', 'Status do ping do IP', ['ip'])

def ping_host(ip):
    """Retorna 1 se o IP estiver disponível e 0 caso contrário"""
    return int(ping(ip, timeout=1) is not None)

if __name__ == '__main__':
    start_http_server(3735)
    
    while True:
        for ip in IP_ADDRESSES:
            # Realiza o ping no IP e atualiza a métrica do Prometheus
            status = ping_host(ip)
            PING_GAUGE.labels(ip).set(status)
        
        # Aguarda 5 segundos
        time.sleep(5)
