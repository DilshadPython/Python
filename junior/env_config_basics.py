"""cloud_app/tutorials/env_config_basics.py

Environment Configuration, Secrets & Multi-Stage Management Masterclass
========================================================================
Comprehensive tutorial module demonstrating:
1. Reading & Parsing Environment Variables via os.environ & dotenv
2. Class-Based Configuration Hierarchy (Base, Development, Testing, Production)
3. Type-Casting & Validation for Environment Variables (bool, int, secret lists)
4. Secrets Management & Git Exclusion Best Practices (.gitignore)
5. Modern Type-Safe Settings Management Pattern (Pydantic BaseSettings style)
"""

import os
import re
from typing import Any, Dict, List, Optional, Type


# ==============================================================================
# 1. DOTENV PARSER & OS.ENVIRON LOADER SIMULATOR
# ==============================================================================


class DotEnvParser:
    """Parses raw .env file contents into key-value environment dictionary."""

    @staticmethod
    def parse_dotenv_content(content: str) -> Dict[str, str]:
        """Parse key=value pairs, stripping whitespace, quotes, and comments."""
        env_vars = {}
        for line in content.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip().strip("'\"")
                env_vars[key] = val
        return env_vars


def get_env_var(key: str, default: Optional[str] = None, required: bool = False) -> str:
    """Retrieve an environment variable with fallback defaults or strict missing error."""
    val = os.environ.get(key, default)
    if required and (val is None or val == ""):
        raise KeyError(f"CRITICAL: Required environment variable '{key}' is not set!")
    return val or ""


def parse_bool_env(key: str, default: bool = False) -> bool:
    """Parse boolean environment variables ('true', '1', 'yes', 'on')."""
    val = os.environ.get(key, "").lower().strip()
    if not val:
        return default
    return val in ("true", "1", "yes", "on", "t")


def parse_list_env(key: str, default: Optional[List[str]] = None) -> List[str]:
    """Parse comma-separated environment variables into a list of strings."""
    if default is None:
        default = []
    val = os.environ.get(key, "")
    if not val:
        return default
    return [item.strip() for item in val.split(",") if item.strip()]


# ==============================================================================
# 2. CLASS-BASED CONFIGURATION HIERARCHY (DEV / TEST / PROD)
# ==============================================================================


class BaseConfig:
    """Base configuration shared across all application environments."""

    APP_NAME: str = "TeachCloud Enterprise Platform"
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "insecure-dev-key-change-in-prod")
    API_PORT: int = int(os.environ.get("API_PORT", "5000"))
    ALLOWED_HOSTS: List[str] = parse_list_env(
        "ALLOWED_HOSTS", ["localhost", "127.0.0.1"]
    )
    DATABASE_URI: str = os.environ.get("DATABASE_URL", "sqlite:///dev.db")
    DEBUG: bool = False
    TESTING: bool = False

    @classmethod
    def get_redacted_config(cls) -> Dict[str, Any]:
        """Return config dict with sensitive secrets masked for safe logging."""
        return {
            "APP_NAME": cls.APP_NAME,
            "SECRET_KEY": "********" if cls.SECRET_KEY else "NOT_SET",
            "API_PORT": cls.API_PORT,
            "ALLOWED_HOSTS": cls.ALLOWED_HOSTS,
            "DATABASE_URI": cls._redact_uri(cls.DATABASE_URI),
            "DEBUG": cls.DEBUG,
            "TESTING": cls.TESTING,
        }

    @staticmethod
    def _redact_uri(uri: str) -> str:
        """Mask passwords in database connection strings (e.g. postgresql://user:pass@host/db)."""
        return re.sub(r":([^@]+)@", ":****@", uri)


class DevelopmentConfig(BaseConfig):
    """Development environment configuration with verbose logging and hot reloading."""

    DEBUG: bool = True
    TESTING: bool = False
    DATABASE_URI: str = os.environ.get(
        "DEV_DATABASE_URL", "sqlite:///teachcloud_dev.db"
    )


class TestingConfig(BaseConfig):
    """Automated testing environment configuration with isolated in-memory database."""

    DEBUG: bool = True
    TESTING: bool = True
    DATABASE_URI: str = "sqlite:///:memory:"
    SECRET_KEY: str = "test-secret-key-for-unit-testing"


class ProductionConfig(BaseConfig):
    """Production environment configuration with strict security and secrets verification."""

    DEBUG: bool = False
    TESTING: bool = False
    DATABASE_URI: str = os.environ.get(
        "PROD_DATABASE_URL",
        "postgresql://cloud_user:secret123@prod-db.host:5432/cloud_db",
    )

    @classmethod
    def validate_production_security(cls) -> List[str]:
        """Validate production configuration security constraints."""
        warnings = []
        if cls.DEBUG:
            warnings.append(
                "SECURITY ALERT: DEBUG mode must NEVER be enabled in Production!"
            )
        if "insecure" in cls.SECRET_KEY or len(cls.SECRET_KEY) < 16:
            warnings.append(
                "SECURITY ALERT: Production SECRET_KEY is too weak or using default!"
            )
        if "sqlite" in cls.DATABASE_URI:
            warnings.append(
                "WARNING: Production should use an enterprise database (PostgreSQL/MySQL), not SQLite."
            )
        return warnings


CONFIG_MAP: Dict[str, Type[BaseConfig]] = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


def get_config_by_name(env_name: str = "development") -> Type[BaseConfig]:
    """Factory function retrieving configuration class based on FLASK_ENV or APP_ENV."""
    return CONFIG_MAP.get(env_name.lower(), DevelopmentConfig)


# ==============================================================================
# 3. SECRETS MANAGEMENT & GIT EXCLUSION AUDITOR
# ==============================================================================


def generate_sample_dotenv() -> str:
    """Generate sample .env file content."""
    return """# TeachCloud Application Environment Configuration
APP_ENV=development
API_PORT=8080
SECRET_KEY=super-secret-production-jwt-key-2026
DATABASE_URL=postgresql://cloud_admin:SecurePass123!@localhost:5432/teachcloud_db
ALLOWED_HOSTS=teachcloud.dev,api.teachcloud.dev
DEBUG=true
"""


def audit_gitignore_secrets(gitignore_lines: List[str]) -> Dict[str, Any]:
    """Audit .gitignore entries to ensure secret files (.env, *.pem, *.key) are protected."""
    required_ignores = [".env", ".env.local", "*.pem", "*.key", "secrets.json"]
    found = []
    missing = []

    for item in required_ignores:
        if any(item in line for line in gitignore_lines):
            found.append(item)
        else:
            missing.append(item)

    return {
        "status": "PASS" if not missing else "WARNING",
        "found_exclusions": found,
        "missing_exclusions": missing,
        "recommendation": "Add missing secret patterns to .gitignore to prevent credential leaks to Git.",
    }


# ==============================================================================
# MASTER DEMONSTRATION FUNCTION FOR INTERACTIVE STUDIO
# ==============================================================================


def demonstrate_env_config_masterclass() -> Dict[str, Any]:
    """Execute master environment configuration workflow simulation."""
    dotenv_raw = generate_sample_dotenv()
    parsed_env = DotEnvParser.parse_dotenv_content(dotenv_raw)

    dev_config = DevelopmentConfig.get_redacted_config()
    test_config = TestingConfig.get_redacted_config()
    prod_config = ProductionConfig.get_redacted_config()
    prod_sec = ProductionConfig.validate_production_security()

    gitignore_audit = audit_gitignore_secrets(
        [".env", ".env.local", "*.pem", "venv/", "__pycache__/"]
    )

    return {
        "parsed_dotenv_sample": parsed_env,
        "development_config": dev_config,
        "testing_config": test_config,
        "production_config_redacted": prod_config,
        "production_security_warnings": prod_sec,
        "gitignore_secrets_audit": gitignore_audit,
    }


if __name__ == "__main__":
    print("=== Environment Configuration & Secrets Masterclass ===")
    demo = demonstrate_env_config_masterclass()
    print("Parsed .env:", demo["parsed_dotenv_sample"])
    print("Prod Redacted:", demo["production_config_redacted"])
    print("Secrets Audit:", demo["gitignore_secrets_audit"])
