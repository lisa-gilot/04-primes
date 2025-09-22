"""
Module pour afficher les nombres premiers inférieurs à 100.
"""

from math import sqrt

def isprime(p):
    """
    Détermine si p (le nombre à tester) est un nombre est premier.
    Renvoie un booléen indiquant True si p est premier
    """
    if p < 2:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True


def main():
    """
    Affiche tous les nombres premiers inférieurs à 100.
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
        print()


if __name__ == "__main__":
    main()
