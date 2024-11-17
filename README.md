# Remove Background App

Cette application permet de supprimer l'arrière-plan d'une image. Chargez vos images et obtenez une version sans fond !

<img width="1469" alt="Capture d’écran 2024-11-17 à 02 07 30" src="https://github.com/user-attachments/assets/e7586cb0-9c7b-413a-90ee-f23a448c2c84">

## Fonctionnalités

- **Suppression d'arrière-plan** : Téléchargez une image et obtenez une version sans arrière-plan.
- **Interface intuitive** : Créez et interagissez facilement avec les images via une interface simple et propre Streamlit.

## Prérequis

- **Python 3.7+**
- **Streamlit** : Pour créer l'interface utilisateur interactive.
- **rembg** : Pour la suppression automatique d'arrière-plan des images.
- **Pillow** : Pour manipuler les images.

## Installation

### Étape 1 : Cloner le dépôt

Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/rachidsahli/Remove-bg-app.git
cd Remove-bg-app
```

### Étape 2 : Créer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
```

### Étape 3 : Installer les dépendances

```bash
pip install -r requirements.txt
```

### Étape 4 : Lancer l'application

```bash
streamlit run app.py
```

### License
Licence MIT
