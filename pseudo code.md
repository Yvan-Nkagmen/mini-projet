FONCTION verifier_heure(heure)#yvan

    SI heure < 7 OU heure >= 15 ALORS
        RETOURNER "fermé"
    SINON SI heure >= 7 ET heure < 10 ALORS
        RETOURNER "déjeuner"
    SINON
        RETOURNER "dîner"
    FIN FONCTION

FONCTION obtenir_menu_du_jour(service, jour) #djawad

    SI service == "déjeuner" ALORS
        menus_du_dejeuner ← [
            ["Lundi": {"Crêpes": 5.5, "Oeufs brouillés": 6}],
            ["Mardi": {"Bagel": 4.5, "Smoothie": 5.0}],
            ... etc ...
        ]
        RETOURNER le menu correspondant au jour dans menus_du_dejeuner
    SINON
        menus_du_diner ← [
            ["Lundi": {"Poulet rôti": 12, "Pâtes Alfredo": 10.5}],
            ["Mardi": {"Burger": 11, "Soupe + sandwich": 8.5}],
            ... etc ...
        ]
        RETOURNER le menu correspondant au jour dans menus_du_diner
    
    FIN FONCTION
FONCTION afficher_menu(menu)#yvan

    POUR chaque plat, prix dans menu FAIRE
        AFFICHER plat + " - " + prix + "$"
    
    FIN FONCTION
FONCTION prendre_commande(menu)#keyshawn

    DEMANDER "Quel plat choisissez-vous ?"
    LIRE plat_choisi
    SI plat_choisi EXISTE dans les plats de menu ALORS
        prix ← menu[plat_choisi]
        RETOURNER (plat_choisi, prix)
    SINON
        AFFICHER "Ce plat n'existe pas dans le menu."
        RETOURNER AUCUN
    
    FIN FONCTION
FONCTION generer_facture(commande, caissier)#keyshawn

    AFFICHER "--- Facture ---"
    AFFICHER "Plat : " + commande.nom
    AFFICHER "Total à payer : " + commande.prix + "$"
    AFFICHER "Caissier : " + caissier
    FIN FONCTION
FONCTION afficher_message_fermeture()

    AFFICHER "La cafétéria est fermée. Heures d'ouverture : 7h à 15h"
    FIN FONCTION

AFFICHER_PERSONNEL()
    
    AFFICHER LE CUISINIER
    AFFICHER CAISSIER
FIN

OBTENIR_JOUR_ACTUEL()#YVAN

    AFFICHER QUEL JOUR SOMMES-NOUS
    LIRE JOUR
    JOUR = INPUT DE L'UTILISATEUR
FIN