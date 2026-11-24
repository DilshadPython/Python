"""
Demonstrates generator delegation using the 'yield from' expression (PEP 380).
Allows delegating iteration to sub-generators and flattening nested iterables.
"""
# "from module import name" imports type annotation symbols directly into local scope.
from typing import Any, Generator, Iterable, List


def sub_generator(name: str, count: int) -> Generator[str, None, str]:
    """Sub-generator yielding formatted items and returning a final status string."""
    for i in range(1, count + 1):
        yield f"{name}-Item-{i}"
    return f"Completed {name}"


def delegating_generator() -> Generator[str, None, List[str]]:
    """
    Delegating generator using 'yield from' to consume sub-generators transparently.
    Captures return values from sub-generators.
    """
    results: List[str] = []
    res1 = yield from sub_generator("Alpha", 3)
    results.append(res1)
    res2 = yield from sub_generator("Beta", 2)
    results.append(res2)
    return results


def flatten_nested(iterable: Iterable[Any]) -> Generator[Any, None, None]:
    """
    Recursively flatten nested structures using 'yield from'.
    
    Args:
        iterable (Iterable[Any]): Nested list or iterable.
        
    Yields:
        Any: Flattened non-iterable values.
    """
    for item in iterable:
        if isinstance(item, (list, tuple)):
            yield from flatten_nested(item)
        else:
            yield item


if __name__ == '__main__':
    print("=== Delegating Generator Output ===")
    gen = delegating_generator()
    try:
        while True:
            item = next(gen)
            print("Yielded:", item)
    except StopIteration as exc:
        print("Final Return Value from delegating generator:", exc.value)

    print("\n=== Recursive Flatten Output ===")
    nested_list = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
    print("Original Nested List:", nested_list)
    print("Flattened List:", list(flatten_nested(nested_list)))
