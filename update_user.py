import pandas as pd
import sqlite3

# Nome del file Excel e del database
excel_file = "utenti.xlsx"
db_file = "utenti.db"

# Leggere il file Excel
df = pd.read_excel(excel_file, engine='openpyxl')

# Specificare il nome da modificare e il nuovo nome
vecchio_nome = "Madeline"  # Nome attuale da cambiare
nuovo_nome = "DonCirPWTelemedicina"  # Nuovo nome da impostare

# Modificare il nome nel DataFrame
df.loc[df["Nome"] == vecchio_nome, "Nome"] = nuovo_nome

# Salvare il file Excel aggiornato
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f"Nome '{vecchio_nome}' cambiato in '{nuovo_nome}' nel file Excel.")

# Connessione al database SQLite
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Aggiornare il database con il nuovo nome
cursor.execute("UPDATE utenti SET Nome = ? WHERE Nome = ?", (nuovo_nome, vecchio_nome))

# Salvare le modifiche e chiudere la connessione
conn.commit()
conn.close()

print(f"Nome '{vecchio_nome}' cambiato in '{nuovo_nome}' anche nel database SQLite!")
