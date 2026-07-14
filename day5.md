# Jour 5 — Git workflow & première Pull Request


## Objectifs

À la fin de la journée, l'apprenant doit être capable de :

1. Travailler sur une **branche dédiée** (ne pas coder directement sur `main`)
2. Rédiger des **commits clairs** et atomiques
3. Ouvrir une **Pull Request** avec description structurée
4. Configurer un `.gitignore` adapté à un projet IA (venv, data sensibles, checkpoints)
5. **Objectif WarmUp formation :** 1ʳᵉ PR validée par le formateur ou un pair

---

## À bien comprendre (concepts clés)

| Concept | Explication |
|---------|-------------|
| **Branche** | Ligne de développement isolée. `git checkout -b feat/week1-final` |
| **Commit atomique** | Un commit = une modification logique. Message : `feat: ...`, `fix: ...`, `docs: ...` |
| **Pull Request (PR)** | Demande de fusion : « voici mon travail, merci de reviewer ». Standard en entreprise et en formation. |
| **`.gitignore`** | Fichiers à ne jamais versionner : secrets, gros datasets, environnements locaux |
| **Ne pas committer** | `.venv/`, `.ipynb_checkpoints/`, fichiers CSV avec données personnelles, clés API |
| **README** | Carte d'identité du projet : comment installer, lancer, structure des dossiers |

**Règle IA :** Les **données brutes** et les **modèles entraînés** (.pkl, .h5) ne vont généralement pas dans Git. On versionne le **code** et un petit `sample.csv` de démo.

---

## Tâches à réaliser

### Finalisation du projet semaine 1

- [ ] **T5.1** — Vérifier la structure finale du projet :

```
prep-ia-prenom/
├── README.md
├── .gitignore
├── requirements.txt
├── main.py
├── data/
│   └── sample.csv
├── src/
│   ├── __init__.py
│   ├── utils.py
│   └── dataset.py
├── notebooks/
│   ├── 01_hello_data.ipynb
│   ├── 02_php_to_python.ipynb
│   ├── 03_modules.ipynb
│   └── 04_oop_dataset.ipynb
├── docs/
│   └── oop_notes.md
└── tests/
    └── manual_tests.md
```

- [ ] **T5.2** — Compléter `.gitignore` :

```
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
*.pkl
*.h5
data/raw/
data/private/
.DS_Store
```

- [ ] **T5.3** — Rédiger `README.md` avec les sections :
  - **Description** du projet prep
  - **Prérequis** (Python 3.11+)
  - **Installation** (clone, venv, pip install -r requirements.txt)
  - **Lancement** (`python main.py`, `jupyter lab`)
  - **Structure du projet** (arborescence)
  - **Auteur** + semaine 1

- [ ] **T5.4** — Relire tous les notebooks : **Kernel Restart & Run All** — aucune erreur

- [ ] **T5.5** — Mettre à jour `requirements.txt` final

### Branche, PR & review

- [ ] **T5.6** — Cloner le **repo starter** de la formation (si pas déjà fait) ou utiliser son repo personnel selon consigne formateur

- [ ] **T5.7** — Créer la branche : `git checkout -b feat/week1-final`

- [ ] **T5.8** — Pousser tout le travail de la semaine avec commits propres (minimum 3 commits logiques, pas un seul commit géant)

- [ ] **T5.9** — Push : `git push -u origin feat/week1-final`

- [ ] **T5.10** — Ouvrir la **Pull Request** vers `main` avec ce template :

```markdown
## Description
Finalisation de la semaine 1 — Prep IA : environnement Python, syntaxe, modules, POO, Git.

## Checklist
- [ ] venv + requirements.txt
- [ ] 4 notebooks exécutables
- [ ] module utils.py + dataset.py
- [ ] main.py fonctionnel
- [ ] README complet
- [ ] .gitignore adapté projet IA

## Comment tester
1. git clone ...
2. python3 -m venv .venv && source .venv/bin/activate
3. pip install -r requirements.txt
4. python main.py
5. jupyter lab → ouvrir 04_oop_dataset.ipynb → Run All

## Difficultés rencontrées
(Décrire 2–3 lignes : ex. problème de kernel Jupyter, indentation, etc.)

## Ce que j'ai compris cette semaine
(5 lignes minimum)
```

- [ ] **T5.11** — Demander une review à un pair (buddy review) : le pair commente la PR avec au moins 1 remarque constructive

- [ ] **T5.12** — Corriger si nécessaire et obtenir **approbation formateur**

---

## Critères d'acceptation (fin de semaine 1)

| # | Critère | Statut |
|---|---------|--------|
| 1 | Environnement venv reproductible | ☐ |
| 2 | 4 notebooks sans erreur | ☐ |
| 3 | Code organisé en modules + classe Dataset | ☐ |
| 4 | README permet à un tiers de lancer le projet | ☐ |
| 5 | PR ouverte, reviewée et validée | ☐ |
| 6 | Explique oral Python vs PHP (5 min) | ☐ |

---
