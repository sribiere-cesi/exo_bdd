class Utilisateur:
    def __init__(self, email, password):
        self.email = email
        self.password = password

utilisateurs = [
    Utilisateur('test@example.com', 'password123')
]

taches = []

def connexion(email, password):
    for utilisateur in utilisateurs:
        if utilisateur.email == email and utilisateur.password == password:
            return True
    return False

def creer_tache(titre, description):
    if not titre:
        raise ValueError("Le titre est obligatoire")
    tache = {'titre': titre, 'description': description}
    taches.append(tache)
    return tache
