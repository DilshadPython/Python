# ─────────────────────────────────────────────────────────────────────────────
# tests/test_yield_tutorial.py — Unit Tests for Yield Generators Tutorial
# ─────────────────────────────────────────────────────────────────────────────
import pytest
import sys
from typing import Dict, Any

from cloud_app.tutorials.yield_basics import (
    count_up_generator,
    fibonacci_generator,
    interactive_accumulator_generator,
    delegating_generator,
    pipeline_filter_generator,
    demonstrate_yield_basics,
    demonstrate_bidirectional_generator,
    demonstrate_yield_from_delegation,
    demonstrate_generator_vs_list_memory,
    demonstrate_range_generator_evolution,
    demonstrate_generator_attributes_and_dir,
)


class TestYieldGeneratorsTutorial:
    """Test suite covering generator functions, delegation, bidirectional communication, and memory metrics."""

    def test_count_up_generator_success(self):
        gen = count_up_generator(3)
        assert next(gen) == 1
        assert next(gen) == 2
        assert next(gen) == 3
        with pytest.raises(StopIteration) as exc_info:
            next(gen)
        assert exc_info.value.value == "Completed counting up to 3"

    def test_count_up_generator_invalid_input(self):
        with pytest.raises(TypeError):
            list(count_up_generator("invalid"))  # type: ignore
        with pytest.raises(ValueError):
            list(count_up_generator(-5))

    def test_fibonacci_generator(self):
        fib_items = list(fibonacci_generator(7))
        assert fib_items == [0, 1, 1, 2, 3, 5, 8]

    def test_fibonacci_generator_invalid_input(self):
        with pytest.raises(TypeError):
            list(fibonacci_generator(3.14))  # type: ignore
        with pytest.raises(ValueError):
            list(fibonacci_generator(-1))

    def test_interactive_accumulator(self):
        acc = interactive_accumulator_generator(10.0)
        assert next(acc) == 10.0
        assert acc.send(5.0) == 15.0
        assert acc.send(2.5) == 17.5
        acc.close()

    def test_interactive_accumulator_invalid_type(self):
        with pytest.raises(TypeError):
            gen = interactive_accumulator_generator("invalid_start")  # type: ignore
            next(gen)

    def test_delegating_generator_yield_from(self):
        gen = delegating_generator([10, 20], range(30, 32))
        assert list(gen) == [10, 20, 30, 31]

    def test_pipeline_filter_generator(self):
        data = [5, 12, 3, 20, 8, 15]
        res = list(pipeline_filter_generator(data, threshold=10))
        # 12 -> 24, 20 -> 40, 15 -> 30
        assert res == [24, 40, 30]

    def test_pipeline_filter_generator_invalid_input(self):
        with pytest.raises(TypeError):
            list(pipeline_filter_generator("not_a_list"))  # type: ignore

    def test_demonstrate_yield_basics(self):
        res = demonstrate_yield_basics(4)
        assert isinstance(res, dict)
        assert res["limit"] == 4
        assert res["is_generator_instance"] is True
        assert res["yielded_values"] == [1, 2, 3, 4]
        assert res["return_value_pep_380"] == "Completed counting up to 4"

    def test_demonstrate_bidirectional_generator(self):
        res = demonstrate_bidirectional_generator()
        assert isinstance(res, dict)
        assert res["initial_primed_value"] == 10.0
        assert res["after_send_5_5"] == 15.5
        assert res["after_send_20_0"] == 35.5
        assert res["caught_exception_on_bad_send"] == "Sent value must be a numeric integer or float"

    def test_demonstrate_yield_from_delegation(self):
        res = demonstrate_yield_from_delegation()
        assert isinstance(res, dict)
        assert res["flattened_yielded_elements"] == [1, 2, 3, 1, 2, 3, 10, 20]
        assert res["sub_iterable_lengths_returned"] == [3, 3, 2]

    def test_demonstrate_generator_vs_list_memory(self):
        res = demonstrate_generator_vs_list_memory(1000)
        assert isinstance(res, dict)
        assert res["element_count"] == 1000
        assert res["list_memory_bytes"] > res["generator_memory_bytes"]

    def test_demonstrate_generator_vs_list_memory_invalid_input(self):
        with pytest.raises(TypeError):
            demonstrate_generator_vs_list_memory(-10)
        with pytest.raises(TypeError):
            demonstrate_generator_vs_list_memory("invalid")  # type: ignore

    def test_demonstrate_range_generator_evolution(self):
        res = demonstrate_range_generator_evolution()
        assert isinstance(res, dict)
        assert "range_public_attributes" in res
        assert "__iter__" in res["range_key_dunders"]
        assert "python_version_notes" in res
        assert "python_3_13" in res["python_version_notes"]

    def test_demonstrate_generator_attributes_and_dir(self):
        res = demonstrate_generator_attributes_and_dir()
        assert isinstance(res, dict)
        assert "send" in res["generator_public_methods"]
        assert "close" in res["generator_public_methods"]
        assert "throw" in res["generator_public_methods"]
        assert "gi_code" in res["generator_internal_gi_attributes"]
        assert res["gi_code_name"] == "count_up_generator"
