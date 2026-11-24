"""
=============================================================================
MONITORING & OBSERVABILITY TUTORIALS: PROMETHEUS, GRAFANA & HEALTH PROBES
=============================================================================
File: cloud_app/tutorials/monitoring_basics.py

Provides standalone Python implementations & Observability simulators for:
Tutorial 1: Prometheus Metrics Instrumentation (Counters, Gauges, Histograms)
Tutorial 2: Grafana Dashboard Panels & CloudWatch / Prometheus Alert Rules
Tutorial 3: Structured JSON Logging & Application Health Check Endpoint

PEP 8 Compliant with full type annotations.
"""

from typing import Dict, Any, List
import time


class PrometheusMetricsSimulator:
    """Simulates Prometheus metric scraping endpoint (/metrics).

    Teaches the Three Primary Metric Types: Counters (increment only), Gauges (up/down), and Histograms (latency distributions).
    """

    def __init__(self, service_name: str = "teachcloud_api"):
        self.service_name = service_name
        self.http_requests_total = 1420
        self.active_connections = 18
        self.request_duration_seconds = 0.045

    def increment_request(self, status: int = 200) -> None:
        # Counter Metric: Increments on every incoming HTTP request (never decreases)
        self.http_requests_total += 1

    def set_active_connections(self, count: int) -> None:
        # Gauge Metric: Fluctuates up and down representing current active connections
        self.active_connections = count

    def generate_metrics_text(self) -> str:
        """Generates standard Prometheus exposition format text output scraped by Prometheus server."""
        return (
            f"# HELP http_requests_total Total number of HTTP requests processed\n"
            f"# TYPE http_requests_total counter\n"
            f'http_requests_total{{service="{self.service_name}",code="200"}} {self.http_requests_total}\n\n'
            f"# HELP active_connections Current active HTTP client connections\n"
            f"# TYPE active_connections gauge\n"
            f'active_connections{{service="{self.service_name}"}} {self.active_connections}\n\n'
            f"# HELP request_duration_seconds HTTP request latency histogram\n"
            f"# TYPE request_duration_seconds histogram\n"
            f'request_duration_seconds_sum{{service="{self.service_name}"}} {round(self.http_requests_total * self.request_duration_seconds, 2)}\n'
            f'request_duration_seconds_count{{service="{self.service_name}"}} {self.http_requests_total}\n'
        )


class GrafanaAlertSimulator:
    """Simulates Grafana dashboard panel queries and alert rule conditions.

    Teaches automated alerting logic: Firing alerts when CPU or 5xx error thresholds breach SLAs.
    """

    def __init__(self, dashboard_title: str = "Cloud API Health Overview"):
        self.dashboard_title = dashboard_title
        self.alert_rules: List[Dict[str, Any]] = []

    def add_alert_rule(self, metric: str, condition: str, threshold: float) -> None:
        # Register alerting threshold rule (e.g. CPU > 85% or Error Rate > 2.5%)
        self.alert_rules.append(
            {
                "metric": metric,
                "condition": condition,
                "threshold": threshold,
                "state": "OK",
            }
        )

    def evaluate_alerts(
        self, current_cpu_pct: float, error_rate_pct: float
    ) -> Dict[str, Any]:
        """Evaluates alert threshold rules against live metric values."""
        fired_alerts = []
        for rule in self.alert_rules:
            if (
                rule["metric"] == "cpu_utilization"
                and current_cpu_pct > rule["threshold"]
            ):
                rule["state"] = "FIRING"
                fired_alerts.append(
                    f"CRITICAL: CPU ({current_cpu_pct}%) > {rule['threshold']}%"
                )
            elif rule["metric"] == "error_rate" and error_rate_pct > rule["threshold"]:
                rule["state"] = "FIRING"
                fired_alerts.append(
                    f"WARNING: HTTP 5xx Error Rate ({error_rate_pct}%) > {rule['threshold']}%"
                )
            else:
                rule["state"] = "OK"

        return {
            "dashboard": self.dashboard_title,
            "overall_status": "ALERTING" if fired_alerts else "HEALTHY",
            "active_alerts_count": len(fired_alerts),
            "alerts": fired_alerts or ["All metrics within normal thresholds."],
        }


class StructuredLoggingSimulator:
    """Simulates JSON structured log output and HTTP health probe responses.

    Teaches machine-readable JSON logging for central indexing (ELK/Loki) and health status endpoints.
    """

    def __init__(self, app_version: str = "v2.4.0"):
        self.app_version = app_version

    def log_event(
        self, level: str, message: str, extra: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """Creates structured JSON log entry formatted for central log aggregators."""
        log_entry = {
            "timestamp": "2026-09-04T19:35:00Z",
            "level": level.upper(),  # INFO, WARNING, ERROR, CRITICAL
            "service": "teachcloud-backend",
            "version": self.app_version,
            "message": message,
        }
        if extra:
            log_entry.update(
                extra
            )  # Inject custom key-value metadata (user_id, client_ip)
        return log_entry

    def health_check(self, db_ok: bool = True, redis_ok: bool = True) -> Dict[str, Any]:
        """Simulates GET /health status probe response used by Load Balancers and K8s Probes."""
        status_code = 200 if (db_ok and redis_ok) else 503
        return {
            "status_code": status_code,  # 200 OK or 503 Service Unavailable
            "status": "healthy" if status_code == 200 else "unhealthy",
            "version": self.app_version,
            "checks": {
                "database": "UP" if db_ok else "DOWN",
                "redis_cache": "UP" if redis_ok else "DOWN",
            },
        }


# Quick tutorial runner functions
def run_tutorial_1_prometheus() -> Dict[str, Any]:
    prom = PrometheusMetricsSimulator("teachcloud_api")
    prom.increment_request()
    prom.set_active_connections(24)
    return {"metrics_raw": prom.generate_metrics_text()}


def run_tutorial_2_grafana() -> Dict[str, Any]:
    graf = GrafanaAlertSimulator("Production Cluster Observability")
    graf.add_alert_rule("cpu_utilization", ">", 85.0)
    graf.add_alert_rule("error_rate", ">", 2.5)

    normal = graf.evaluate_alerts(current_cpu_pct=42.0, error_rate_pct=0.4)
    alerting = graf.evaluate_alerts(current_cpu_pct=91.5, error_rate_pct=3.8)
    return {"normal_state": normal, "alerting_state": alerting}


def run_tutorial_3_logging() -> Dict[str, Any]:
    slog = StructuredLoggingSimulator("v2.4.0")
    log_sample = slog.log_event(
        "INFO", "User login successful", {"user_id": 402, "ip": "192.168.1.10"}
    )
    health_sample = slog.health_check(db_ok=True, redis_ok=True)
    return {"structured_log": log_sample, "health_probe": health_sample}


if __name__ == "__main__":
    print("=== Monitoring Tutorial 1 ===", run_tutorial_1_prometheus())
    print("=== Monitoring Tutorial 2 ===", run_tutorial_2_grafana())
    print("=== Monitoring Tutorial 3 ===", run_tutorial_3_logging())
