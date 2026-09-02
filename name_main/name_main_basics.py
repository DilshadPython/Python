"""
Master Executable Script for __name__ == '__main__' Tutorial Module.

This script executes and demonstrates all three curriculum steps:
- Step 1: 01-Fundamentals (execution context, __name__ variable, main entry point idiom).
- Step 2: 02-Advanced-Math-and-Operators (module import vs direct execution, sys.argv CLI parsing).
- Step 3: 03-Range-Evolution-and-Performance (local vs global execution speed, reflection).
"""

# Import pathlib and sys to configure folder import paths
from pathlib import Path
import sys

# Ensure subfolder modules can be imported directly
BASE_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(BASE_DIR / "01-Fundamentals"))
sys.path.insert(0, str(BASE_DIR / "02-Advanced-Math-and-Operators"))
sys.path.insert(0, str(BASE_DIR / "03-Range-Evolution-and-Performance"))

# Import Step 1 functions
from main_entry_point_idiom import calculate_square_sequence
from name_attribute_basics import format_greeting, get_execution_context

# Import Step 2 functions
from cli_args_and_execution_context import parse_cli_arguments
from module_import_vs_execution import analyze_imported_module

# Import Step 3 functions
from execution_performance_and_evolution import benchmark_local_vs_global_execution
from reflection_and_introspection import introspect_module_attributes, introspect_range_attributes


def run_name_main_curriculum_demo() -> None:
    """Execute master pedagogical demonstration across all 3 steps."""
    print("=" * 65)
    print(" STEP 1: __name__ ATTRIBUTE FUNDAMENTALS & ENTRY POINTS")
    print("=" * 65)
    ctx = get_execution_context()
    print(f"Current Module __name__: '{ctx['module_name']}'")
    print(f"Execution Mode:         '{ctx['execution_mode']}'")
    print(f"Greeting:               '{format_greeting()}'")
    print(f"Calculated Squares:     {calculate_square_sequence(5)}")

    print("\n" + "=" * 65)
    print(" STEP 2: MODULE IMPORT VS DIRECT EXECUTION & CLI ARGS")
    print("=" * 65)
    imp_analysis = analyze_imported_module()
    print(f"Current Module:          '{imp_analysis['current_file_module']}'")
    print(f"Imported Func Module:   '{imp_analysis['imported_func_module']}'")
    parsed_cli = parse_cli_arguments(["script.py", "--mode=demo", "--verbose"])
    print(f"Parsed CLI Arguments:    {parsed_cli['arguments']}")

    print("\n" + "=" * 65)
    print(" STEP 3: SCOPE PERFORMANCE BENCHMARKS & REFLECTION")
    print("=" * 65)
    bench = benchmark_local_vs_global_execution(200_000)
    print(f"Local Scope (main()):   {bench['local_scope_seconds']:.6f} sec")
    print(f"Global Scope (top):     {bench['global_scope_seconds']:.6f} sec")
    print(f"Local Scope Speedup:    {bench['local_speedup_factor']}x faster")

    rng_info = introspect_range_attributes()
    print(f"Public range() Attributes: {rng_info['public_attribute_list']}")
    print("=" * 65)


if __name__ == "__main__":
    run_name_main_curriculum_demo()
