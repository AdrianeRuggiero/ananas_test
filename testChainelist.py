import unittest
from chainelist import chainelist


# j'ai défini une classe TestChainelist qui hérite de unittest.TestCase
class TestChainelist(unittest.TestCase):
    # j'ai défini trois méthodes de test différentes
    def test_chainelist_doublon(self):
        # Cas de test avec des éléments en doublon
        input_list = ['a', 'b', 'a', 'c', 'b']
        result = chainelist(input_list)
        self.assertEqual(result, ['a', 'b', 'c'])

    def test_chainelist_vide(self):
        # Cas de test avec une liste vide
        input_list = []
        result = chainelist(input_list)
        self.assertEqual(result, [])

    def test_chainelist_mix_types(self):
        # Cas de test avec des chaînes de caractères et des nombres
        input_list = ['a', 1, 'b', 2, 'a']
        result = chainelist(input_list)
        self.assertEqual(result, ['a', 1, 'b', 2])


if __name__ == '__main__':
    # Création de la suite de tests
    suite = unittest.TestSuite()
    suite.addTest(TestChainelist('test_chainelist_doublon'))
    suite.addTest(TestChainelist('test_chainelist_vide'))
    suite.addTest(TestChainelist('test_chainelist_mix_types'))

    # Exécution des tests runner
    runner = unittest.TextTestRunner()
    runner.run(suite)
