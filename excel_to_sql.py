import pandas as pd
import sqlite3

# Nome del file Excel generato nell'esercizio 1
excel_file = "utenti.xlsx"

# Nome del database SQLite
db_file = "utenti.db"

# Leggere i dati dall'Excel
df = pd.read_excel(excel_file, engine='openpyxl')

# Connessione al database SQLite
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Creare la tabella SQL con gli stessi dati del file Excel
cursor.execute("""
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Cognome TEXT NOT NULL,
        Email TEXT UNIQUE NOT NULL,
        Telefono TEXT NOT NULL
    )
""")

# Inserire i dati nella tabella
df.to_sql("utenti", conn, if_exists="replace", index=False)

# Chiudere la connessione
conn.commit()
conn.close()

print(f"Tabella SQL creata e popolata con successo nel database {db_file}!")
