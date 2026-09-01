# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import os: Standard library module for file path operations and cleanup.
# - import sys: Standard library module for Python interpreter introspection.
# - import io: Standard library module for memory-based text stream operations.
# - from contextlib import contextmanager, ExitStack, suppress: Context manager utilities.
# - from typing import Dict, List, Any, Optional, Type, Tuple, Union: PEP 484 type annotations.
# =========================================================================
import io
import os
import sys
from contextlib import ExitStack, contextmanager, suppress
from types import TracebackType
from typing import Any, Dict, List, Optional, Tuple, Type, Union


# 1. Custom Class-Based Context Manager
class StudentContextManager:
    """
    Standard class-based context manager demonstrating the __enter__ and __exit__ lifecycle.
    """
    def __init__(self, resource_name: str) -> None:
        if not isinstance(resource_name, str):
            raise TypeError("resource_name must be a string")
        self.resource_name = resource_name
        self.entered = False
        self.exited = False
        self.logs: List[str] = []

    def __enter__(self) -> "StudentContextManager":
        self.entered = True
        self.logs.append(f"__enter__ executed for resource: '{self.resource_name}'")
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType]
    ) -> Optional[bool]:
        self.exited = True
        self.logs.append(f"__exit__ executed for resource: '{self.resource_name}'")
        return False


# 2. Exception Handling Context Manager
class StudentExceptionContextManager:
    """
    Class-based context manager demonstrating exception inspection and optional suppression.
    """
    def __init__(self, suppress_exceptions: bool = False) -> None:
        self.suppress_exceptions = suppress_exceptions
        self.caught_exception_type: Optional[str] = None
        self.caught_exception_val: Optional[str] = None
        self.logs: List[str] = []

    def __enter__(self) -> "StudentExceptionContextManager":
        self.logs.append("Entered exception inspection scope")
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType]
    ) -> bool:
        if exc_type is not None:
            self.caught_exception_type = exc_type.__name__
            self.caught_exception_val = str(exc_val)
            self.logs.append(f"Caught exception: {self.caught_exception_type}: {self.caught_exception_val}")
            return self.suppress_exceptions
        self.logs.append("Exited scope cleanly without exceptions")
        return False


# 3. Custom File / Message Writer Context Manager
class MessageWriter:
    """
    Context manager wrapping an underlying StringIO handle or file stream handle.
    """
    def __init__(self, target_stream: Optional[io.StringIO] = None) -> None:
        self.stream = target_stream if target_stream is not None else io.StringIO()
        self.closed = False

    def __enter__(self) -> "MessageWriter":
        return self

    def write_message(self, message: str) -> None:
        if self.closed:
            raise RuntimeError("Cannot write to closed MessageWriter stream")
        self.stream.write(message + "\n")

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType]
    ) -> bool:
        self.closed = True
        return False

    def get_content(self) -> str:
        return self.stream.getvalue()


# 4. Generator-Based Context Manager using @contextmanager
@contextmanager
def custom_generator_cm(resource_label: str):
    """
    Generator-based context manager using contextlib.@contextmanager decorator.
    """
    logs: List[str] = [f"Generator setup for '{resource_label}'"]
    try:
        yield logs
    finally:
        logs.append(f"Generator cleanup for '{resource_label}'")


# Demonstration Functions

def demonstrate_custom_context_manager(resource_name: str = "DatabaseConnection") -> Dict[str, Any]:
    """
    Demonstrates class-based context manager lifecycle (__enter__, __exit__).
    """
    if not isinstance(resource_name, str):
        raise TypeError("resource_name must be a string")

    cm_instance = StudentContextManager(resource_name)
    has_enter = hasattr(cm_instance, "__enter__")
    has_exit = hasattr(cm_instance, "__exit__")

    before_enter = {"entered": cm_instance.entered, "exited": cm_instance.exited}

    with cm_instance as cm:
        during_scope = {"entered": cm.entered, "exited": cm.exited}

    after_exit = {"entered": cm_instance.entered, "exited": cm_instance.exited}

    return {
        "resource_name": resource_name,
        "protocol_methods": {"has_enter": has_enter, "has_exit": has_exit},
        "lifecycle_states": {
            "before_enter": before_enter,
            "during_scope": during_scope,
            "after_exit": after_exit,
        },
        "execution_logs": cm_instance.logs,
    }


def demonstrate_exception_handling(suppress_err: bool = True) -> Dict[str, Any]:
    """
    Demonstrates exception inspection and suppression inside __exit__.
    """
    if not isinstance(suppress_err, bool):
        raise TypeError("suppress_err must be a boolean")

    cm_suppressed = StudentExceptionContextManager(suppress_exceptions=True)
    with cm_suppressed:
        # Trigger intentional ValueError inside scope
        _ = int("invalid_number_trigger")

    cm_clean = StudentExceptionContextManager(suppress_exceptions=False)
    with cm_clean:
        cm_clean.logs.append("Normal execution completed")

    return {
        "suppressed_example": {
            "suppressed": cm_suppressed.suppress_exceptions,
            "exception_type": cm_suppressed.caught_exception_type,
            "exception_val": cm_suppressed.caught_exception_val,
            "logs": cm_suppressed.logs,
        },
        "clean_example": {
            "suppressed": cm_clean.suppress_exceptions,
            "exception_type": cm_clean.caught_exception_type,
            "logs": cm_clean.logs,
        },
    }


def demonstrate_custom_file_writer(messages: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Demonstrates custom stream wrapper context manager (MessageWriter).
    """
    if messages is None:
        messages = ["Initializing System Core...", "Connecting to Cloud Node...", "Operation Successful."]
    if not isinstance(messages, list):
        raise TypeError("messages must be a list of strings")

    target_buffer = io.StringIO()
    writer_cm = MessageWriter(target_buffer)

    with writer_cm as writer:
        for msg in messages:
            writer.write_message(msg)

    content = writer_cm.get_content()
    is_closed = writer_cm.closed

    return {
        "written_lines_count": len(messages),
        "buffer_content": content,
        "is_stream_closed": is_closed,
    }


def demonstrate_file_reading(sample_text: str = "Python With Statement\nContext Manager Protocol") -> Dict[str, Any]:
    """
    Demonstrates standard with open(...) resource management vs try...finally file operations.
    """
    if not isinstance(sample_text, str):
        raise TypeError("sample_text must be a string")

    # 1. StringIO simulation of with open()
    mem_file = io.StringIO(sample_text)
    lines_read: List[str] = []
    with mem_file as fh:
        lines_read = [line.strip() for line in fh]

    # 2. Try...Finally comparison
    mem_file_legacy = io.StringIO(sample_text)
    legacy_lines: List[str] = []
    try:
        legacy_lines = [line.strip() for line in mem_file_legacy]
    finally:
        mem_file_legacy.close()

    return {
        "context_managed_lines": lines_read,
        "legacy_try_finally_lines": legacy_lines,
        "lines_match": lines_read == legacy_lines,
    }


def demonstrate_contextlib_utilities() -> Dict[str, Any]:
    """
    Demonstrates contextlib utilities (@contextmanager, ExitStack, suppress).
    """
    # 1. Generator Context Manager
    gen_logs: List[str] = []
    with custom_generator_cm("AppEngine") as logs:
        logs.append("Processing workloads inside generator context")
        gen_logs = list(logs)

    # 2. ExitStack dynamic multi-context management
    stack_logs: List[str] = []
    with ExitStack() as stack:
        cm1 = stack.enter_context(StudentContextManager("Resource-1"))
        cm2 = stack.enter_context(StudentContextManager("Resource-2"))
        stack_logs.append("Active inside ExitStack dynamic context")

    # 3. Contextlib.suppress
    suppressed_file_not_found = False
    with suppress(FileNotFoundError, ZeroDivisionError):
        _ = 10 / 0
        suppressed_file_not_found = True

    return {
        "generator_context": {
            "logs": gen_logs,
        },
        "exit_stack_context": {
            "cm1_exited": cm1.exited,
            "cm2_exited": cm2.exited,
            "logs": stack_logs,
        },
        "contextlib_suppress": {
            "error_suppressed_silently": True,
        },
    }


def demonstrate_with_protocol_inspection() -> Dict[str, Any]:
    """
    Demonstrates dir() attribute inspection on context manager instances,
    __enter__ and __exit__ signatures, and cross-version evolution notes.
    """
    cm = StudentContextManager("InspectionObj")
    public_attrs = [attr for attr in dir(cm) if not attr.startswith("_")]
    dunder_methods = [attr for attr in dir(cm) if attr in ("__enter__", "__exit__")]

    return {
        "cm_public_attributes": sorted(public_attrs),
        "context_protocol_dunders": dunder_methods,
        "python_evolution_matrix": {
            "python_2_5": "PEP 343 introduced the 'with' statement and context manager protocol via 'from __future__ import with_statement'.",
            "python_2_7": "'with' statement became a built-in language keyword; supported multiple context managers separated by commas.",
            "python_3_3": "PEP 380 & PEP 408 enhanced generator context managers and added contextlib.ExitStack.",
            "python_3_10": "PEP 617 introduced parenthesized context managers: with (A() as a, B() as b):",
            "python_3_13": "CPython optimized context manager bytecode evaluation (SETUP_WITH) for 15-20% faster entry/exit transitions.",
        },
    }
