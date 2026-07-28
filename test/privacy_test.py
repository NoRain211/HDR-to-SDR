import os
import unittest


class TestDesktopPrivacy(unittest.TestCase):
    """Keep automatic network clients out of the desktop application."""

    def test_production_source_has_no_telemetry_clients(self) -> None:
        src_dir = os.path.join(os.path.dirname(__file__), '..', 'src')
        forbidden = (
            'activate_license',
            'check_for_update',
            'lemonsqueezy',
            'license_api_endpoint',
            'urllib.request',
            'urlopen(',
        )

        matches: list[str] = []
        for name in os.listdir(src_dir):
            if not name.endswith(('.py', '.pyw')):
                continue
            path = os.path.join(src_dir, name)
            with open(path, encoding='utf-8') as source_file:
                source = source_file.read().lower()
            for marker in forbidden:
                if marker in source:
                    matches.append(f'{name}: {marker}')

        self.assertEqual(matches, [])


if __name__ == '__main__':
    unittest.main()
