import unittest

from secret_santa import secret_santa as run


class TestSecretSanta(unittest.TestCase):
    def test_empty(self ):
        with self.assertRaises(Exception):
            run()
        with self.assertRaises(Exception):
            run([])
        with self.assertRaises(Exception):
            run(["joey"])

    def test_two(self):
        result = run(["joey", "john"])
        joey = self.find_name('joey', result)
        john = self.find_name('john', result)
        self.assertIsNotNone(joey)
        self.assertIsNotNone(john)

    def test_large(self):
        names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        result = run(names)
        for person in result:
            self.assertIsNotNone(person)
            self.assertIsNotNone(person.send_to)
            self.assertIsNotNone(person.receive_from)

    @staticmethod
    def find_name(name, l):
        return next((p for p in l if p.name == name), None)


if __name__ == "__main__":
    unittest.main()
