"""cloud_app/tutorials/concurrency_parallelism_basics.py

Python Concurrency, Parallelism & Asynchronous Programming Masterclass
=======================================================================
Comprehensive tutorial module demonstrating:
1. Sequential Execution vs Threading vs Multiprocessing vs Asyncio
2. Thread Safety, Race Conditions & Mutex Locks (threading.Lock)
3. Multiprocessing CPU-Bound Parallel Compute (ProcessPoolExecutor)
4. Asyncio Event Loop & Cooperative Multitasking (async/await)
5. Thread-Safe Producer-Consumer Pattern (queue.Queue)
"""

import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import queue
import threading
import time
from typing import Any, Dict, List, Tuple


# ==============================================================================
# 1. SEQUENTIAL VS CONCURRENCY VS PARALLELISM SIMULATION
# ==============================================================================


def simulate_io_task(task_id: int, duration_sec: float = 0.1) -> Dict[str, Any]:
    """Simulate I/O-bound network request or file read."""
    time.sleep(duration_sec)
    return {"task_id": task_id, "duration": duration_sec, "status": "COMPLETED"}


def cpu_bound_heavy_task(n: int = 500_000) -> int:
    """Simulate CPU-intensive calculation (sum of squares)."""
    return sum(i * i for i in range(n))


def run_sequential_io(task_count: int = 4) -> Tuple[List[Dict[str, Any]], float]:
    """Sequential Execution: Synchronous blocking tasks executed one by one."""
    t0 = time.perf_counter()
    results = [simulate_io_task(i) for i in range(task_count)]
    elapsed = time.perf_counter() - t0
    return results, round(elapsed * 1000, 2)


def run_threaded_io(task_count: int = 4) -> Tuple[List[Dict[str, Any]], float]:
    """Threading: Concurrent I/O-bound execution releasing GIL during sleep."""
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=task_count) as executor:
        futures = [executor.submit(simulate_io_task, i) for i in range(task_count)]
        results = [f.result() for f in futures]
    elapsed = time.perf_counter() - t0
    return results, round(elapsed * 1000, 2)


# ==============================================================================
# 2. THREAD SAFETY & RACE CONDITION MUTEX LOCKS
# ==============================================================================


class UnsafeCounter:
    """Thread-unsafe shared counter vulnerable to race conditions."""

    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        # Non-atomic read-modify-write operation
        current = self.value
        time.sleep(0.0001)  # Force thread context switch
        self.value = current + 1


class SafeCounter:
    """Thread-safe counter protected by a Mutex Lock (threading.Lock)."""

    def __init__(self) -> None:
        self.value = 0
        self._lock = threading.Lock()

    def increment(self) -> None:
        with self._lock:  # Acquire & release mutex automatically
            current = self.value
            time.sleep(0.0001)
            self.value = current + 1


def demonstrate_race_condition(thread_count: int = 10) -> Dict[str, Any]:
    """Demonstrate data corruption from race condition vs Mutex Lock protection."""
    unsafe_cnt = UnsafeCounter()
    safe_cnt = SafeCounter()

    # Run Unsafe Threads
    threads = [
        threading.Thread(target=unsafe_cnt.increment) for _ in range(thread_count)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # Run Safe Threads
    safe_threads = [
        threading.Thread(target=safe_cnt.increment) for _ in range(thread_count)
    ]
    for t in safe_threads:
        t.start()
    for t in safe_threads:
        t.join()

    return {
        "expected_final_count": thread_count,
        "unsafe_race_count": unsafe_cnt.value,
        "safe_mutex_lock_count": safe_cnt.value,
        "race_condition_detected": unsafe_cnt.value != thread_count,
        "mutex_lock_verified": safe_cnt.value == thread_count,
    }


# ==============================================================================
# 3. MULTIPROCESSING CPU-BOUND PARALLEL COMPUTE
# ==============================================================================


def benchmark_multiprocessing_cpu(iterations: int = 4) -> Dict[str, Any]:
    """Compare Sequential CPU compute vs Multiprocessing multi-core parallelism."""
    # 1. Sequential CPU execution
    t0 = time.perf_counter()
    seq_res = [cpu_bound_heavy_task(400_000) for _ in range(iterations)]
    t1 = time.perf_counter()
    seq_time_ms = (t1 - t0) * 1000

    # 2. Multiprocessing parallel execution (Separate OS processes bypassing GIL)
    t2 = time.perf_counter()
    with ProcessPoolExecutor(max_workers=min(4, iterations)) as executor:
        futures = [
            executor.submit(cpu_bound_heavy_task, 400_000) for _ in range(iterations)
        ]
        parallel_res = [f.result() for f in futures]
    t3 = time.perf_counter()
    parallel_time_ms = (t3 - t2) * 1000

    return {
        "iterations": iterations,
        "sequential_time_ms": round(seq_time_ms, 2),
        "parallel_time_ms": round(parallel_time_ms, 2),
        "speedup_factor": round(seq_time_ms / max(parallel_time_ms, 1e-9), 2),
        "computed_sum_sample": parallel_res[0],
    }


# ==============================================================================
# 4. ASYNCIO EVENT LOOP & COOPERATIVE MULTITASKING
# ==============================================================================


async def async_fetch_data(endpoint_id: int, delay: float = 0.05) -> Dict[str, Any]:
    """Asynchronous coroutine using non-blocking await."""
    await asyncio.sleep(delay)  # Yields control back to event loop
    return {"endpoint_id": endpoint_id, "data": f"Payload-{endpoint_id}", "status": 200}


async def run_asyncio_event_loop(
    total_requests: int = 5,
) -> Tuple[List[Dict[str, Any]], float]:
    """Concurrently execute async coroutines on single-threaded Event Loop."""
    t0 = time.perf_counter()
    tasks = [async_fetch_data(i) for i in range(total_requests)]
    results = await asyncio.gather(*tasks)
    elapsed_ms = (time.perf_counter() - t0) * 1000
    return list(results), round(elapsed_ms, 2)


def execute_asyncio_pipeline(total_requests: int = 5) -> Dict[str, Any]:
    """Synchronous wrapper to launch asyncio event loop."""
    results, elapsed_ms = asyncio.run(run_asyncio_event_loop(total_requests))
    return {
        "request_count": total_requests,
        "elapsed_ms": elapsed_ms,
        "results_sample": results[:2],
        "asyncio_status": "SUCCESS",
    }


# ==============================================================================
# 5. THREAD-SAFE PRODUCER-CONSUMER QUEUE PATTERN
# ==============================================================================


def demonstrate_producer_consumer_queue(item_count: int = 5) -> Dict[str, Any]:
    """Demonstrate thread-safe Queue coordination between producer and consumer."""
    task_queue: queue.Queue[str] = queue.Queue()
    processed_items: List[str] = []

    def producer():
        for i in range(item_count):
            item = f"Job-{i + 1}"
            task_queue.put(item)
            time.sleep(0.01)

    def consumer():
        while len(processed_items) < item_count:
            try:
                item = task_queue.get(timeout=0.2)
                processed_items.append(f"Processed_{item}")
                task_queue.task_done()
            except queue.Empty:
                break

    t_prod = threading.Thread(target=producer)
    t_cons = threading.Thread(target=consumer)

    t_prod.start()
    t_cons.start()

    t_prod.join()
    t_cons.join()

    return {
        "items_produced": item_count,
        "items_consumed": len(processed_items),
        "queue_empty": task_queue.empty(),
        "processed_sample": processed_items,
    }


# ==============================================================================
# DEMONSTRATION HELPER FUNCTIONS FOR INTERACTIVE STUDIO
# ==============================================================================


def demonstrate_all_concurrency_pillars() -> Dict[str, Any]:
    """Execute master summary benchmark across Sequential, Threading, Multiprocessing, and Asyncio."""
    _, seq_ms = run_sequential_io(4)
    _, thread_ms = run_threaded_io(4)
    race_res = demonstrate_race_condition(10)
    async_res = execute_asyncio_pipeline(5)
    queue_res = demonstrate_producer_consumer_queue(5)

    return {
        "sequential_io_ms": seq_ms,
        "threaded_io_ms": thread_ms,
        "io_speedup_factor": round(seq_ms / max(thread_ms, 1e-9), 2),
        "race_condition": race_res,
        "asyncio": async_res,
        "producer_consumer_queue": queue_res,
    }


if __name__ == "__main__":
    print("=== Python Concurrency & Parallelism Masterclass ===")
    summary = demonstrate_all_concurrency_pillars()
    print(
        "IO Benchmark:",
        f"Sequential {summary['sequential_io_ms']}ms vs Threaded {summary['threaded_io_ms']}ms",
    )
    print("Race Condition Test:", summary["race_condition"])
    print("Asyncio Result:", summary["asyncio"])
    print("Queue Result:", summary["producer_consumer_queue"])
