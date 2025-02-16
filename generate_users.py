import pandas as pd
from faker import Faker

# Creazione dell'istanza di Faker per generare dati casuali
fake = Faker()

# Generare dati per 10 utenti
users = []
for _ in range(10):
    user = {
        "Nome": fake.first_name(),
        "Cognome": fake.last_name(),
        "Email": fake.email(),
        "Telefono": fake.phone_number()
    }
    users.append(user)

# Creare un DataFrame con i dati generati
df = pd.DataFrame(users)

# Salvare il DataFrame in un file Excel
file_path = "utenti.xlsx"
df.to_excel(file_path, index=False, engine='openpyxl')

print(f"File {file_path} generato con successo!")
