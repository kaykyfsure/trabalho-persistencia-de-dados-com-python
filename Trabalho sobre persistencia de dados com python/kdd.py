import time

lista_palavras = list()

nome_arquivo_entrada = 'seu_arquivo.txt'

try:
    with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            
            palavras_linha = linha.split()
            
            for palavra in palavras_linha:
                palavra_limpa = palavra.strip('.,!?;:()[]{}""\'\'')
                if palavra_limpa:  
                    lista_palavras.append(palavra_limpa.lower()) 
                    
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo_entrada}' não foi encontrado. Crie o arquivo na mesma pasta.")
    exit()

print(f"Total de palavras extraídas: {len(lista_palavras)}\n")


dados_bubble = lista_palavras.copy()
dados_selection = lista_palavras.copy()
dados_native = lista_palavras.copy()


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Iniciando Bubble Sort...")
inicio = time.time()
bubble_sort(dados_bubble)
fim = time.time()
tempo_bubble = fim - inicio
print(f"Bubble Sort concluído! Tempo: {tempo_bubble:.6f} segundos.")
print(f"Amostra do resultado: {dados_bubble[:10]}\n")


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("Iniciando Selection Sort...")
inicio = time.time()
selection_sort(dados_selection)
fim = time.time()
tempo_selection = fim - inicio
print(f"Selection Sort concluído! Tempo: {tempo_selection:.6f} segundos.")
print(f"Amostra do resultado: {dados_selection[:10]}\n")


print("Iniciando Ordenação Nativa (Timsort)...")
inicio = time.time()
dados_native.sort() 
fim = time.time()
tempo_native = fim - inicio
print(f"Ordenação Nativa concluída! Tempo: {tempo_native:.6f} segundos.")
print(f"Amostra do resultado: {dados_native[:10]}\n")

print("="*50)
print("Análise de Performance:")
print(f"Bubble Sort:    {tempo_bubble:.6f} s")
print(f"Selection Sort: {tempo_selection:.6f} s")
print(f"Método Nativo:  {tempo_native:.6f} s")
print("="*50)
