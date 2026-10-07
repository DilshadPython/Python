"""
=============================================================================
TERRAFORM BEGINNER TUTORIALS: HCL SYNTAX, MODULES, STATE & PLAN SIMULATION
=============================================================================
File: cloud_app/tutorials/terraform_basics.py

Provides standalone Python implementations & Terraform HCL simulators for:
Tutorial 1: HCL Syntax, Provider Configuration & AWS VPC / Subnet Resources
Tutorial 2: Input Variables, Output Parameters & Modular Infrastructure Design
Tutorial 3: Remote State Lock & Terraform Plan / Apply Workflow

PEP 8 Compliant with full type annotations.
"""

from typing import Dict, Any, List


class HCLResourceSimulator:
    """Simulates HCL resource block definition and validation.

    Teaches declarative HCL syntax: resource "<TYPE>" "<NAME>" { ... }
    """

    def __init__(self, provider: str = "aws", region: str = "us-east-1"):
        self.provider = provider
        self.region = region
        self.resources: Dict[str, Dict[str, Any]] = {}

    def add_resource(
        self, resource_type: str, name: str, attributes: Dict[str, Any]
    ) -> None:
        # Construct resource key (e.g. aws_vpc.main or aws_subnet.public_1)
        key = f"{resource_type}.{name}"
        self.resources[key] = attributes

    def validate_config(self) -> Dict[str, Any]:
        """Simulates 'terraform validate' command checking HCL syntax correctness."""
        return {
            "valid": True,
            "provider": self.provider,
            "region": self.region,
            "resource_count": len(self.resources),
            "resources": self.resources,
            "diagnostics": [],  # Returns empty array when HCL syntax contains no errors
        }


class TerraformModuleSimulator:
    """Simulates Terraform variables, outputs, and reusable module blocks.

    Teaches DRY (Don't Repeat Yourself) infrastructure design using input variables and exported outputs.
    """

    def __init__(self, module_name: str = "vpc_module"):
        self.module_name = module_name
        self.variables: Dict[str, Any] = {}
        self.outputs: Dict[str, Any] = {}

    def set_input_variable(self, name: str, value: Any) -> None:
        # Define variable parameter passed into module (e.g. instance_class, environment)
        self.variables[name] = value

    def set_output(self, name: str, value: Any) -> None:
        # Export output attribute for consumption by other resources (e.g. DB Endpoint URI)
        self.outputs[name] = value

    def render_module(self) -> Dict[str, Any]:
        """Renders input variables and output values."""
        return {
            "module": self.module_name,
            "input_variables": self.variables,
            "outputs": self.outputs,
            "status": "configured",
        }


class TerraformPlanApplySimulator:
    """Simulates terraform plan and terraform apply state transformations.

    Teaches state locking (DynamoDB) and state file persistence (Amazon S3 bucket).
    """

    def __init__(self, state_backend: str = "s3"):
        self.state_backend = state_backend
        self.lock_table = "terraform-locks-dynamodb"  # DynamoDB table preventing concurrent apply execution

    def execute_plan(self, planned_changes: List[Dict[str, str]]) -> Dict[str, Any]:
        """Simulates 'terraform plan' execution (Dry run previewing infrastructure changes)."""
        to_add = sum(1 for c in planned_changes if c["action"] == "create")
        to_change = sum(1 for c in planned_changes if c["action"] == "update")
        to_destroy = sum(1 for c in planned_changes if c["action"] == "destroy")

        return {
            "backend": self.state_backend,
            "lock_acquired": True,
            "plan_summary": f"Plan: {to_add} to add, {to_change} to change, {to_destroy} to destroy.",
            "changes": planned_changes,
        }

    def execute_apply(self) -> Dict[str, Any]:
        """Simulates 'terraform apply -auto-approve' (Provisioning resources & updating terraform.tfstate)."""
        return {
            "status": "Apply complete!",
            "resources_added": 3,
            "resources_changed": 0,
            "resources_destroyed": 0,
            "state_file_updated": "s3://teachcloud-tf-state/prod/terraform.tfstate",
        }


# Quick tutorial runner functions
def run_tutorial_1_hcl() -> Dict[str, Any]:
    tf = HCLResourceSimulator("aws", "eu-west-1")
    tf.add_resource(
        "aws_vpc", "main", {"cidr_block": "10.0.0.0/16", "enable_dns_hostnames": True}
    )
    tf.add_resource(
        "aws_subnet",
        "public_1",
        {"vpc_id": "aws_vpc.main.id", "cidr_block": "10.0.1.0/24"},
    )
    return tf.validate_config()


def run_tutorial_2_modules() -> Dict[str, Any]:
    mod = TerraformModuleSimulator("database_cluster")
    mod.set_input_variable("db_instance_class", "db.t4g.micro")
    mod.set_input_variable("allocated_storage", 20)
    mod.set_output("db_endpoint", "prod-db.c123456789.eu-west-1.rds.amazonaws.com:5432")
    return mod.render_module()


def run_tutorial_3_plan_apply() -> Dict[str, Any]:
    pa = TerraformPlanApplySimulator("s3")
    changes = [
        {"resource": "aws_s3_bucket.media", "action": "create"},
        {"resource": "aws_security_group.web", "action": "create"},
        {"resource": "aws_instance.app_server", "action": "create"},
    ]
    plan = pa.execute_plan(changes)
    apply = pa.execute_apply()
    return {"plan_result": plan, "apply_result": apply}


if __name__ == "__main__":
    print("=== Terraform Tutorial 1 ===", run_tutorial_1_hcl())
    print("=== Terraform Tutorial 2 ===", run_tutorial_2_modules())
    print("=== Terraform Tutorial 3 ===", run_tutorial_3_plan_apply())
