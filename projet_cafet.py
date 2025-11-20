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



def obtenir_menu_du_jour(service, jour): #djawad
    if service=="dejeuner":
        menus_du_dejeuner = [
        ["Lundi": {"Crêpes": 5.5, "Omelette": 6}],
        ["Mardi": {"Bagel": 4.5, "Smoothie": 5.0}],
        ["Mercredi": {"pain": 3.5, "jus d'orange": 3.0}],
        ["jeudi":{"croissant": 3.5, "café": 4.0}],
        ["vendredi": {"céréales": 5.0, "pomme": 2.0}]
    ]
        return menus_du_dejeuner
    else:
        menus_du_diner = [
            ["Lundi": {"Poulet rôti": 12, "Pâtes Alfredo": 10.5}],
            ["Mardi": {"Burger": 11, "Soupe + sandwich": 8.5}],
            ["Mercredi": {"poulet au curry"}]
        ]












def afficher_menu(menu): #yvan
    """
    affiche le menu du jour avec les plats et les prix.
    :param menu: dictionnaire contenant les plats
    :return:
    """
    print("==== Menu de jour ====")
    for  plat, prix in menu.items():
        print(plat,"-",prix,"$")


def prendre_commande(): #Keyshawn
    while True:
        commande = input("Que voulez-vous dans votre commande si vous voulez arrêter pesez enter")
        list_commande = []
        list_commande.append(commande)
        if commande == "":
            print(f"Voici votre commande {list_commande}")
            break


def generer_facture(commande : list): #Keyshawn
    prix_tot = 0
    for i in commande:
        if i == "poulet rôti":
            prix_tot += 12
        elif i == "pâte alfredo":
            prix_tot += 10.5
        elif i == "Tortilla aux œufs":
            prix_tot += 7
        elif i == "burger":
            prix_tot += 11
        elif i==





        elif i == "crêpes":
            prix_tot += 5.5
        elif i == "omelette":
            prix_tot += 6
        elif i == "Bagel":
            prix_tot +=4.5
        elif i== "Smoothie":
            prix_tot += 5.0
        elif i== "pain":
            prix_tot += 3.5
        elif i== "jus d'orange":
            prix_tot += 3.0
        elif i== "croissant":
             prix_tot += 3.5
        elif i== "café":
             prix_tot += 4.0
        elif i== "céréales":
            prix_tot +=5.0
        elif i== "pomme":
            prix_tot += 2.0

def afficher_message_fermeture(): #Yvan
    """
    Affiche un message indiquant que la cafétéria est fermée.
    :return: None
    """

    print("La cafétéria est fermée. Heures d'ouverture : 7h à 15h")

def afficher_personnel(): #Djawad
    """
    Affiche la liste du personnel présent.
    :return: None
    """

    print("Cuisinier")
    print("Caissier")






def obtenir_jour_actuel(): #yvan
    """
    demande à l'utilisateur le jour de la semaine.
    :return: le jour de la semaine
    """
    jour = input("quel jour de la semaine sommes-nous? (lundi à vendredi?): ").lower()
    return jour

if __name__ == "__main__":
        print("Bienvenue à la cafétéria !")

        # Choisir personnel(djawad)
        cuisinier = input("Nom du cuisinier : ")
        caissier = input("Nom du caissier : ")
        afficher_personnel(cuisinier, caissier)

        # Obtenir heure valide(yvan)
        while True:
            try:
                heure = int(input("Entrez l'heure actuelle (0-23) : "))
                if 0 <= heure <= 23:
                    break
                else:
                    print("L'heure doit être entre 0 et 23.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entier.")

        service = verifier_heure(heure)

        if service == "fermé":
            afficher_message_fermeture()
        else:
            print(f"Service actuel : {service}")
            jour = obtenir_jour_actuel()
            menu = obtenir_menu_du_jour(service, jour)

            if not menu:
                print(f"Aucun menu disponible pour {jour}.")
            else:
                afficher_menu(menu)

                # Boucle commandes(keyshawn)
                commandes = []
                while True:
                    commande = prendre_commande(menu)
                    commandes.append(commande)

                    continuer = input("Voulez-vous commander un autre plat ? (oui/non) : ").lower()
                    if continuer != "oui":
                        break

                # Modifier ou supprimer commandes si besoin
                commandes = modifier_commandes(commandes, menu)

                # Générer la facture finale
                generer_facture(commandes, caissier, cuisinier)
