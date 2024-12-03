from google.cloud import firestore
from datetime import datetime

def save_message():
    # Firestore-Client initialisieren
    db = firestore.Client()

    # Daten erstellen
    doc_ref = db.collection("messages").document()
    doc_ref.set({
        "message": "Hallo",
        "timestamp": datetime.utcnow()
    })

    print("Nachricht wurde erfolgreich gespeichert.")

if __name__ == "__main__":
    save_message()
