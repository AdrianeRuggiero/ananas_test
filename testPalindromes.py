import unittest
from palindromes import compter_palindromes


class TestCompterPalindromes(unittest.TestCase):

    def test_compter_palindromes(self):
        # Cas de test d'une liste avec des palindromes et des non-palindromes
        input_list = ["radar", "level", "python", "stats", "racecar"]
        result = compter_palindromes(input_list)
        self.assertEqual(result, 4)

    def test_compter_palindromes_vide(self):
        # Cas de test d'une liste vide
        input_list = []
        result = compter_palindromes(input_list)
        self.assertEqual(result, 0)

    def test_compter_palindromes_tous_palindromes(self):
        # Cas de test d'une liste contenant que des palindromes
        input_list = ["radar", "level", "deed", "noon", "civic"]
        result = compter_palindromes(input_list)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    # Création de la suite de tests
    suite = unittest.TestSuite()
    suite.addTest(TestCompterPalindromes('test_compter_palindromes'))
    suite.addTest(TestCompterPalindromes('test_compter_palindromes_vide'))
    suite.addTest(
        TestCompterPalindromes('test_compter_palindromes_tous_palindromes')
    )

    # Exécution des tests runner
    runner = unittest.TextTestRunner()
    runner.run(suite)
