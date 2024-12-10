Feature: Connexion utilisateur
  Scenario: Connexion réussie
    Given un utilisateur enregistré avec l'e-mail "test@example.com" et le mot de passe "password123"
    When il saisit "test@example.com" et "password123"
    Then il est redirigé vers le tableau de bord
