""" Retourne une liste contenant les éléments uniques de la liste d'entrée."""


def chainelist(list):
    # creation d'une nouvelle list
    listFinal = []
    # parcourir la liste initiale
    for elt in list:
        # si l'element de la liste initial n'existe pas dans la nouvelle list
        if elt not in listFinal:
            # on ajoute l'element dans la nouvelle liste
            listFinal.append(elt)
    return listFinal

#pour distinguer le code qui doit être exécuté
if __name__ == '__main__':
    # Demander à l'utilisateur d'entrer une liste
    user_input = input("entrer une liste : ")
    user_list = user_input.split()

    # Appeler la fonction et afficher le résultat
    result = chainelist(user_list)
    print(f"votre liste unique est: {result}")
