import pathlib
import unittest


class TestNavigation(unittest.TestCase):
    def test_main_route_is_correct(self):
        source = (
            pathlib.Path(__file__).resolve().parents[1]
            / "src" / "streckenuebersicht" / "main" / "main.py"
        ).read_text(encoding="utf-8")

        self.assertIn('"/bicycle"', source)
        self.assertNotIn('"/bicyle"', source)
        self.assertTrue(
            'from .main_menu import MainMenuView' in source
            or 'from main_menu import MainMenuView' in source
        )


if __name__ == "__main__":
    unittest.main()
