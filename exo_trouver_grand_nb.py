# Demande à l'utilisateur de saisir trois nombres
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
nombre3 = float(input("Entrez le troisième nombre : "))

# Vérifie le plus grand nombre
if nombre1 >= nombre2 and nombre1 >= nombre3: #je compare la premiere valeur avec les autre valeur
    plus_grand = nombre1
elif nombre2 >= nombre1 and nombre2 >= nombre3:# la deuxieme valeur avec le reste
    plus_grand = nombre2
else:
    plus_grand = nombre3 # si aucune des deux autre valeurs est plus plus grand que nb3 alros nb 3 est le plus grand 

# mtn faut afffichew
print("Le plus grand nombre parmi", nombre1, ",", nombre2, "et", nombre3, "est :", plus_grand)