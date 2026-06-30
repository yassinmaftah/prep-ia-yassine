# Jour 3 — Fonctions, modules & structure de projet

---

## Objectifs

À la fin de la journée, l'apprenant doit être capable de :

1. Écrire des **fonctions réutilisables** avec paramètres, valeurs par défaut et annotation de types
2. Organiser le code en **modules** (fichiers `.py`) importables
3. Comprendre `if __name__ == "__main__":` et la différence import vs exécution directe
4. Structurer un mini-projet data comme on structurera plus tard un pipeline ML

---

## À bien comprendre (concepts clés)

| Concept | Explication |
|---------|-------------|
| **`def`** | Définit une fonction. `return` renvoie une valeur (sinon la fonction retourne `None`). |
| **Type hints** | `def load(path: str) -> list:` — n'impose rien à l'exécution, mais documente et aide l'IDE. Standard en projets pro. |
| **Module** | Un fichier `.py` = un module importable : `from src.utils import load_csv` |
| **`__name__ == "__main__"`** | Le fichier est lancé directement (`python main.py`) → exécute le bloc. S'il est importé → ce bloc ne s'exécute pas. |
| **Séparation des responsabilités** | `utils.py` = fonctions pures / outils. `main.py` = point d'entrée qui orchestre. Même logique que Controller vs Service en Laravel. |
| **`pathlib`** | Module standard pour manipuler les chemins de fichiers de façon propre (`Path("data/file.csv")`). |

**Habitude data :** une fonction = une responsabilité claire, testable, réutilisable dans un notebook via `import`.

---

## Tâches à réaliser

### Module `utils.py`

Créer la structure :

```
prep-ia-prenom/
├── src/
│   ├── __init__.py      # fichier vide
│   └── utils.py
├── data/
│   └── sample.csv       # fourni ou créé par l'apprenant
├── main.py
└── notebooks/
```

- [ ] **T3.1** — Créer `data/sample.csv` avec colonnes : `id,name,age,score` (minimum 10 lignes)

- [ ] **T3.2** — Dans `src/utils.py`, implémenter les fonctions suivantes :

```python
from pathlib import Path

def load_csv(path: str | Path) -> list[dict]:
    """Lit un CSV simple et retourne une liste de dictionnaires.
    Utiliser uniquement le module csv (pas pandas pour l'instant)."""
    ...

def filter_by_min_score(records: list[dict], min_score: float) -> list[dict]:
    """Retourne les enregistrements dont score >= min_score."""
    ...

def average_score(records: list[dict]) -> float:
    """Calcule la moyenne du champ 'score'. Retourne 0.0 si liste vide."""
    ...

def summarize(records: list[dict]) -> dict:
    """Retourne {'count': n, 'avg_score': x, 'max_score': y, 'min_score': z}"""
    ...
```

- [ ] **T3.3** — Chaque fonction doit avoir une **docstring** d'une ligne minimum

- [ ] **T3.4** — Gérer le cas liste vide dans `average_score` (pas de division par zéro)

### Script principal & intégration notebook

- [ ] **T3.5** — Créer `main.py` :

```python
from src.utils import load_csv, filter_by_min_score, average_score, summarize

if __name__ == "__main__":
    records = load_csv("data/sample.csv")
    print("Total records:", len(records))
    passed = filter_by_min_score(records, min_score=10)
    print("Admis (score >= 10):", len(passed))
    print("Résumé:", summarize(records))
```

- [ ] **T3.6** — Vérifier l'exécution : `python main.py` (depuis la racine du projet, venv activé)

- [ ] **T3.7** — Créer `notebooks/03_modules.ipynb` :
  - Cellule 1 : ajouter la racine du projet au `sys.path` **ou** installer le package en editable (`pip install -e .`) — formateur choisit une méthode
  - Cellule 2 : `from src.utils import load_csv, summarize`
  - Cellule 3 : charger le CSV et afficher le résumé
  - Cellule 4 (Markdown) : expliquer la différence entre lancer `main.py` et importer dans un notebook

- [ ] **T3.8** — Tests manuels documentés dans un fichier `tests/manual_tests.md` :

| Fonction | Entrée | Résultat attendu | OK ? |
|----------|--------|------------------|------|
| `average_score([])` | `[]` | `0.0` | |
| `filter_by_min_score(..., 12)` | sample.csv | N lignes | |
| ... | | | |

- [ ] **T3.9** — Commit : `feat: add utils module and main entrypoint`

---

## Critères d'acceptation

- [ ] `python main.py` affiche un résumé correct
- [ ] Les 4 fonctions sont dans `utils.py`, pas dans `main.py`
- [ ] Import depuis le notebook fonctionne
- [ ] `manual_tests.md` contient au moins 6 cas de test

---

