def trouver_le_plus_grand(nombre1, nombre2, nombre3):
    if nombre1 >= nombre2 and nombre1 >= nombre3:
        return nombre1
    elif nombre2 >= nombre1 and nombre2 >= nombre3:
        return nombre2
    else:
        return nombre3

# je demande a l'utilisateur de rentrer les valeur a tester
"""""nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
nombre3 = float(input("Entrez le troisième nombre : "))"""""

import unittest

class TestTrouverLePlusGrand(unittest.TestCase):

    def test_trouver_le_plus_grand(self):
        self.assertEqual(trouver_le_plus_grand(9, 99, 103), 103)
        self.assertEqual(trouver_le_plus_grand(10, 10.1, 3), 10.1)
        self.assertEqual(trouver_le_plus_grand(-1, -2, -3), -1)
        self.assertEqual(trouver_le_plus_grand(0, 0, 0), 0)
        self.assertEqual(trouver_le_plus_grand(5, 5, 2), 5)
        self.assertEqual(trouver_le_plus_grand(2, 3, 2), 3)

if __name__ == '__main__':
    unittest.main()