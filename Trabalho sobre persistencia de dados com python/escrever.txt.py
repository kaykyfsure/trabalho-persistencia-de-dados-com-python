arquivo = open("texto.txt", "w", encoding="utf-8")

texto = list()

texto.append("conheço o seu o seu mano,ele é um rato não é um homem\n")
texto.append("moshpit,enquanto geral grita meu nome\n")
texto.append("você disse que ia quebrar tudo,me impressione,comece a girar no moshpit igual um ciclone\n")

arquivo.writelines(texto)

arquivo.close()

print("Arquivo 'texto.txt' criado e escrito com sucesso!")