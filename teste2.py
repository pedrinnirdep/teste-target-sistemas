def contar_a_na_string(string):
    contador_a = 0
    
    for char in string:
        if char == 'a' or char == 'A':
            contador_a += 1
    
    if contador_a > 0:
        return f"A letra 'a' ocorre {contador_a} vezes na string."
    else:
        return "A letra 'a' não está presente na string."

string = input("Informe uma string: ")
resultado = contar_a_na_string(string)
print(resultado)

