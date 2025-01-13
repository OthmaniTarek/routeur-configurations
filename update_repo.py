import subprocess
import os

def run_command(command):
    """Exécute une commande shell et affiche la sortie."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Erreur : {result.stderr}")
        exit(1)

def is_git_repo():
    """Vérifie si le répertoire courant est un dépôt Git."""
    try:
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def update_repo(branch="main"):
    # Vérifie si le répertoire est un dépôt Git
    if not is_git_repo():
        print("Ce répertoire n'est pas un dépôt Git.")
        exit(1)

    # Récupère les modifications du dépôt distant
    print(f"Récupération des modifications du dépôt distant sur la branche {branch}...")
    run_command(f"git pull origin {branch}")

    # Vérifie s'il y a des conflits
    status = subprocess.run(["git", "status"], capture_output=True, text=True)
    if "conflit" in status.stdout.lower():
        print("Conflits détectés, résolution automatique...")
        # Résolution automatique des conflits en choisissant la version distante
        run_command("git checkout --theirs .")
        run_command("git add .")
        run_command('git commit -m "Résolution automatique des conflits"')

    # Ajoute toutes les modifications locales
    print("Ajout des modifications locales...")
    run_command("git add .")

    # Demande un message de commit
    commit_message = input("Entrez un message de commit : ")

    # Valide les modifications
    print("Validation des modifications...")
    run_command(f'git commit -m "{commit_message}"')

    # Pousse les modifications vers le dépôt distant
    print(f"Envoi des modifications vers le dépôt distant sur la branche {branch}...")
    run_command(f"git push origin {branch}")

    print("Mise à jour terminée avec succès.")

if __name__ == "__main__":
    branch = input("Entrez le nom de la branche à mettre à jour (par défaut 'main') : ")
    if not branch:
        branch = "main"
    update_repo(branch)