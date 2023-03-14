string = input("Digite uma string para ser invertida: ")
inverted = ""
for i in range(len(string) - 1, -1, -1):
    inverted += string[i]
print("String invertida: ", inverted)
