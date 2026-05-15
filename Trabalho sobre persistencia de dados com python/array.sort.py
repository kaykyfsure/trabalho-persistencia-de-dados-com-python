import random


print("--- PARTE 1: ARRAY DE INTEIROS ---")


array_inteiros = [random.randint(1, 100) for _ in range(15)]
print(f"Array original (desordenado): {array_inteiros}")


array_inteiros.sort()


print(f"Array ordenado (crescente):   {array_inteiros}")


array_inteiros.sort(key=None, reverse=True)


print(f"Array ordenado (decrescente): {array_inteiros}")


print("\n" + "="*50 + "\n")



print("--- PARTE 2: ARRAY DE STRINGS ---")


array_strings = [
    "Carlos Souza",      
    "15/05/1996",        
    "123.456.789-00",    
    "45.678.901-2",      
    "Ana Costa",         
    "20/12/2001",        
    "987.654.321-11",    
    "12.345.678-9"       
]
print(f"Array original (desordenado): {array_strings}")


array_strings.sort()


print(f"Array ordenado (crescente):   {array_strings}")


array_strings.sort(key=None, reverse=True)


print(f"Array ordenado (decrescente): {array_strings}")