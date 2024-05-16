import numpy as np
import pygad

# Datos de las inversiones y beneficios por zona
inversiones = np.array([
                        [0, 0, 0, 0],
                        [0.28, 0.25, 0.15, 0.20],
                        [0.45, 0.41, 0.25, 0.33],
                        [0.65, 0.55, 0.40, 0.42],
                        [0.78, 0.65, 0.50, 0.48],
                        [0.90, 0.75, 0.62, 0.53],
                        [1.02, 0.80, 0.73, 0.56],
                        [1.13, 0.85, 0.82, 0.58],
                        [1.23, 0.88, 0.90, 0.60],
                        [1.32, 0.90, 0.96, 0.60],
                        [1.38, 0.90, 1.00, 0.60]
                        ])

# Función de aptitud
def funcion_aptitud(ga_instance, solution, solution_idx):
    total_inversion = np.sum(solution)
    penalizacion = np.abs(total_inversion - 10)  # Calcular la diferencia con 10
    ganancias = np.dot(solution, inversiones.T) # Transponer inversiones
    return np.sum(ganancias) / 500 * penalizacion + 1

# Configuración del algoritmo genético
ga_config = {"num_generations": 20,
             "num_parents_mating": 25,
             "sol_per_pop": 50,
             "num_genes": 4,
             "fitness_func": funcion_aptitud,
             "mutation_percent_genes": 1,
             "crossover_type": "two_points"}

# Crear el objeto del algoritmo genético
ga_instance = pygad.GA(**ga_config)

# Ejecutar el algoritmo genético
ga_instance.run()

# Obtener la mejor solución
mejor_solucion, mejor_aptitud, mejor_idx = ga_instance.best_solution()

# Redondear los valores de la solución y ajustar para que sumen 10 y sean no negativos
solucion_ajustada = np.maximum(np.round(mejor_solucion), 0)
diferencia = int(np.sum(solucion_ajustada) - 10)  # Diferencia entre la suma actual y 10
indices_ordenados = np.argsort(mejor_solucion)  # Ordenar los valores de la solución

# Ajustar los valores para que sumen 10 y sean no negativos
for i in range(abs(diferencia)):
    if diferencia > 0 and i < len(indices_ordenados):
        solucion_ajustada[indices_ordenados[-(i + 1)]] -= 1  # Restar 1 si la diferencia es positiva y el índice es válido
    elif diferencia < 0 and i < len(indices_ordenados):
        solucion_ajustada[indices_ordenados[i]] += 1  # Sumar 1 si la diferencia es negativa y el índice es válido


print("Mejor solución encontrada:", solucion_ajustada)
print("Beneficio total:", mejor_aptitud)
