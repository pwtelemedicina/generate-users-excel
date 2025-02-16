import pandas as pd
import sqlite3

# Leggere il file Excel
file_path = "utenti.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

# Connessione al database SQLite
conn = sqlite3.connect("utenti.db")
cursor = conn.cursor()

# Creare la tabella utenti (se non esiste già)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Cognome TEXT,
        Email TEXT,
        Telefono TEXT
    )
""")

# Inserire i dati nel database
df.to_sql("utenti", conn, if_exists="replace", index=False)

# Chiudere la connessione
conn.commit()
conn.close()

print("Dati caricati nel database SQLite con successo!")
