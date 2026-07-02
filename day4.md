# Jour 4 — Programmation Orientée Objet Python


## Objectifs

À la fin de la journée, l'apprenant doit être capable de :

1. Définir une **classe** avec attributs, constructeur (`__init__`) et méthodes
2. Comprendre **encapsulation** et **héritage** simple en Python
3. Modéliser un jeu de données comme un **objet** (préfiguration des classes utilisées en ML)
4. Relier POO Python à POO PHP/Laravel (Models, héritage Eloquent)

---

## À bien comprendre (concepts clés)

| Concept | Explication |
|---------|-------------|
| **`class`** | Plan pour créer des objets. `class Dataset:` définit le comportement. |
| **`__init__`** | Constructeur : `def __init__(self, path):` — `self` = l'instance (équivalent `$this`) |
| **`self`** | Référence à l'instance courante. Obligatoire en premier paramètre des méthodes d'instance. |
| **Attributs d'instance** | `self.path = path` — données propres à chaque objet |
| **Méthodes** | Fonctions dans la classe : `def summary(self):` |
| **Héritage** | `class CsvDataset(Dataset):` — réutilise et étend le parent |
| **`super()`** | Appelle la méthode du parent : `super().__init__(path)` |
| **`@property`** | Méthode accessible comme attribut : `dataset.row_count` au lieu de `dataset.row_count()` |

**Pont Laravel :** `class User extends Model` → `class CsvDataset(Dataset)`. Les Models encapsulent des données + comportement.

**Pourquoi en IA :** On encapsule chargement, nettoyage et stats dans une classe → pipeline lisible et réutilisable.

---

## Tâches à réaliser

### Classe `Dataset` de base

- [ ] **T4.1** — Créer `src/dataset.py`

- [ ] **T4.2** — Implémenter la classe parente `Dataset` :

```python
class Dataset:
    def __init__(self, name: str):
        self.name = name
        self._records: list[dict] = []  # convention _: "privé"

    def load(self, records: list[dict]) -> None:
        """Charge les enregistrements en mémoire."""
        ...

    @property
    def row_count(self) -> int:
        ...

    @property
    def columns(self) -> list[str]:
        """Retourne les noms de colonnes (clés du premier enregistrement)."""
        ...

    def summary(self) -> dict:
        """Retourne nom, row_count, columns."""
        ...

    def __repr__(self) -> str:
        return f"Dataset(name={self.name!r}, rows={self.row_count})"
```

- [ ] **T4.3** — Implémenter la sous-classe `CsvDataset(Dataset)` :
  - Méthode `load_from_csv(self, path: str) -> None` — réutilise `load_csv` de `utils.py`
  - Méthode `filter_by_column(self, column: str, min_value: float) -> list[dict]`

- [ ] **T4.4** — Tester en console Python interactif :
  ```python
  from src.dataset import CsvDataset
  ds = CsvDataset("Étudiants")
  ds.load_from_csv("data/sample.csv")
  print(ds)
  print(ds.summary())
  ```

### Notebook + refactor

- [ ] **T4.5** — Créer `notebooks/04_oop_dataset.ipynb` :
  - Instancier `CsvDataset`
  - Charger les données
  - Afficher `row_count`, `columns`, `summary()`
  - Filtrer par score >= 10
  - Cellule Markdown : schéma de la hiérarchie de classes (texte ou dessin)

- [ ] **T4.6** — Refactoriser `main.py` pour utiliser `CsvDataset` au lieu d'appels directs à `utils`

- [ ] **T4.7** — Ajouter une classe bonus `FilteredDataset(CsvDataset)` avec méthode `top_n(self, column: str, n: int)` — optionnel mais recommandé pour les avancés

- [ ] **T4.8** — Rédiger `docs/oop_notes.md` (1 page max) :
  - Qu'est-ce que `self` ?
  - Différence entre attribut public et `_attribut`
  - Lien avec un Model Eloquent Laravel (exemple concret)

- [ ] **T4.9** — Commit : `feat: add Dataset and CsvDataset classes`

---

## Critères d'acceptation

- [ ] `CsvDataset` hérite bien de `Dataset` et utilise `super()`
- [ ] `print(ds)` affiche une représentation lisible (`__repr__`)
- [ ] `main.py` refactoré utilise la classe
- [ ] L'apprenant peut dessiner/expliquer le diagramme parent → enfant à l'oral

---

## Auto-évaluation

1. À quoi sert `self` ?
2. Que signifie le `_` devant `_records` ?
3. Quelle est la différence entre `@property` et une méthode classique ?
4. Pourquoi créer `CsvDataset` plutôt que tout mettre dans `utils.py` ?

---
