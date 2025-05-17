#ATV 5 
import random
import statistics


# 1) 
def calcula_imc(p=87, a=1.75):
    return p / a**2

# 2) 
alturas = [
    45, 23, 67, 12, 11, 89, 23, 41, 50, 62, 78, 34, 56, 19, 72, 88, 11, 90, 39, 65,
    76, 27, 48, 59, 81, 14, 11, 93, 3, 68, 29, 52, 74, 16, 85, 20, 55, 38, 69, 11,
    83, 7, 44, 61, 18, 96, 22, 58, 31, 71, 40, 53, 87, 31
]


print("Maior valor:", max(alturas))
print("Menor valor:", min(alturas))
print("Soma dos valores:", sum(alturas))
print("Valor absoluto de -25:", abs(-25))
print("3.14159 arredondado para 2 casas decimais:", round(3.14159, 2))


print("\n--- Estatísticas com statistics ---")
print("Média:", statistics.mean(alturas))
print("Mediana:", statistics.median(alturas))
print("Moda:", statistics.mode(alturas))
print("Variância da amostra:", statistics.variance(alturas))
print("Desvio padrão da amostra:", statistics.stdev(alturas))

# 3) 

matriz_float = [[random.random() for _ in range(10)] for _ in range(5)]


matriz_inteiros = [[random.randint(0, 9) for _ in range(4)] for _ in range(8)]


print("\nMatriz 5x10 (floats entre 0 e 1):")
for linha in matriz_float:
    print(linha)

print("\nMatriz 8x4 (inteiros entre 0 e 9):")
for linha in matriz_inteiros:
    print(linha)


print("\nIMC calculado:", round(calcula_imc(), 2))
