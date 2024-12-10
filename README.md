# 📘 Exercice BDD : Connexion et Gestion des Tâches

Ce projet permet de pratiquer le **Behavior-Driven Development (BDD)** en utilisant la bibliothèque **Behave**.  
Vous allez définir des scénarios Gherkin, implémenter les steps correspondants et automatiser les tests de l'application de gestion des tâches.  

---

## 📚 **Structure du projet**
bdd-taches/
 ├── features/ 
 │ ├── taches.feature # Fichier contenant les scénarios Gherkin 
 │ └── steps/ 
 │ └── taches_steps.py # Contient les implémentations des étapes (Given, When, Then) 
 ├── app/ 
 │ └── taches.py # Contient le code de l'application 
 ├── requirements.txt # Fichier des dépendances (Behave) 
 └── README.md # Explications de l'exercice


---

## 📋 **Objectifs**
- Écrire des scénarios BDD avec Gherkin.
- Implémenter les étapes de test (Given, When, Then) avec **Behave**.
- Automatiser les tests de connexion et de gestion des tâches.  

---

## 🚀 **Installation**

###  **Cloner le dépôt**
```bash
git clone [URL_DU_REPO]
cd bdd-taches
```
###  **Installer les dépendances**
Assurez-vous d'avoir Python 3.x installé. Ensuite, exécutez :
```bash
pip install -r requirements.txt
```

###  **Lancer les tests**
```bash
behave
```

---

## 📋 **Fichiers importants**

| Fichier  | Rôle        |
| :--------------- |:---------------:| 
| features/taches.feature |   	Scénarios de test BDD écrits en Gherkin.        |
| features/steps/taches_steps.py  | Contient l'implémentation des étapes Given, When, Then.            |
| app/taches.py | 	Logique métier (connexion utilisateur, création de tâches).          |
| requirements.txt| Liste des dépendances à installer (Behave).          |

---

## 📋 ** Exemple de scénario BDD (Gherkin)**
Le fichier features/taches.feature contient les scénarios suivants :
```gherkin
Feature: Connexion d'un utilisateur
  En tant qu'utilisateur
  Je veux me connecter à mon compte
  Afin d'accéder à mes informations

  Scenario: Connexion réussie
    Given un utilisateur enregistré avec l'e-mail "test@example.com" et le mot de passe "password123"
    When il saisit "test@example.com" et "password123"
    Then il est redirigé vers le tableau de bord

  Scenario: Échec de la connexion
    Given un utilisateur enregistré avec l'e-mail "test@example.com" et le mot de passe "password123"
    When il saisit "test@example.com" et "mauvaismotdepasse"
    Then un message d'erreur "Identifiants incorrects" est affiché
 ```
---

 ###  **Lancer les tests**
```bash
behave
```
--- 
 ###  **Améliorations possibles**

- Ajouter de nouveaux scénarios (par exemple, réinitialisation de mot de passe).
- Valider les champs d'entrée utilisateur (par ex. empêcher les champs vides).
- Refactoriser le code dans taches.py pour améliorer la qualité et la lisibilité.

---
 ###  **Ressources utiles**

- [Documentation Behave](https://behave.readthedocs.io/en/latest/)
- [Introduction au BDD](https://www.youtube.com/watch?v=333nX_Q9-3s)
