def inverter_string(string):
    string_invertida = ''
    for char in string:
        string_invertida = char + string_invertida
    return string_invertida

string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)
print("String Invertida:", string_invertida)
