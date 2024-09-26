import mysql.connector

# Connexion à MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="user-non-root",
    password="password-non-root"
)

cursor = conn.cursor()

# Création de la base de données 'Ecole' et sélection de cette base
cursor.execute("CREATE DATABASE IF NOT EXISTS Ecole")
cursor.execute("USE Ecole")

# Création des tables "élèves" et "enseignants"
cursor.execute('''
CREATE TABLE IF NOT EXISTS eleves (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    numero_salle INT NOT NULL,
    telephone VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(100) UNIQUE,
    annee_obtention INT NOT NULL,
    numero_classe INT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS enseignants (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    numero_salle INT NOT NULL,
    departement VARCHAR(100) NOT NULL,
    annee_obtention INT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telephone VARCHAR(15) NOT NULL UNIQUE,
    numero_classe INT NOT NULL
);
''')

# Insertion de l'étudiant Mark Watney et de l'enseignant Jonas Salk
cursor.execute('''
INSERT INTO eleves (prenom, nom, numero_salle, telephone, email, annee_obtention, numero_classe)
VALUES ('Mark', 'Watney', 101, '777-555-1234', NULL, 2035, 5);
''')

cursor.execute('''
INSERT INTO enseignants (prenom, nom, numero_salle, departement, annee_obtention, email, telephone, numero_classe)
VALUES ('Jonas', 'Salk', 201, 'Biologie', 1955, 'jsalk@school.org', '777-555-4321', 5);
''')

# Sauvegarde des modifications
conn.commit()

# Extraction des données
cursor.execute("SELECT * FROM eleves;")
eleves = cursor.fetchall()

cursor.execute("SELECT * FROM enseignants;")
enseignants = cursor.fetchall()

print("Élèves :")
for eleve in eleves:
    print(eleve)

print("\nEnseignants :")
for enseignant in enseignants:
    print(enseignant)

# Association des élèves et enseignants
print("\nAssociation des élèves avec leurs enseignants :")
for eleve in eleves:
    for enseignant in enseignants:
        if eleve[7] == enseignant[8]:
            print(f"L'élève {eleve[1]} {eleve[2]} (Classe {eleve[7]}) est associé à l'enseignant {enseignant[1]} {enseignant[2]} (Classe {enseignant[8]}).")

# Comptage des élèves par enseignant
enseignant_eleve_count = {}

for enseignant in enseignants:
    enseignant_eleve_count[enseignant[1] + " " + enseignant[2]] = 0

for eleve in eleves:
    for enseignant in enseignants:
        if eleve[7] == enseignant[8]:
            enseignant_eleve_count[enseignant[1] + " " + enseignant[2]] += 1

print("\nNombre d'élèves par enseignant :")
for enseignant, count in enseignant_eleve_count.items():
    print(f"{enseignant} a {count} élève(s).")

# Fermer la connexion
conn.close()
print("Connexion fermée.")
