import pytest
from projet_cafet import *


def test_dejeuner():#yvan
    assert verifier_heure(7) == "dejeuner"
    assert verifier_heure(8) == "dejeuner"
    assert verifier_heure(9) == "dejeuner"

def test_obtenir_jour_actuel():#yvan
    """

    """





def obtenir_menu_du_jour(service,jour):
    def test_menus(self):
        # Test du déjeuner
        menu_dejeuner = obtenir_menu_du_jour("dejeuner", "Lundi")
        self.assertIsInstance(menu_dejeuner, dict)

        # Test du dîner
        menu_diner = obtenir_menu_du_jour("diner", "Lundi")
        self.assertisinstance(menu_diner, dict)


