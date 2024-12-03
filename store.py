import os
import base64
import json
from google.cloud import firestore
from google.oauth2 import service_account
from google.auth.transport.requests import Request

def authenticate_firestore():
    # Die Base64-verschlüsselte JSON-Datei aus den Umgebungsvariablen entschlüsseln
    service_account_base64 = os.getenv("GOOGLE_SERVICE_ACCOUNT")
    decoded_service_account = base64.b64decode(service_account_base64)
    
    # JSON-Daten laden
    service_account_info = json.loads(decoded_service_account)

    # Authentifizierung und Initialisierung von Firestore
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    db = firestore.Client(credentials=credentials)
    return db

def save_to_firestore(collection_name, document_data):
    db = authenticate_firestore()
    # Speichern der Daten in Firestore
    doc_ref = db.collection(collection_name).add(document_data)
    print(f"Document written with ID: {doc_ref.id}")

if __name__ == "__main__":
    # Beispiel-Daten zum Speichern
    data = {
        "name": "Test User",
        "email": "testuser@example.com",
        "status": "active"
    }

    # Die Sammlung und Dokumenten-ID in Firestore angeben
    collection_name = "users"

    save_to_firestore(collection_name, data)
