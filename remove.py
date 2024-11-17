# Creation d'un script permettant de supprimer l'arrière-plan d'une image

import streamlit as st
from PIL import Image
from rembg import remove
from io import BytesIO

# Initialisation de la page
st.set_page_config(page_title='Effaceur d\'arrière plan', layout='wide', page_icon='✏️',
                   initial_sidebar_state='auto')

st.title('Effaceur d\'arrière plan')
st.write('Réaliser par Rachid SAHLI')
st.write('Cette application vous permet de supprimer l\'arrière plan de votre image.')
st.sidebar.write('## Uploader') # Initialisation de la sidebar

# Creation de 2 colonnes
col1, col2 = st.columns(2)

# Fonction de convertion
def convert_image(image):
    buf = BytesIO() # Stockage de l'image en memoire
    image.save(buf, format = 'PNG') # Sauvegarder l'image en memoire au format png
    byte_im = buf.getvalue() # Recuperation de l'image sous forme de bytes
    return byte_im # Retour des donnees de l'image sous forme de bytes

def fix_image(image):
    image = Image.open(image) # Ouverture de l'image
    col1.write('Image orginiale') # Texte sur la colonne 1
    col1.image(image) # Image originale sur la colonne 1
    fixed = remove(image) # Remove bg de l'image

    col2.write("Image sans fond") # Text sur la colonne 2
    col2.image(fixed) # Image transfo sur la colonne 2

    st.sidebar.write('\n') # Saut de ligne
    st.download_button("Télécharger l'image", convert_image(image),
                        'image_detouree.png', 'image/png') # Boutton de telechargement

# Chargement de l'image dans la sidebar
image_upload = st.sidebar.file_uploader('Choisissez une image', type=['png','jpeg',"jpg"])    

# Condition
if image_upload is not None: # Si image non-vide
    fix_image(image_upload) # Afficher l'image telecharger
else:
    fix_image('image/elephant.jpg') # Afficher image par defaut
    

