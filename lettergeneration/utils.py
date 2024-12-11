# myapp/utils.py

import PyPDF2
import openai

openai.api_key = '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'
import PyPDF2

def extraire_donnees(filepath):
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        contenu = ""
        for page in reader.pages:
            contenu += page.extract_text()
        return contenu


def generer_lettre_motivation(data):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes cover letters tailored to job requirements."},
            {"role": "user", "content": f"Utilise les informations suivantes pour rédiger une lettre de motivation personnalisée : {data}"}
        ]
    )
    return response.choices[0].message['content']

