"""
Senior Level Python Keywords Demonstration Module.

This module provides advanced asynchronous coroutines, structural pattern matching,
CPython AST keyword parsing, soft keyword evaluation, and type statement analysis
designed for senior software architects (`async`, `await`, `match`, `case`, `_`, `type`, `ast.parse`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import ast`: CPython Abstract Syntax Tree parser and compiler module.
# - `import asyncio`: Asynchronous I/O event loop and coroutine framework.
# - `import sys`: System utilities for runtime environment introspection.
# - `from typing import Any, Dict, List`: PEP 484 type hint generics.
# =========================================================================
import ast
import asyncio
import sys
from typing import Any, Dict, List


async def async_fetch_data(resource_id: int) -> Dict[str, Any]:
    """Asynchronous worker coroutine using `async` and `await`.

    Args:
        resource_id (int): Target resource identifier.

    Returns:
        Dict[str, Any]: Simulated fetched payload dictionary.
    """
    # Non-blocking pause yielding control back to asyncio event loop
    await asyncio.sleep(0.01)
    return {"resource_id": resource_id, "status": "active", "payload": f"Data Packet {resource_id}"}


async def demonstrate_async_concurrency(item_ids: List[int]) -> List[Dict[str, Any]]:
    """Gather and process multiple asynchronous tasks concurrently using `async` / `await`.

    Args:
        item_ids (List[int]): List of resource IDs to fetch.

    Returns:
        List[Dict[str, Any]]: Collected data payloads.
    """
    tasks = [async_fetch_data(item_id) for item_id in item_ids]
    results = await asyncio.gather(*tasks)
    return list(results)


def demonstrate_pattern_matching(command_input: str) -> str:
    """Demonstrate Structural Pattern Matching soft keywords (`match`, `case`, `_`).

    Args:
        command_input (str): CLI or API command string.

    Returns:
        str: Route action description.
    """
    tokens = command_input.strip().split()

    # CPython 3.10+ Structural Pattern Matching (`match` / `case`)
    match tokens:
        case ["start", service]:
            return f"Action: Launching service '{service}'"
        case ["stop", service]:
            return f"Action: Terminating service '{service}'"
        case ["status"]:
            return "Action: Checking cluster health status"
        case [action, *args] if action in ("reload", "restart"):
            return f"Action: Performing {action} with arguments {args}"
        case _:
            return f"Action: Unrecognized command format '{command_input}'"


def extract_keywords_from_ast(source_code: str) -> List[str]:
    """Parse Python source code using Abstract Syntax Tree (`ast`) and extract keywords.

    Args:
        source_code (str): Python source code snippet.

    Returns:
        List[str]: List of AST node class names representing structural keywords.
    """
    parsed_ast = ast.parse(source_code)
    keywords_found: List[str] = []

    for node in ast.walk(parsed_ast):
        node_name = type(node).__name__
        if node_name in ("If", "For", "While", "Try", "With", "AsyncFunctionDef", "Return", "Yield", "Match"):
            keywords_found.append(node_name)

    return keywords_found


def demonstrate_type_statement_analysis(word: str) -> Dict[str, Any]:
    """Analyze soft keywords and modern type statement identifiers (Python 3.12+ `type`).

    Args:
        word (str): Identifier string to evaluate.

    Returns:
        Dict[str, Any]: Analysis details.
    """
    import keyword

    is_hard = keyword.iskeyword(word)
    is_soft = getattr(keyword, "issoftkeyword", lambda w: False)(word)

    return {
        "identifier": word,
        "is_hard_keyword": is_hard,
        "is_soft_keyword": is_soft,
        "valid_variable_name": word.isidentifier() and not is_hard,
    }


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for senior keywords demonstration."""
    print("=== Senior Level Python Keywords Demonstration ===")

    # Asynchronous event loop execution
    results = asyncio.run(demonstrate_async_concurrency([101, 102, 103]))
    print("Async Coroutines (async / await):", results)

    # Structural pattern matching
    print("Pattern Matching (match / case):", demonstrate_pattern_matching("start database"))
    print("Pattern Matching Unknown:", demonstrate_pattern_matching("unknown_cmd"))

    # AST Keyword Parsing
    sample_code = "async def fetch(): try: return 1\n except: pass"
    print("AST Keywords Extracted:", extract_keywords_from_ast(sample_code))

    # Type statement analysis
    print("Type Statement Analysis ('match'):", demonstrate_type_statement_analysis("match"))
    print("Type Statement Analysis ('type'):", demonstrate_type_statement_analysis("type"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
