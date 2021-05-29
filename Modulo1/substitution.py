def codificar(mensaje, rotacion):
    alfabeto_minusculas = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto_minusculas)
    codificado = ""
    for letras in mensaje:
        if not letras.isalpha() or letras.lower() == 'ñ':
            codificado += letras
            continue
        valor_letras = ord(letras)
        alfabeto_a_usar = alfabeto_minusculas
        limite = 97  
        if letras.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas
       
        posicion = (valor_letras - limite + rotacion) % longitud_alfabeto
        
        codificado += alfabeto_a_usar[posicion]
    return codificado
texto=input("Ingrese un texto a codificar: ")
resultado=codificar(texto,4) #la codificacion recorre el numero de letras indicadas en rotacion
print(resultado)