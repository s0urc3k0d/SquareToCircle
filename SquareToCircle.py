import os
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import filedialog

def print_header():
    header = (
        "====================================\n"
        "           Square to Circle         \n"
        "            by S0URC3K0D            \n"
        "===================================="
    )
    print(header)
    print()  # Ligne vide pour aérer

def select_folder(title):
    folder = filedialog.askdirectory(title=title)
    if not folder:
        print(f"Aucun dossier sélectionné pour : {title}")
        exit(1)
    return folder

def process_images(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            input_path = os.path.join(source_folder, filename)
            try:
                with Image.open(input_path) as im:
                    width, height = im.size

                    # Vérifie si l'image est carrée
                    if width != height:
                        print(f"Image ignorée (non carrée): {filename}")
                        continue

                    # Convertir en mode RGBA pour gérer la transparence
                    im = im.convert("RGBA")

                    # Création d'un masque circulaire en niveaux de gris
                    mask = Image.new("L", im.size, 0)
                    draw = ImageDraw.Draw(mask)
                    draw.ellipse((0, 0, width, height), fill=255)

                    # Appliquer le masque sur le canal alpha de l'image
                    im.putalpha(mask)

                    # Si l'image d'origine est JPEG, sauvegarde en PNG pour conserver la transparence
                    base, ext = os.path.splitext(filename)
                    if ext.lower() in ['.jpg', '.jpeg']:
                        new_filename = base + ".png"
                    else:
                        new_filename = filename

                    output_path = os.path.join(destination_folder, new_filename)
                    im.save(output_path)
                    print(f"Image traitée : {new_filename}")

            except Exception as e:
                print(f"Erreur lors du traitement de {filename} : {e}")

    print("Traitement terminé.")

if __name__ == "__main__":
    print_header()  # Affichage de l'entête dans l'invite de commande

    # Initialisation de Tkinter et masquage de la fenêtre principale
    root = tk.Tk()
    root.withdraw()

    # Sélection du dossier source et destination via des boîtes de dialogue
    source_folder = select_folder("Sélectionnez le dossier source contenant les images")
    destination_folder = select_folder("Sélectionnez le dossier de destination pour les images modifiées")

    process_images(source_folder, destination_folder)
