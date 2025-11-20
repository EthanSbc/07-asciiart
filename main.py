"""
Ce module impplémente 2 fonction qui retournent de l'artcode
Une des fonctions est itérative, l'autre est récursive
elles sont ensuite appelé dans le main()
"""

#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant 
    une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if len(s) == 0:
        return []
    f = []
    cpt = 1
    for lettre in range(1, len(s)):
        if s[lettre] == s[lettre -1]:
            cpt += 1
        if s[lettre] != s[lettre -1] :
            f.append((s[lettre-1],cpt))
            cpt = 1
    f.append((s[-1], cpt))
    return f


def artcode_r(s):
    """retourne la liste de tuples encodant 
    une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    if not s:
        return []

    # Compter les occurrences du premier caractère
    pre = s[0]
    cpt = 1
    i = 1
    while i < len(s) and s[i] == pre:
        cpt += 1
        i += 1

    # Appel récursif sur le reste
    return [(pre, cpt)] + artcode_r(s[cpt:])
#### Fonction principale
def main():
    """
    le main qui appele les deux fonctions implémenter ci dessus
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
