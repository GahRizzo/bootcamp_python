### Objetivo: Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

def reverse_string(string: str) -> str:
    
    reverse_str = string[::-1]
    return reverse_str

typed_string = input("Type a word: ")

print(f"The reversed string is: {reverse_string(typed_string)}")