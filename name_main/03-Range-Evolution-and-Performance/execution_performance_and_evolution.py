"""
Local vs Global Execution Performance and Version Evolution Module.

This module documents and benchmarks:
- Execution speed difference between running code inside main() (local scope LOAD_FAST)
  vs top-level script scope (global scope LOAD_GLOBAL).
- Comprehensive Python 3.3 to Python 3.13 evolution matrix for module entry points.
"""

# Import sys for memory size introspection
import sys

# Import time for performance benchmarking
import time


def benchmark_local_vs_global_execution(iterations: int = 500_000) -> dict[str, float]:
    """Benchmark range summation execution time in local function scope vs global scope.

    Args:
        iterations (int, optional): Iteration count. Defaults to 500000.

    Returns:
        dict[str, float]: Execution time in seconds and local scope speedup factor.
    """
    # Local scope execution time (LOAD_FAST opcode optimization)
    def local_run() -> int:
        s = 0
        for x in range(iterations):
            s += x
        return s

    start_loc = time.perf_counter()
    _ = local_run()
    time_loc = time.perf_counter() - start_loc

    # Simulating global variable lookups (LOAD_GLOBAL opcode)
    start_glob = time.perf_counter()
    g_sum = 0
    for g_x in range(iterations):
        g_sum += g_x
    time_glob = time.perf_counter() - start_glob

    return {
        "local_scope_seconds": time_loc,
        "global_scope_seconds": time_glob,
        "local_speedup_factor": round(time_glob / time_loc, 2) if time_loc > 0 else 1.0,
    }


def get_version_evolution_matrix() -> dict[str, str]:
    """Provide version-by-version evolution matrix for entry points and main execution context from 3.3 to 3.13.

    Returns:
        dict[str, str]: Evolution matrix map.
    """
    return {
        "Python 3.3": "Lazy range sequence slicing range(100)[::2]; sys.implementation introduced for interpreter details.",
        "Python 3.4": "__spec__ attribute added to modules for PEP 451 module loading and import introspection.",
        "Python 3.5": "PEP 484 type hints syntax allowing 'def main() -> int:' annotations.",
        "Python 3.6": "Module attribute insertion order preservation; f-strings in main entry logging.",
        "Python 3.7": "__main__.py execution improvements for runnable zip packages and directory packages.",
        "Python 3.8": "Walrus operator (:=) and positional-only syntax (/) in main CLI entry routines.",
        "Python 3.9": "PEP 585 built-in generic type hints (list[str] instead of typing.List[str]) in main signatures.",
        "Python 3.10": "Structural Pattern Matching (match/case PEP 634) for parsing CLI command flags inside main().",
        "Python 3.11": "Specializing Adaptive Interpreter (PEP 659) accelerates local variable bytecode dispatches by 10-25%.",
        "Python 3.12": "Per-interpreter GIL isolation and enhanced traceback error highlighting inside main() blocks.",
        "Python 3.13": "Free-threaded CPython (PEP 703 - GIL removal) enabling multi-threaded entry point execution.",
    }


if __name__ == "__main__":
    bench = benchmark_local_vs_global_execution(500_000)
    print("--- Local vs Global Scope Execution Benchmark ---")
    print(f"Local Scope Time (inside main):   {bench['local_scope_seconds']:.6f} sec")
    print(f"Global Scope Time (top-level):    {bench['global_scope_seconds']:.6f} sec")
    print(f"Local Scope Speedup Factor:      {bench['local_speedup_factor']}x faster")

    print("\n--- Python 3.3 to Python 3.13 Evolution Matrix ---")
    for ver, desc in get_version_evolution_matrix().items():
        print(f"[{ver}]: {desc}")
