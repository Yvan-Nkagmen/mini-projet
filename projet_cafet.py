def verifier_heure(heure):  #yvan
    """
    fonction qui sert a vérifier si la cafetéria est ouverte,
    si c'est l'heure du déjeuner ou diner
    :param heure: l'heure actuelle
    :return: ouvert ou fermé, déjeuner ou diner
    """
    if heure < 7 or heure >= 15:
        return "fermé"
    elif 7 <= heure < 10:
        return "dejeuner"
    else:
        return "diner"

def afficher_menu(menu):

    print("==== Menu de jour ====")


def choisir_plat():


def prendre_commande(): #Keysahwn
    while True:
        commande = input("Que voulez-vous dans votre commande si vous voulez arrêter pesez enter")
        list_commande = []
        list_commande.append(commande)
        if commande == "":
            print(f"Voici votre commande {list_commande}")
            break


def generer_facture(commande : list): #Keysahwn
    prix_tot = 0
    for i in commande:
        if i == "poulet rôti":
            prix_tot += 12
        elif i == "pâte alfredo":
            prix_tot += 10.5
        elif i == "crêpes":
            prix_tot += 5.5
        elif i == "omelette":
            prix_tot += 6
        elif i == "Tortilla aux œufs":
            prix_tot += 7
        elif i == "burger":
            prix_tot += 11




if __name__=="__main__":
    print("")
