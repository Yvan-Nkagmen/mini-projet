import pytest
from projet_cafet import *


def test_dejeuner():#yvan
    assert verifier_heure(7) == "dejeuner"
    assert verifier_heure(8) == "dejeuner"
    assert verifier_heure(9) == "dejeuner"

def test_obtenir_jour_actuel():#yvan
    """

    """