import os
import json
import base64
import firebase_admin
from firebase_admin import credentials, firestore

def initialize_firestore():
    """
    Initialisiert Firestore mit dem Base64-verschlüsselten Secret aus GitHub Actions Secrets.
    """
    base64_secret = os.getenv("FIREBASE_SECRET_BASE64")
    if not base64_secret:
        raise ValueError("Das Secret 'FIREBASE_SECRET_BASE64' ist nicht verfügbar.")
    
    # Decode Base64-Secret
    decoded_secret = base64.b64decode(base64_secret).decode("utf-8")
    credentials_dict = json.loads(decoded_secret)
    cred = credentials.Certificate(credentials_dict)

    # Firebase initialisieren
    firebase_admin.initialize_app(cred)
    print("Firestore initialisiert.")

def create_collection():
    """
    Erstellt eine Sammlung namens 'hallo'.
    """
    db = firestore.client()
    doc_ref = db.collection("hallo").document("beispiel_dokument")
    doc_ref.set({
        "name": "Beispiel",
        "nachricht": "Hallo, Welt!",
        "zeitstempel": firestore.SERVER_TIMESTAMP
    })
    print("Sammlung 'hallo' mit einem Beispiel-Dokument erstellt.")
