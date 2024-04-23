import unittest

def etudiants_avec_bonne_note(etudiants):
    etudiants_bons = {}
    for nom, note in etudiants.items():
        if note >= 15:
            etudiants_bons[nom] = note
    return etudiants_bons

class TestEtudiantsAvecBonneNote(unittest.TestCase):
    
    def test_etudiants_avec_bonne_note(self):
        etudiants_notes = {
            "bomarl": 17,
            "weedman": 14,
            "Snoopy": 16,
            "Wizzou": 13,
            "Picsous": 18
        }
        resultat_attendu = {
            "bomarl": 17,
            "Snoopy": 16,
            "Picsous": 18
        }
        resultat_obtenu = etudiants_avec_bonne_note(etudiants_notes)
        self.assertEqual(resultat_obtenu, resultat_attendu)


if __name__ == '__main__':
    unittest.main()
