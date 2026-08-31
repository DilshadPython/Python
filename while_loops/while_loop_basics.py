# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import sys: Standard library module for interpreter parameters and maxsize checks.
# - import itertools: Standard library module for predicate iterator filtering (takewhile, dropwhile).
# - import time: High-resolution performance timer benchmarking for loop execution.
# - from typing import Dict, List, Any, Tuple, Optional, Union: PEP 484 type annotations.
# =========================================================================
import itertools
import sys
import time
from typing import Any, Dict, List, Optional, Tuple, Union

Number = Union[int, float]


def starter_while_loop_examples() -> Dict[str, Any]:
    """Starter examples demonstrating count-controlled and dual-variable while loops.
    
    Inspired by DilshadPython/Python/While-loop scripts:
    - while_count_control.py
    - while_decrease_counter.py
    - while_ascending_descending.py
    - while_dual_variable.py
    """
    # Count-controlled increment
    counter = 0
    count_list: List[int] = []
    while counter < 5:
        count_list.append(counter)
        counter += 1

    # Count-controlled decrement
    countdown = 5
    countdown_list: List[int] = []
    while countdown > 0:
        countdown_list.append(countdown)
        countdown -= 1

    # Dual-variable simultaneous increment and decrement
    x, y = 0, 10
    dual_steps: List[Tuple[int, int]] = []
    while x < 5 and y > 5:
        dual_steps.append((x, y))
        x += 1
        y -= 1

    # Accumulator sum
    total_sum = 0
    num = 1
    while num <= 10:
        total_sum += num
        num += 1

    return {
        "counter_sequence": count_list,
        "countdown_sequence": countdown_list,
        "dual_variable_steps": dual_steps,
        "accumulated_sum": total_sum,
        "final_counter_value": counter,
    }


def interactive_and_event_controlled_loops(
    quiz_guesses: List[int],
    pet_guesses: List[str],
    calc_op: Tuple[float, float, str],
) -> Dict[str, Any]:
    """Demonstrates event-controlled loops, sentinel evaluation, and interactive logic.
    
    Inspired by DilshadPython/Python/While-loop scripts:
    - while_company_quiz.py
    - while_guess_pet.py
    - while_calculator.py
    """
    if not isinstance(quiz_guesses, list):
        raise TypeError("Input 'quiz_guesses' must be a valid Python list")
    if not isinstance(pet_guesses, list):
        raise TypeError("Input 'pet_guesses' must be a valid Python list")

    # 1. Company Quiz Evaluation Logic (while_company_quiz.py)
    quiz_attempts = 0
    quiz_success = False
    quiz_message = "No choices provided"
    idx = 0
    while idx < len(quiz_guesses) and quiz_attempts < 3:
        guess = quiz_guesses[idx]
        quiz_attempts += 1
        idx += 1
        if guess == 1:
            quiz_success = True
            quiz_message = "Correct! The company is Google."
            break
        elif guess == 3:
            quiz_success = False
            quiz_message = "Sorry, your guess was wrong. The answer was Google."
            break
        else:
            if quiz_attempts >= 3:
                quiz_message = "Maximum attempts reached."

    # 2. Pet Name Guessing Logic (while_guess_pet.py)
    pet_attempts = 0
    pet_found = False
    idx = 0
    while idx < len(pet_guesses):
        ans = pet_guesses[idx].strip()
        pet_attempts += 1
        idx += 1
        if ans == "Raffi":
            pet_found = True
            break

    # 3. Arithmetic Calculator Logic (while_calculator.py)
    v1, v2, op = calc_op
    calc_result: Union[float, str]
    if op == "+":
        calc_result = v1 + v2
    elif op == "-":
        calc_result = v1 - v2
    elif op == "*":
        calc_result = v1 * v2
    elif op == "/":
        calc_result = v1 / v2 if v2 != 0 else "Error: Division by zero"
    else:
        calc_result = "Error: Unrecognized operator"

    return {
        "quiz_success": quiz_success,
        "quiz_attempts": quiz_attempts,
        "quiz_message": quiz_message,
        "pet_found": pet_found,
        "pet_attempts": pet_attempts,
        "calc_result": calc_result,
    }


def state_flags_and_accumulators(target_sum: int = 24) -> Dict[str, Any]:
    """Demonstrates boolean state flags (keep_going) and step accumulator tracking.
    
    Inspired by DilshadPython/Python/While-loop scripts:
    - while_boolean_accumulator.py
    - while_early_check_accumulator.py
    - while_trajectory_status.py
    """
    if not isinstance(target_sum, int) or target_sum <= 0:
        raise TypeError("Input 'target_sum' must be a positive integer")

    # Boolean flag step accumulator (5 and 7 increments)
    keep_going = True
    a, b = 0, 0
    accumulation_history: List[Tuple[int, int, int]] = []

    while keep_going:
        a += 5
        b += 7
        total = a + b
        accumulation_history.append((a, b, total))
        if total >= target_sum:
            keep_going = False

    # Trajectory status tracker (while_trajectory_status.py)
    pos = 0
    trajectory: List[int] = []
    status_active = True
    while status_active and pos < 50:
        pos += 12
        trajectory.append(pos)
        if pos >= 36:
            status_active = False

    return {
        "accumulation_history": accumulation_history,
        "final_total": accumulation_history[-1][2] if accumulation_history else 0,
        "trajectory": trajectory,
        "status_active": status_active,
    }


def loop_control_and_sentinels(
    numbers: List[int], stop_val: int = -1
) -> Dict[str, Any]:
    """Demonstrates loop control keywords ('break', 'continue') and 'while-else' behavior.
    
    Inspired by DilshadPython/Python/While-loop scripts:
    - while_break_sentinel.py
    - while_continue_division.py
    - while_true_threshold.py
    """
    if not isinstance(numbers, list):
        raise TypeError("Input 'numbers' must be a valid Python list")

    # 1. Break on Sentinel Value (-1) (while_break_sentinel.py)
    idx = 0
    collected_before_sentinel: List[int] = []
    hit_sentinel = False
    while idx < len(numbers):
        curr = numbers[idx]
        if curr == stop_val:
            hit_sentinel = True
            break
        collected_before_sentinel.append(curr)
        idx += 1

    # 2. Continue to Skip Division by Zero (while_continue_division.py)
    idx = 0
    valid_division_results: List[float] = []
    skipped_zero_count = 0
    while idx < len(numbers):
        curr = numbers[idx]
        idx += 1
        if curr == 0:
            skipped_zero_count += 1
            continue
        valid_division_results.append(round(100.0 / curr, 2))

    # 3. While-Else Execution Flag
    idx = 0
    else_executed = False
    while idx < len(numbers):
        if numbers[idx] == -99999:  # Unreachable sentinel
            break
        idx += 1
    else:
        else_executed = True

    return {
        "collected_before_sentinel": collected_before_sentinel,
        "hit_sentinel": hit_sentinel,
        "valid_division_results": valid_division_results,
        "skipped_zero_count": skipped_zero_count,
        "else_executed": else_executed,
    }


def process_while_loop_with_standard_libraries(items: List[int]) -> Dict[str, Any]:
    """Integrates itertools.takewhile, itertools.dropwhile, and sys parameters.
    
    Inspired by DilshadPython/Python/While-loop scripts:
    - while_read_file_average.py
    - while_modulus_sequence.py
    """
    if not isinstance(items, list):
        raise TypeError("Input 'items' must be a valid Python list")

    take_even = list(itertools.takewhile(lambda x: x % 2 == 0, items))
    drop_even = list(itertools.dropwhile(lambda x: x % 2 == 0, items))

    iterator = iter(items)
    manual_while_extracted: List[int] = []
    while True:
        try:
            val = next(iterator)
            manual_while_extracted.append(val * 10)
        except StopIteration:
            break

    return {
        "takewhile_even": take_even,
        "dropwhile_even": drop_even,
        "manual_iterator_extraction": manual_while_extracted,
        "interpreter_maxsize": sys.maxsize,
    }
