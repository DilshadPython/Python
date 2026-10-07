"""
=============================================================================
KUBERNETES BEGINNER TUTORIALS: DEPLOYMENTS, SERVICES, CONFIGMAPS & PROBES
=============================================================================
File: cloud_app/tutorials/k8s_basics.py

Provides standalone Python implementations & Kubernetes manifest simulators for:
Tutorial 1: Kubernetes Pods & Declarative Deployment Specs
Tutorial 2: Kubernetes Services (ClusterIP/LoadBalancer) & Ingress Rules
Tutorial 3: ConfigMaps, Secrets & Liveness/Readiness Health Probes

PEP 8 Compliant with full type annotations.
"""

from typing import Dict, Any, List, Optional


class K8sDeploymentSimulator:
    """Simulates Kubernetes Deployment object creation and replica reconciliation.

    Teaches learners how K8s reconciles desired replica state against active Pod instances.
    """

    def __init__(self, name: str = "web-deployment", replicas: int = 3):
        # Deployment metadata and target replica count declared in deployment.yaml
        self.name = name
        self.replicas = replicas
        self.image = "nginx:1.25-alpine"
        self.labels = {"app": "web-api", "tier": "frontend"}
        self.container_port = 80

    def set_container(self, image: str, port: int) -> None:
        # Sets container image tag and target port inside Pod spec
        self.image = image
        self.container_port = port

    def reconcile(self) -> Dict[str, Any]:
        """Simulates K8s control loop creating pods matching desired replicas."""
        pods = []
        for i in range(1, self.replicas + 1):
            # CNI Network plugin assigns flat Pod IP address (10.244.x.x)
            pods.append(
                {
                    "pod_name": f"{self.name}-{hash(self.name) % 10000:04d}-pod{i}",
                    "status": "Running",
                    "ready": "1/1",
                    "restarts": 0,
                    "ip": f"10.244.1.{10 + i}",
                }
            )

        return {
            "kind": "Deployment",
            "metadata": {"name": self.name, "namespace": "default"},
            "spec": {
                "replicas": self.replicas,
                "selector": {"matchLabels": self.labels},
            },
            "status": {
                "desired_replicas": self.replicas,
                "available_replicas": self.replicas,
                "ready_replicas": self.replicas,
                "pods": pods,
            },
        }


class K8sServiceSimulator:
    """Simulates K8s Service load balancer for routing traffic to Pods.

    Demonstrates virtual ClusterIP / LoadBalancer endpoint mapping to dynamic Pod IPs.
    """

    def __init__(self, name: str = "web-service", service_type: str = "ClusterIP"):
        self.name = name
        self.service_type = service_type  # Service Types: ClusterIP (Internal), NodePort, or LoadBalancer
        self.selector = {"app": "web-api"}
        self.port = 80
        self.target_port = 8000

    def set_ports(self, port: int, target_port: int) -> None:
        # Port mapping: 'port' is exposed on Service, 'target_port' is container app port
        self.port = port
        self.target_port = target_port

    def get_routing_table(self, pods_list: List[Dict[str, str]]) -> Dict[str, Any]:
        """Simulates kube-proxy endpoint creation mapping Service to Pod IPs."""
        endpoints = [p["ip"] + f":{self.target_port}" for p in pods_list if "ip" in p]

        return {
            "kind": "Service",
            "name": self.name,
            "type": self.service_type,
            "cluster_ip": "10.96.142.88",
            "ports": [{"port": self.port, "targetPort": self.target_port}],
            "selector": self.selector,
            "endpoints": endpoints,
        }


class K8sProbeSimulator:
    """Simulates Liveness and Readiness Health Probes for container resiliency.

    Teaches self-healing: Liveness restarts unresponsive pods, Readiness controls traffic routing.
    """

    def __init__(self, path: str = "/healthz", initial_delay: int = 5):
        self.path = path
        self.initial_delay = initial_delay  # Grace period before Kubelet starts probing
        self.period_seconds = 10  # Probe execution frequency interval

    def evaluate_health(self, http_status: int) -> Dict[str, Any]:
        """Evaluates probe outcome based on application health HTTP status."""
        is_alive = 200 <= http_status < 400
        action = "Keep pod running" if is_alive else "Restart container via Kubelet"

        return {
            "probe_path": self.path,
            "http_status": http_status,
            "liveness_status": "SUCCESS" if is_alive else "FAILED",
            "kubelet_action": action,
            "initial_delay_seconds": self.initial_delay,
        }


# Quick tutorial runner functions for interactive studio execution
def run_tutorial_1_deployment() -> Dict[str, Any]:
    dep = K8sDeploymentSimulator("teachcloud-dep", replicas=3)
    dep.set_container("teachcloud/backend:v1.2", 5000)
    return dep.reconcile()


def run_tutorial_2_service() -> Dict[str, Any]:
    dep_res = run_tutorial_1_deployment()
    pods = dep_res["status"]["pods"]
    svc = K8sServiceSimulator("teachcloud-svc", "LoadBalancer")
    svc.set_ports(80, 5000)
    return svc.get_routing_table(pods)


def run_tutorial_3_probes() -> Dict[str, Any]:
    probe = K8sProbeSimulator("/healthz", initial_delay=10)
    healthy = probe.evaluate_health(200)
    unhealthy = probe.evaluate_health(500)
    return {"healthy_probe": healthy, "unhealthy_probe": unhealthy}


# Quick tutorial runner functions
def run_tutorial_1_deployment() -> Dict[str, Any]:
    dep = K8sDeploymentSimulator("teachcloud-backend", replicas=3)
    dep.set_container("teachcloud/backend:v1.2", 5000)
    return dep.reconcile()


def run_tutorial_2_service() -> Dict[str, Any]:
    dep = K8sDeploymentSimulator("teachcloud-backend", replicas=3)
    deployment_state = dep.reconcile()
    pods = deployment_state["status"]["pods"]

    svc = K8sServiceSimulator("teachcloud-svc", service_type="LoadBalancer")
    svc.set_ports(80, 5000)
    return svc.get_routing_table(pods)


def run_tutorial_3_probes() -> Dict[str, Any]:
    probe = K8sProbeSimulator("/api/v1/healthz", initial_delay=10)
    healthy = probe.evaluate_health(200)
    unhealthy = probe.evaluate_health(500)
    return {"healthy_probe": healthy, "unhealthy_probe": unhealthy}


if __name__ == "__main__":
    print("=== K8s Tutorial 1 ===", run_tutorial_1_deployment())
    print("=== K8s Tutorial 2 ===", run_tutorial_2_service())
    print("=== K8s Tutorial 3 ===", run_tutorial_3_probes())
