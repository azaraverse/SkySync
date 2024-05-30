#!/usr/bin/python3
"""Unittest for file path"""
import unittest
import os


class TestFilePath(unittest.TestCase):
    """Unittest testcase for filepath."""
    def test_static_folder_path(self):
        """Test the filepath for the static folder."""
        current_dir = os.path.dirname(__file__)
        static_folder_path = os.path.join(
            current_dir, '..', 'app', 'static'
        )
        self.assertTrue(
            os.path.exists(static_folder_path),
            "Static folder path does not exist."
        )

    def test_template_folder_path(self):
        """Test the filepath for the template folder."""
        current_dir = os.path.dirname(__file__)
        template_folder_path = os.path.join(
            current_dir, '..', 'app', 'template'
        )
        self.assertTrue(
            os.path.exists(template_folder_path),
            "Template folder path does not exist."
        )


if __name__ == "__main__":
    unittest.main()
