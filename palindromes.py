def compter_palindromes(liste_mots):
    # Initialise le compteur pour les palindromes
    nb_palindromes = 0

    # Parcourt chaque mot dans la liste
    for mot in liste_mots:
        # Vérifie si le mot est égal à son inversion (palindrome)
        if mot == mot[::-1]:
            # Si c'est le cas, incrémente le compteur de palindromes
            nb_palindromes += 1

    # Retourne le nombre de palindromes trouvés dans la liste
    return nb_palindromes


# Liste de mots à vérifier
liste_mots = ["radar", "level", "python", "stats", "racecar"]

# Appel de la fonction pour compter les palindromes dans la liste
nb_palindromes = compter_palindromes(liste_mots)

# Affiche le nombre de palindromes dans la liste
print("Nombre de palindromes dans la liste :", nb_palindromes)
