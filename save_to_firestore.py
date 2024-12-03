import os

def load_and_print_secret():
    # Secret aus der Umgebungsvariable laden
    secret_value = os.getenv("MY_SECRET")

    if secret_value:
        print(f"Secret erfolgreich geladen: {secret_value}")
    else:
        print("Fehler: Secret konnte nicht geladen werden.")

if __name__ == "__main__":
    load_and_print_secret()
