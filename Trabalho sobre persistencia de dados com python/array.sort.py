array_inteiros = [55, 7, 89, 12, 42, 99, 1, 74, 23, 68, 47, 91, 18, 35, 60]

array_inteiros.sort()
print(f"Array ordenado (crescente):   {array_inteiros}")

array_inteiros.sort(key=None, reverse=True)
print(f"Array ordenado (decrescente): {array_inteiros}")


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

array_strings.sort()
print(f"Array ordenado (crescente):   {array_strings}")


array_strings.sort(key=None, reverse=True)
print(f"Array ordenado (decrescente): {array_strings}")
