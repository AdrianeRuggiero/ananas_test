def etudiants_avec_bonne_note(etudiants):
    
    
    
    #ici  cree une fonction qui  paramettre un dictionnaire 
    etudiants_bons = {}
    for nom, note in etudiants.items():
        if note >= 15:
            etudiants_bons[nom] = note
    return etudiants_bons

#list etudiant 
etudiants_notes = {
    "bomarl": 17,
    "weedman": 14,
    "Snoopy": 16,
    "Wizzou": 13,
    "Picsous": 18
}

etudiants_bons_notes = etudiants_avec_bonne_note(etudiants_notes)
print("Étudiants avec une note moyenne supérieure ou égale à 15 :", etudiants_bons_notes)