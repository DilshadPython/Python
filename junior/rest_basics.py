"""
REST API Basics Tutorial & Dispatcher Simulator
Teach Cloud - Cloud, DevOps, and Python Backend Development

This module provides a beginner-friendly interactive interface for learning
RESTful API architectures (GET, POST, PUT, DELETE), JSON payload handling,
and HTTP response status codes.
"""

from typing import Dict, List, Any, Optional, Tuple


class RESTStudioRunner:
    """
    In-memory REST API simulator for testing HTTP endpoints, JSON payloads,
    and status codes without needing external network servers.
    """

    def __init__(self):
        # In-memory item store representing database state
        self.items: Dict[int, Dict[str, Any]] = {
            1: {
                "id": 1,
                "name": "PostgreSQL Database Service",
                "category": "Database",
                "status": "active",
            },
            2: {
                "id": 2,
                "name": "Redis Cache Cluster",
                "category": "Cache",
                "status": "active",
            },
            3: {
                "id": 3,
                "name": "Nginx Ingress Gateway",
                "category": "Networking",
                "status": "active",
            },
        }
        self.next_id = 4

    def handle_request(
        self, method: str, path: str, body: Optional[Dict[str, Any]] = None
    ) -> Tuple[int, Dict[str, Any]]:
        """
        Dispatches incoming HTTP client requests based on method and URI path.
        Returns a tuple of (HTTP_STATUS_CODE, RESPONSE_JSON_DICT).
        """
        method = method.upper().strip()
        path = path.strip().rstrip("/")

        # 1. GET /api/v1/services -> List all items
        if method == "GET" and path == "/api/v1/services":
            return 200, {
                "status_code": 200,
                "message": "OK",
                "count": len(self.items),
                "data": list(self.items.values()),
            }

        # 2. GET /api/v1/services/<id> -> Get single item
        elif method == "GET" and path.startswith("/api/v1/services/"):
            try:
                item_id = int(path.split("/")[-1])
            except ValueError:
                return 400, {
                    "status_code": 400,
                    "error": "Bad Request: Invalid ID format.",
                }

            if item_id in self.items:
                return 200, {
                    "status_code": 200,
                    "message": "OK",
                    "data": self.items[item_id],
                }
            return 404, {
                "status_code": 404,
                "error": f"Resource with ID {item_id} not found.",
            }

        # 3. POST /api/v1/services -> Create new service item
        elif method == "POST" and path == "/api/v1/services":
            if not body or "name" not in body or "category" not in body:
                return 400, {
                    "status_code": 400,
                    "error": "Bad Request: Payload must include 'name' and 'category'.",
                }

            new_item = {
                "id": self.next_id,
                "name": str(body["name"]),
                "category": str(body["category"]),
                "status": str(body.get("status", "active")),
            }
            self.items[self.next_id] = new_item
            self.next_id += 1
            return 201, {
                "status_code": 201,
                "message": "Resource Created Successfully",
                "data": new_item,
            }

        # 4. PUT /api/v1/services/<id> -> Update service item
        elif method == "PUT" and path.startswith("/api/v1/services/"):
            try:
                item_id = int(path.split("/")[-1])
            except ValueError:
                return 400, {
                    "status_code": 400,
                    "error": "Bad Request: Invalid ID format.",
                }

            if item_id not in self.items:
                return 404, {
                    "status_code": 404,
                    "error": f"Resource with ID {item_id} not found.",
                }

            if not body:
                return 400, {
                    "status_code": 400,
                    "error": "Bad Request: JSON payload body required.",
                }

            item = self.items[item_id]
            item["name"] = body.get("name", item["name"])
            item["category"] = body.get("category", item["category"])
            item["status"] = body.get("status", item["status"])
            return 200, {
                "status_code": 200,
                "message": "Resource Updated Successfully",
                "data": item,
            }

        # 5. DELETE /api/v1/services/<id> -> Remove service item
        elif method == "DELETE" and path.startswith("/api/v1/services/"):
            try:
                item_id = int(path.split("/")[-1])
            except ValueError:
                return 400, {
                    "status_code": 400,
                    "error": "Bad Request: Invalid ID format.",
                }

            if item_id not in self.items:
                return 404, {
                    "status_code": 404,
                    "error": f"Resource with ID {item_id} not found.",
                }

            deleted_item = self.items.pop(item_id)
            return 200, {
                "status_code": 200,
                "message": "Resource Deleted Successfully",
                "deleted_id": item_id,
                "deleted_name": deleted_item["name"],
            }

        # Fallback 404
        return 404, {
            "status_code": 404,
            "error": f"Endpoint '{method} {path}' not found.",
        }


def run_rest_demo() -> Dict[str, Any]:
    """
    Demonstrates full REST API request cycle (GET, POST, PUT, DELETE).
    Returns structured results for tutorial verification.
    """
    api = RESTStudioRunner()

    # 1. GET ALL
    s1, r1 = api.handle_request("GET", "/api/v1/services")

    # 2. POST (Create)
    s2, r2 = api.handle_request(
        "POST",
        "/api/v1/services",
        {"name": "RabbitMQ Message Broker", "category": "Messaging"},
    )

    # 3. PUT (Update)
    created_id = r2["data"]["id"]
    s3, r3 = api.handle_request(
        "PUT", f"/api/v1/services/{created_id}", {"status": "degraded"}
    )

    # 4. DELETE
    s4, r4 = api.handle_request("DELETE", f"/api/v1/services/{created_id}")

    return {
        "get_all": (s1, r1),
        "post_create": (s2, r2),
        "put_update": (s3, r3),
        "delete_remove": (s4, r4),
    }


if __name__ == "__main__":
    demo = run_rest_demo()
    print("--- REST API DEMO COMPLETE ---")
    for key, (status, resp) in demo.items():
        print(f"[{key.upper()}] HTTP {status}: {resp}")
