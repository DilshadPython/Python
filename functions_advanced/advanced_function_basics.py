# Copyright (c) 2026 Teach Cloud / DilshadPython. All Rights Reserved.
# Unauthorized copying, re-hosting, scraping, or platform distribution is strictly prohibited.
# Official Platform: https://www.teach-cloud.net/ | Repository: https://github.com/dilshadpython

"""Advanced Python Functions, Decorators, Generators, Async Coroutines & Functools Utilities.

Import Notes & Architecture:
    - 'import asyncio': Standard library async runtime engine and event loop execution.
    - 'import functools': Advanced functional utilities (wraps, partial, lru_cache, singledispatch).
    - 'import inspect': Signature inspection, stack frames, and generator state checks.
    - 'import time': High-resolution timing benchmarks for decorator measurements.
    - 'from typing import Dict, List, Any, Union, Tuple, Optional, Callable, Generator, AsyncGenerator': PEP 484 type annotations.
"""

import asyncio
import functools
import inspect
import sys
import time
from typing import (
    Any,
    AsyncGenerator,
    Callable,
    Dict,
    Generator,
    List,
    Optional,
    Tuple,
    Union,
)

Number = Union[int, float]


# =========================================================================
# 1. DECORATORS & METADATA PRESERVATION
# =========================================================================
def timer_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator measuring function execution latency while preserving metadata via @functools.wraps."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Tuple[Any, float]:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        return result, round(elapsed, 6)
    return wrapper


def retry_decorator(retries: int = 3, delay: float = 0.01) -> Callable[..., Any]:
    """Parametrized decorator factory retrying execution on exceptions."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Dict[str, Any]:
            attempts = 0
            last_error: Optional[Exception] = None
            for attempt in range(1, retries + 1):
                attempts = attempt
                try:
                    res = func(*args, **kwargs)
                    return {"success": True, "attempts": attempts, "result": res, "error": None}
                except Exception as err:
                    last_error = err
                    time.sleep(delay)
            return {"success": False, "attempts": attempts, "result": None, "error": str(last_error)}
        return wrapper
    return decorator


class ExecutionCounterDecorator:
    """Class-based decorator tracking total invocation counts via __call__."""

    def __init__(self, func: Callable[..., Any]) -> None:
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        self.count += 1
        res = self.func(*args, **kwargs)
        return {"call_count": self.count, "output": res}


def decorator_patterns_and_wrappers(x: int, y: int) -> Dict[str, Any]:
    """Demonstrates function decorators, parametrized decorators, class decorators, and metadata preservation.

    Inspired by DilshadPython/Python/Functions-Advanced scripts:
    - basic_decorator.py
    - decorator_with_args.py
    - stacked_decorators.py
    - class_decorator.py
    - wraps_metadata.py
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Inputs 'x' and 'y' must be valid numbers")

    @timer_decorator
    def sample_multiply(a: int, b: int) -> int:
        """Multiplies two numbers."""
        return a * b

    product_val, latency = sample_multiply(x, y)

    @retry_decorator(retries=2, delay=0.001)
    def flaky_divider(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division by zero in flaky_divider")
        return a / b

    retry_success = flaky_divider(x, y)
    retry_failure = flaky_divider(x, 0)

    @ExecutionCounterDecorator
    def adder(a: int, b: int) -> int:
        return a + b

    call_1 = adder(x, y)
    call_2 = adder(x, 10)

    return {
        "timer_result": product_val,
        "latency_measured": latency > 0,
        "wrapped_name": sample_multiply.__name__,
        "wrapped_doc": sample_multiply.__doc__,
        "has_wrapped_attr": hasattr(sample_multiply, "__wrapped__"),
        "retry_success": retry_success,
        "retry_failure": retry_failure,
        "class_decorator_call_1": call_1,
        "class_decorator_call_2": call_2,
    }


# =========================================================================
# 2. GENERATORS & BIDIRECTIONAL COROUTINES
# =========================================================================
def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """Yields Fibonacci numbers up to the specified limit."""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


def subgenerator_worker() -> Generator[str, None, str]:
    """Subgenerator delegating sequence items and returning a final result string."""
    yield "Task Alpha"
    yield "Task Beta"
    return "Worker Complete"


def delegating_parent_generator() -> Generator[str, None, Dict[str, Any]]:
    """Parent generator delegating execution via 'yield from'."""
    yield "Header Start"
    worker_result = yield from subgenerator_worker()
    yield "Header End"
    return {"worker_summary": worker_result}


def interactive_accumulator() -> Generator[int, int, int]:
    """Bidirectional generator accepting values via .send()."""
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value
    return total


def generator_mechanics_and_coroutines(limit: int = 5) -> Dict[str, Any]:
    """Demonstrates yield, yield from subgenerator delegation, and bidirectional .send().

    Inspired by DilshadPython/Python/Functions-Advanced scripts:
    - generator_function.py
    - yield_from_delegation.py
    - generator_send_throw.py
    - generator_expression.py
    """
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Input 'limit' must be a positive integer")

    # 1. Standard generator iteration
    fib_gen = fibonacci_generator(limit)
    fib_list = list(fib_gen)

    # 2. yield from subgenerator delegation
    delegator = delegating_parent_generator()
    delegated_items: List[str] = []
    parent_summary: Optional[Dict[str, Any]] = None
    while True:
        try:
            item = next(delegator)
            delegated_items.append(item)
        except StopIteration as stop_err:
            parent_summary = stop_err.value
            break

    # 3. Bidirectional .send() communication
    accum = interactive_accumulator()
    next(accum)  # Prime generator
    step1 = accum.send(10)
    step2 = accum.send(25)
    final_total = 0
    try:
        accum.send(None)  # Terminate loop
    except StopIteration as stop_err:
        final_total = stop_err.value

    # 4. Memory comparison: Generator Expression vs List Comprehension
    gen_exp = (x ** 2 for x in range(1000))
    list_comp = [x ** 2 for x in range(1000)]

    return {
        "fibonacci_sequence": fib_list,
        "delegated_items": delegated_items,
        "parent_summary": parent_summary,
        "bidirectional_steps": [step1, step2],
        "final_accumulated_total": final_total,
        "gen_exp_size_bytes": sys.getsizeof(gen_exp),
        "list_comp_size_bytes": sys.getsizeof(list_comp),
    }


# =========================================================================
# 3. FUNCTOOLS: PARTIAL, LRU_CACHE & SINGLE DISPATCH
# =========================================================================
@functools.lru_cache(maxsize=128)
def cached_fibonacci(n: int) -> int:
    """Computes Fibonacci numbers with O(N) memoized runtime using @functools.lru_cache."""
    if n <= 1:
        return n
    return cached_fibonacci(n - 1) + cached_fibonacci(n - 2)


@functools.singledispatch
def process_data_payload(data: Any) -> str:
    """Base single-dispatch generic function fallback."""
    return f"Generic payload handler: {type(data).__name__}"


@process_data_payload.register(int)
def _(data: int) -> str:
    return f"Integer payload handler: value={data * 2}"


@process_data_payload.register(list)
def _(data: list) -> str:
    return f"List payload handler: count={len(data)}, sum={sum(x for x in data if isinstance(x, (int, float)))}"


@process_data_payload.register(dict)
def _(data: dict) -> str:
    return f"Dict payload handler: keys={list(data.keys())}"


def functools_advanced_utilities(base_power: int = 2) -> Dict[str, Any]:
    """Demonstrates functools.partial, lru_cache memoization, and singledispatch function overloading.

    Inspired by DilshadPython/Python/Functions-Advanced scripts:
    - partial_application.py
    - lru_cache_memoization.py
    - single_dispatch_overload.py
    """
    if not isinstance(base_power, int):
        raise TypeError("Input 'base_power' must be a valid integer")

    # 1. Partial Application
    def power_calculator(base: int, exponent: int) -> int:
        return base ** exponent

    square_func = functools.partial(power_calculator, exponent=base_power)
    cube_func = functools.partial(power_calculator, exponent=3)

    sq_val = square_func(5)  # 5^2 = 25
    cb_val = cube_func(5)    # 5^3 = 125

    # 2. LRU Cache memoization & cache_info
    cached_fibonacci.cache_clear()
    fib_30 = cached_fibonacci(30)
    cache_stats = cached_fibonacci.cache_info()

    # 3. Single Dispatch Overloading
    res_int = process_data_payload(42)
    res_list = process_data_payload([10, 20, 30])
    res_dict = process_data_payload({"name": "Dilshad", "role": "Engineer"})
    res_str = process_data_payload("Hello Python")

    return {
        "partial_square_5": sq_val,
        "partial_cube_5": cb_val,
        "partial_target_func": square_func.func.__name__,
        "partial_keywords": square_func.keywords,
        "cached_fib_30": fib_30,
        "cache_hits": cache_stats.hits,
        "cache_misses": cache_stats.misses,
        "cache_maxsize": cache_stats.maxsize,
        "singledispatch_int": res_int,
        "singledispatch_list": res_list,
        "singledispatch_dict": res_dict,
        "singledispatch_str": res_str,
    }


# =========================================================================
# 4. ASYNC COROUTINES & ASYNC GENERATORS
# =========================================================================
async def async_fetch_data(task_id: int, delay: float = 0.001) -> Dict[str, Any]:
    """Native async coroutine simulating asynchronous I/O retrieval."""
    await asyncio.sleep(delay)
    return {"task_id": task_id, "status": "completed", "timestamp": time.time()}


async def async_stream_generator(count: int) -> AsyncGenerator[int, None]:
    """Asynchronous generator yielding streamed items with non-blocking delays."""
    for i in range(1, count + 1):
        await asyncio.sleep(0.001)
        yield i * 10


def async_coroutines_and_generators(task_count: int = 3) -> Dict[str, Any]:
    """Demonstrates native async def / await coroutines and async generators using asyncio.run().

    Inspired by DilshadPython/Python/Functions-Advanced scripts:
    - async_coroutine.py
    - async_generator.py
    """
    if not isinstance(task_count, int) or task_count <= 0:
        raise ValueError("Input 'task_count' must be a positive integer")

    async def main_async_runner() -> Dict[str, Any]:
        tasks = [async_fetch_data(i) for i in range(1, task_count + 1)]
        coroutine_results = await asyncio.gather(*tasks)

        streamed_items: List[int] = []
        async for item in async_stream_generator(task_count):
            streamed_items.append(item)

        return {
            "coroutine_results": coroutine_results,
            "streamed_items": streamed_items,
        }

    # Execute async pipeline synchronously inside tutorial wrapper
    async_summary = asyncio.run(main_async_runner())
    return async_summary


# =========================================================================
# 5. PYTHON 2.7 LEGACY ADVANCED FUNCTION COMPARISON
# =========================================================================
def python2_legacy_advanced_comparison() -> Dict[str, Any]:
    """Demonstrates legacy Python 2.7 advanced function patterns vs Python 3 modern equivalents.

    Illustrates:
    - Decorators without @functools.wraps losing metadata vs Python 3 metadata preservation
    - Legacy gen.next() method vs Python 3 next(gen) / gen.__next__()
    - Manual dictionary memoization class vs Python 3 @functools.lru_cache
    - Legacy generator coroutines vs Python 3 native async def / await
    """
    # 1. Python 2.7 generator .next() vs Python 3 next()
    def sample_gen() -> Generator[int, None, None]:
        yield 100
        yield 200

    g = sample_gen()
    val_1 = next(g)  # Modern Python 3 syntax replacing legacy g.next()
    val_2 = next(g)

    # 2. Python 2.7 manual memoization class vs Python 3 @lru_cache
    class ManualMemoizePy2:
        def __init__(self, func: Callable[..., Any]) -> None:
            self.func = func
            self.cache: Dict[Tuple[Any, ...], Any] = {}

        def __call__(self, *args: Any) -> Any:
            if args not in self.cache:
                self.cache[args] = self.func(*args)
            return self.cache[args]

    @ManualMemoizePy2
    def manual_factorial(n: int) -> int:
        if n <= 1:
            return 1
        return n * manual_factorial(n - 1)

    fact_5 = manual_factorial(5)
    cache_keys_count = len(manual_factorial.cache)

    return {
        "generator_next_py3_syntax": [val_1, val_2],
        "manual_memoize_py2_result": fact_5,
        "manual_memoize_cache_size": cache_keys_count,
        "py3_lru_cache_advantage": "@functools.lru_cache handles maxsize eviction, thread safety & C-level speed",
    }


# =========================================================================
# 6. INTROSPECTION OF ADVANCED FUNCTION OBJECTS
# =========================================================================
def execute_advanced_function_introspection() -> Dict[str, Any]:
    """Demonstrates introspection of generator frames, partial objects, lru_cache stats, and decorated wrappers."""
    gen = fibonacci_generator(3)
    gen_frame = inspect.getgeneratorstate(gen)

    def target(a: int, b: int, c: int) -> int:
        return a + b + c

    part = functools.partial(target, b=20)

    @timer_decorator
    def annotated_fn(x: int) -> int:
        """Annotated function doc."""
        return x * 2

    return {
        "generator_state_created": gen_frame,
        "generator_is_running": inspect.isgeneratorfunction(fibonacci_generator),
        "partial_func_name": part.func.__name__,
        "partial_keywords": part.keywords,
        "decorated_wrapped_name": annotated_fn.__wrapped__.__name__,
        "decorated_docstring": annotated_fn.__doc__,
        "is_coroutine_function": inspect.iscoroutinefunction(async_fetch_data),
    }
