"""
=============================================================================
DOCKER BEGINNER TUTORIALS: CONTAINERS, MULTI-STAGE BUILDS & DOCKER COMPOSE
=============================================================================
File: cloud_app/tutorials/docker_basics.py

Provides standalone, beginner-friendly Python implementations & simulators for:
Tutorial 1: Single Container Setup & Dockerfile Validation
Tutorial 2: Multi-Stage Build Optimization Simulator
Tutorial 3: Docker Compose Multi-Container Networking

PEP 8 Compliant with full type annotations.
"""

from typing import Dict, Any, List


class DockerfileSimulator:
    """Simulator for Dockerfile validation and image build process.

    Teaches learners how Dockerfile directives translate into container image layers.
    """

    def __init__(self, base_image: str = "python:3.11-slim"):
        # FROM directive: Select minimal OS/language base image to reduce footprint
        self.base_image = base_image
        self.instructions: List[str] = [f"FROM {base_image}"]
        self.workdir = "/app"
        self.exposed_port = 8000
        self.env_vars: Dict[str, str] = {}

    def set_workdir(self, path: str) -> None:
        # WORKDIR directive: Sets working directory inside container filesystem
        self.workdir = path
        self.instructions.append(f"WORKDIR {path}")

    def add_env(self, key: str, value: str) -> None:
        # ENV directive: Injects runtime environment variables into container process
        self.env_vars[key] = value
        self.instructions.append(f"ENV {key}={value}")

    def expose(self, port: int) -> None:
        # EXPOSE directive: Documents network port expected to receive connections
        self.exposed_port = port
        self.instructions.append(f"EXPOSE {port}")

    def build_image(self) -> Dict[str, Any]:
        """Simulates building a Docker image layer by layer.

        Validates that required directives are present and calculates image layer count.
        """
        if not self.workdir:
            return {
                "success": False,
                "error": "WORKDIR must be specified before COPY or CMD",
            }

        # Calculate total image layers created by each directive
        layers_count = (
            len(self.instructions) + 2
        )  # Includes COPY app files + CMD entrypoint
        return {
            "success": True,
            "image_name": "teachcloud-app:latest",
            "base_image": self.base_image,
            "layers_count": layers_count,
            "exposed_port": self.exposed_port,
            "env_vars": self.env_vars,
            "instructions": self.instructions
            + ["COPY . /app", 'CMD ["python", "run_app.py"]'],
        }


class MultiStageBuildSimulator:
    """Simulates multi-stage Dockerfile build size optimization.

    Shows how separating compiler environments from slim runners drastically reduces image size.
    """

    def __init__(self, app_name: str = "flask-microservice"):
        self.app_name = app_name

    def simulate_single_stage(self) -> Dict[str, Any]:
        """Single stage build retains build dependencies, gcc compilers, and pip cache (Heavy ~900MB)."""
        return {
            "stage": "single-stage",
            "base_image": "python:3.11",
            "size_mb": 920.0,
            "build_tools_included": True,
            "security_vulnerabilities_estimated": 14,
        }

    def simulate_multi_stage(self) -> Dict[str, Any]:
        """Multi-stage build copies built artifacts to python:slim runner (Lean ~145MB)."""
        return {
            "stage": "multi-stage-distroless",
            "builder_image": "python:3.11",  # Stage 1: Build wheel packages & compile C extensions
            "runner_image": "python:3.11-slim",  # Stage 2: Copy only built site-packages into clean image
            "size_mb": 145.0,
            "build_tools_included": False,
            "size_reduction_pct": 84.2,
            "security_vulnerabilities_estimated": 2,
        }


class DockerComposeSimulator:
    """Simulates multi-container Docker Compose service orchestrations.

    Demonstrates bridge network creation, port mappings, and service dependencies.
    """

    def __init__(self, project_name: str = "cloud_stack"):
        self.project_name = project_name
        self.services: Dict[str, Dict[str, Any]] = {}

    def add_service(
        self, name: str, image: str, port_mapping: str, depends_on: List[str] = None
    ) -> None:
        # Defines a container service spec (e.g. API, Postgres DB, Redis Cache)
        self.services[name] = {
            "image": image,
            "ports": [port_mapping],  # Host:Container port mapping (e.g. 5000:5000)
            "depends_on": depends_on or [],  # Startup dependency ordering
            "status": "created",
        }

    def up(self) -> Dict[str, Any]:
        """Simulates 'docker compose up -d' command execution."""
        running_services = {}
        for s_name, s_spec in self.services.items():
            running_services[s_name] = {
                "container_id": f"cntr_{s_name}_01",
                "image": s_spec["image"],
                "ports": s_spec["ports"],
                "status": "running (healthy)",
            }

        return {
            "project": self.project_name,
            "status": "healthy",
            "active_containers": len(running_services),
            "services": running_services,
            "network": f"{self.project_name}_default (bridge)",  # Isolated inter-container DNS network
        }


# Quick demonstration functions with step-by-step comments for interactive execution
def run_tutorial_1_dockerfile() -> Dict[str, Any]:
    # Step 1: Initialize simulator with a slim base image
    sim = DockerfileSimulator("python:3.11-slim")
    # Step 2: Set application directory inside container
    sim.set_workdir("/usr/src/app")
    # Step 3: Inject environment variables
    sim.add_env("FLASK_ENV", "production")
    # Step 4: Expose application port 5000
    sim.expose(5000)
    # Step 5: Execute layer build simulation
    return sim.build_image()


def run_tutorial_2_multistage() -> Dict[str, Any]:
    # Compare single-stage monolithic image vs 80%+ smaller multi-stage production image
    ms = MultiStageBuildSimulator("api-service")
    single = ms.simulate_single_stage()
    multi = ms.simulate_multi_stage()
    return {"single_stage": single, "multi_stage": multi}


def run_tutorial_3_compose() -> Dict[str, Any]:
    # Orchestrate a complete multi-container microservice stack
    comp = DockerComposeSimulator("teachcloud_backend")
    # 1. Database service (PostgreSQL on port 5432)
    comp.add_service("db", "postgres:16-alpine", "5432:5432")
    # 2. In-memory cache service (Redis on port 6379)
    comp.add_service("cache", "redis:7-alpine", "6379:6379")
    # 3. Web API service depending on DB and Cache
    comp.add_service(
        "api", "teachcloud/api:v1", "5000:5000", depends_on=["db", "cache"]
    )
    # Start container cluster
    return comp.up()


if __name__ == "__main__":
    print("=== Docker Tutorial 1 ===", run_tutorial_1_dockerfile())
    print("=== Docker Tutorial 2 ===", run_tutorial_2_multistage())
    print("=== Docker Tutorial 3 ===", run_tutorial_3_compose())
