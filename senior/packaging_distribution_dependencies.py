"""
Track 12: Packaging, Distribution & Dependency Resolution

Description: Master Senior Python Track 12: Packaging, Distribution & Dependency Resolution. Wheels vs sdist, Applications vs Libraries lockfiles, and modern Rust tooling (uv).
Level: Senior
URL: http://127.0.0.1:5000/python/senior/packaging_distribution_dependencies
"""

# --- Code Snippet 1 ---
# Application deterministic lockfile entry (uv.lock / poetry.lock):
[[package]]
name = "pydantic"
version = "2.6.4"
hashes = [
    { sha256 = "6d41ff1758c08a9f626a575a6c38ee21074e0d4cf96ffb47ec46e2a2223707cf" }
]

