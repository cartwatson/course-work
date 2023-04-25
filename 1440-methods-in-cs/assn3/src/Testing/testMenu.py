# Tests the Menu and MenuOption Classes

import unittest
import Menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu.Menu("Deck")
        self.menu.addOption("A", "Test option A")
        self.menu.addOption("B", "Test option B")
        self.menu.addOption("C", "Test option C")
        self.menu.addOption("D", "Test option D")
        self.menu.addOption("E", "Test option E")
        self.menu1 = Menu.Menu("")

    def test_addOption(self):
        menu = Menu.Menu("Test")
        menu.addOption("A", "Test option A")
        menu.addOption("", "")
        self.assertNotEqual(menu.getOptionCount(), 2)

    def test_getOption(self):
        MenuOption = self.menu.getOption(0)
        self.assertEqual(MenuOption.getCommand(), "A")
        self.assertEqual(MenuOption.getDescription(), "Test option A")
        MenuOption = self.menu.getOption(1)
        self.assertEqual(MenuOption.getCommand(), "B")
        self.assertEqual(MenuOption.getDescription(), "Test option B")
        MenuOption = self.menu.getOption(2)
        self.assertEqual(MenuOption.getCommand(), "C")
        self.assertEqual(MenuOption.getDescription(), "Test option C")
        MenuOption = self.menu.getOption(3)
        self.assertEqual(MenuOption.getCommand(), "D")
        self.assertEqual(MenuOption.getDescription(), "Test option D")
        MenuOption = self.menu.getOption(4)
        self.assertEqual(MenuOption.getCommand(), "E")
        self.assertEqual(MenuOption.getDescription(), "Test option E")

        self.assertIsNone(self.menu1.getOption(0))
        self.assertIsNone(self.menu1.getOption(-1))

    def test_getHeader(self):
        self.assertEqual(self.menu.getHeader(), "Deck")
        self.assertNotEqual(self.menu.getHeader(), "")
        self.assertEqual(self.menu1.getHeader(), "")
        self.assertNotEqual(self.menu1.getHeader(), "Deck")

    def test_getOptionCount(self):
        self.assertEqual(self.menu.getOptionCount(), 5)
        self.assertNotEqual(self.menu.getOptionCount(), 0)
        self.assertEqual(self.menu1.getOptionCount(), 0)
        self.assertNotEqual(self.menu1.getOptionCount(), 5)


if __name__ == '__main__':
    unittest.main()
