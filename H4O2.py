import re
import math
import numpy as np

# Function to calculate the electrostatic energy between two atoms
def calculate_energy(qi, qj, rij):
    return ((qi * qj) / rij) * 332

# Ruta del archivo CSV
archivo_csv = "C:/Users/USUARIO/Downloads/chemcraft/molecules csv/H4O2(3.3).csv"

# Listas para almacenar las columnas
atom_index = []
coordinates = []

# Leer el archivo CSV
with open(archivo_csv, 'r') as csv_file:
    for line in csv_file:
        # Usar expresión regular para dividir la línea en columnas por cualquier cantidad de espacios
        columns = re.split(r'\s+', line.strip())

        if len(columns) == 4:
            atom_index.append(columns[0])
            coordinates.append(list(map(float, columns[1:])))


# Definir el tamaño de la matriz
num_atoms = len(coordinates)
matrix_rij = np.zeros((num_atoms, num_atoms))

# Llenar la matriz con valores
for i in range(num_atoms):
    for j in range(num_atoms):
        if i != j:
            rij = math.sqrt(sum((ci - cj) ** 2 for ci, cj in zip(coordinates[i], coordinates[j])))
            matrix_rij[i, j] = rij

# Calculate non-bonding energies and distances
Etot = 0
for i in range(num_atoms):
    for j in range(num_atoms):
        if i != j:
            rij = matrix_rij[i, j]
            if rij >= 1.6:
                qi = qj = 0
                if atom_index[i] == '1':
                    qi = 0.417
                elif atom_index[i] == '8':
                    qi = -0.417 * 2
                if atom_index[j] == '1':
                    qj = 0.417
                elif atom_index[j] == '8':
                    qj = -0.417 * 2

                Eij = calculate_energy(qi, qj, rij)
                Etot += Eij

# Print results
print("\nTotal non-bonding energy:", Etot)
print("\nDistances matrix:\n", matrix_rij)
