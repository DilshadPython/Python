# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import sys: Standard library module for interpreter introspection and version info.
# - import time: Standard library module for execution benchmarking.
# - from typing import Any, Dict, List, Tuple: PEP 484 type annotations.
# - import numpy as np: High-performance scientific computing and matrix library.
# =========================================================================
import sys
import time
from typing import Any, Dict, List, Tuple
import numpy as np

from cloud_app.python.tutorials.junior.python_versions_tutorials.v33_to_v36_foundations.version_33_to_36_features import (
    demonstrate_python33_to_36_features,
)
from cloud_app.python.tutorials.junior.python_versions_tutorials.v37_to_v310_modern_features.version_37_to_310_features import (
    demonstrate_python37_to_310_features,
)
from cloud_app.python.tutorials.junior.python_versions_tutorials.v311_to_v313_performance_and_jit.version_311_to_313_features import (
    demonstrate_python311_to_313_features,
)


def run_01_foundations_33_to_36() -> Dict[str, Any]:
    """Executes Python 3.3 to Python 3.6 evolution feature demonstrations."""
    return demonstrate_python33_to_36_features()


def run_02_modern_features_37_to_310() -> Dict[str, Any]:
    """Executes Python 3.7 to Python 3.10 evolution feature demonstrations."""
    return demonstrate_python37_to_310_features()


def run_03_performance_and_jit_311_to_313() -> Dict[str, Any]:
    """Executes Python 3.11 to Python 3.13 evolution feature demonstrations."""
    return demonstrate_python311_to_313_features()


def run_all_python_version_demos() -> Dict[str, Any]:
    """
    Executes all 3 subfolder Python Version Evolution curriculum demonstrations in sequence.

    Returns:
        Dict[str, Any]: Aggregated dictionary containing execution outputs across Python 3.3 to 3.13.
    """
    return {
        "01_foundations_33_to_36": run_01_foundations_33_to_36(),
        "02_modern_features_37_to_310": run_02_modern_features_37_to_310(),
        "03_performance_and_jit_311_to_313": run_03_performance_and_jit_311_to_313(),
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(run_all_python_version_demos())
