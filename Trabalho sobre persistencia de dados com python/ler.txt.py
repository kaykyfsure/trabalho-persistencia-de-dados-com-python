nome_arquivo = r"C:\Users\kayky\OneDrive\Área de Trabalho\Nova pasta\loremipsum.txt"


arquivo = open(nome_arquivo, "r", encoding="utf-8")


print("____TODO O CONTEÚDO DO ARQUIVO____")
todo_conteudo = arquivo.read()
print(todo_conteudo)


arquivo.seek(0)


print("____APENAS A PRIMEIRA LINHA____")
primeira_linha = arquivo.readline()
print(primeira_linha, end="")  


arquivo.seek(0)


print("\n\n____APENAS OS 3 PRIMEIROS CARACTERES____")
tres_caracteres = arquivo.read(3)
print(tres_caracteres)


arquivo.close()


print("____LEITURA UTILIZANDO A INSTRUÇÃO 'with'____")
with open(nome_arquivo, "r", encoding="utf-8") as arquivo_with:
    conteudo = arquivo_with.read()
    print(conteudo)