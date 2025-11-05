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


def generer_facture():


if__name__=="__main__":