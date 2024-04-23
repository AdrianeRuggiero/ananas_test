import unittest
from unittest.mock import patch
from chainelist import chainelist

class TestChainelist(unittest.TestCase):
    # mocker la fonction input, (input fonction dans le module builtins).
    @patch('builtins.input', return_value='a b a c b')

    def test_chainelist_doublon(self, mock_input):
        
        input_list = ['a', 'b', 'a', 'c', 'b']
        result = chainelist(input_list)
        # Vérification que la fonction retourne la liste avec des éléments uniques
        self.assertEqual(result, ['a', 'b', 'c'])

    @patch('builtins.input', return_value='')    
    def test_chainelist_vide(self, mock_input):
        
        input_list = []
        result = chainelist(input_list)
        # Vérification que la fonction retourne une liste vide
        self.assertEqual(result, [])

    @patch('builtins.input', return_value='a 1 b 2 a')    
    def test_chainelist_mix_types(self, mock_input):
        
        input_list = ['a', 1, 'b', 2, 'a']
        result = chainelist(input_list)
        
        self.assertEqual(result, ['a', 1, 'b', 2])

if __name__ == '__main__':
    # Création de la suite de tests
    suite = unittest.TestSuite()
    suite.addTest(TestChainelist('test_chainelist_doublon'))
    suite.addTest(TestChainelist('test_chainelist_vide'))
    suite.addTest(TestChainelist('test_chainelist_mix_types'))

    # Exécution des tests avec le runner
    runner = unittest.TextTestRunner()
    runner.run(suite)
