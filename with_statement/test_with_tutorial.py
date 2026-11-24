import io
import unittest
from cloud_app.tutorials.with_basics import (
    StudentContextManager,
    StudentExceptionContextManager,
    MessageWriter,
    custom_generator_cm,
    demonstrate_custom_context_manager,
    demonstrate_exception_handling,
    demonstrate_custom_file_writer,
    demonstrate_file_reading,
    demonstrate_contextlib_utilities,
    demonstrate_with_protocol_inspection,
)


class TestWithTutorial(unittest.TestCase):
    def test_student_context_manager(self):
        cm = StudentContextManager("TestResource")
        self.assertFalse(cm.entered)
        self.assertFalse(cm.exited)
        with cm as resource:
            self.assertEqual(resource, cm)
            self.assertTrue(cm.entered)
            self.assertFalse(cm.exited)
        self.assertTrue(cm.entered)
        self.assertTrue(cm.exited)
        self.assertEqual(len(cm.logs), 2)

    def test_student_context_manager_invalid_type(self):
        with self.assertRaises(TypeError):
            StudentContextManager(123)

    def test_demonstrate_custom_context_manager(self):
        res = demonstrate_custom_context_manager("CloudDatabase")
        self.assertEqual(res["resource_name"], "CloudDatabase")
        self.assertTrue(res["protocol_methods"]["has_enter"])
        self.assertTrue(res["protocol_methods"]["has_exit"])
        self.assertTrue(res["lifecycle_states"]["after_exit"]["exited"])

    def test_demonstrate_custom_context_manager_invalid_type(self):
        with self.assertRaises(TypeError):
            demonstrate_custom_context_manager(None)

    def test_demonstrate_exception_handling(self):
        res = demonstrate_exception_handling(suppress_err=True)
        self.assertEqual(res["suppressed_example"]["exception_type"], "ValueError")
        self.assertTrue(res["suppressed_example"]["suppressed"])
        self.assertIsNone(res["clean_example"]["exception_type"])

    def test_demonstrate_exception_handling_invalid_type(self):
        with self.assertRaises(TypeError):
            demonstrate_exception_handling(suppress_err="invalid")

    def test_message_writer(self):
        buf = io.StringIO()
        with MessageWriter(buf) as writer:
            writer.write_message("Line 1")
            writer.write_message("Line 2")
        self.assertEqual(buf.getvalue(), "Line 1\nLine 2\n")

    def test_message_writer_closed_error(self):
        writer = MessageWriter()
        with writer:
            writer.write_message("Inside")
        with self.assertRaises(RuntimeError):
            writer.write_message("Outside closed stream")

    def test_demonstrate_custom_file_writer(self):
        res = demonstrate_custom_file_writer(["Msg A", "Msg B"])
        self.assertEqual(res["written_lines_count"], 2)
        self.assertIn("Msg A", res["buffer_content"])
        self.assertTrue(res["is_stream_closed"])

    def test_demonstrate_custom_file_writer_invalid_type(self):
        with self.assertRaises(TypeError):
            demonstrate_custom_file_writer("Not a list")

    def test_demonstrate_file_reading(self):
        res = demonstrate_file_reading("Hello\nWorld")
        self.assertEqual(res["context_managed_lines"], ["Hello", "World"])
        self.assertTrue(res["lines_match"])

    def test_demonstrate_file_reading_invalid_type(self):
        with self.assertRaises(TypeError):
            demonstrate_file_reading(12345)

    def test_demonstrate_contextlib_utilities(self):
        res = demonstrate_contextlib_utilities()
        self.assertIn("Processing workloads", res["generator_context"]["logs"][1])
        self.assertTrue(res["exit_stack_context"]["cm1_exited"])
        self.assertTrue(res["exit_stack_context"]["cm2_exited"])
        self.assertTrue(res["contextlib_suppress"]["error_suppressed_silently"])

    def test_demonstrate_with_protocol_inspection(self):
        res = demonstrate_with_protocol_inspection()
        self.assertIn("__enter__", res["context_protocol_dunders"])
        self.assertIn("__exit__", res["context_protocol_dunders"])
        self.assertIn("python_3_13", res["python_evolution_matrix"])


if __name__ == "__main__":
    unittest.main()
