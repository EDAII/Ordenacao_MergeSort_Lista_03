import numpy as np
import time


# Gera valores inteiros aleatorios de 1 ate 100000
def gera_valor_aleatorio():
    valor = np.random.randint(0, 100000)
    return valor


# Gera o vetor de valores randomicos
def gera_lista(limite_superior):
    lista = []
    for i in range(limite_superior):
        numero = gera_valor_aleatorio()
        lista.append(numero)
    return lista


# Faz o merge de dois vetores do vetor principal
def merge(vetor, left, mid, right):

    subvetor_esquerda = mid - left + 1
    subvetor_direita = right - mid

    temp_vet_esq = [0] * (subvetor_esquerda)
    temp_vet_dir = [0] * (subvetor_direita)

    # Copia o conteudo do vetor principal para os subvetores
    for i in range(0, subvetor_esquerda):
        temp_vet_esq[i] = vetor[left + i]
    for j in range(0, subvetor_direita):
        temp_vet_dir[j] = vetor[mid + 1 + j]

    # Define index inicial dos subvetores
    i = 0
    j = 0
    # Define index inicial do vetor principal
    k = left

    # Compara elemento por elemento dos subvetoes e guarda no vetor principal
    while i < subvetor_esquerda and j < subvetor_direita:
        if temp_vet_esq[i] <= temp_vet_dir[j]:
            vetor[k] = temp_vet_esq[i]
            i += 1
        else:
            vetor[k] = temp_vet_dir[j]
            j += 1
        k += 1
    # Copia os valores do subvetor da esquerda caso ainda tenha elementos
    while i < subvetor_esquerda:
        vetor[k] = temp_vet_esq[i]
        i += 1
        k += 1
    # Copia os valores do subvetor da direita caso ainda tenha elementos
    while j < subvetor_direita:
        vetor[k] = temp_vet_dir[j]
        j += 1
        k += 1

    return vetor


def merge_sort(vetor, left, right):

    if left < right:

        # right - 1 usado para evitar overflow
        mid = (left+(right-1))/2

        merge_sort(vetor, left, mid)
        merge_sort(vetor, mid+1, right)
        merge(vetor, left, mid, right)

    return vetor


# Recebe o limite superior do vetor de valores aleatorios e realiza a ordenacao
def main():
    tamanho = input('Digite o tamanho do vetor a ser gerado: \n')
    vetor = []
    vetor_ordenado = []
    vetor = gera_lista(tamanho)

    print(vetor)

    start = time.time()
    vetor_ordenado = merge_sort(vetor, 0, tamanho-1)
    end = time.time()

    print(vetor_ordenado)
    print('Tempo para ordenacao: ', end - start)

if __name__ == '__main__':
    main()
