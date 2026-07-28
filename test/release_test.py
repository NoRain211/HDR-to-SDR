import os
import re
import unittest

from src.version import APP_VERSION


class TestReleaseMetadata(unittest.TestCase):
    def setUp(self) -> None:
        root = os.path.join(os.path.dirname(__file__), '..')
        with open(os.path.join(root, 'installer.iss'), encoding='utf-8') as installer_file:
            self.installer = installer_file.read()

    def test_app_and_installer_versions_match(self) -> None:
        match = re.search(r'#define AppVersion\s+"([^"]+)"', self.installer)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), APP_VERSION)

    def test_installer_has_no_update_endpoint(self) -> None:
        self.assertNotIn('AppUpdatesURL', self.installer)


if __name__ == '__main__':
    unittest.main()
