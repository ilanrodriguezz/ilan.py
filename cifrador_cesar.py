cipherange = None
forwards = ""
backwards = ""
while type(cipherange) != int:
    try:
        cipherange = int(input("Ingrese el rango: "))
        if cipherange <= -26 or cipherange >= 26:
            print("Por favor, ingrese un número entre -25 y 25")
            cipherange = None
            continue
        elif cipherange == 0:
            print("No seas difícil.")
            cipherange = None
            continue
        elif cipherange < 0 and cipherange > -26:
            cipherange *= -1
    except ValueError:
        print("Vamos, colaborá conmigo.")
        continue
message = input("Qué mensaje desea cifrar/descifrar: ")
for ch in message:
    pluscheck = ord(ch) + cipherange
    minuscheck = ord(ch) + cipherange * -1
    #print(pluscheck, minuscheck) #DEBUGGING
    if ch.isspace():
        forwards += " "
        backwards += " "
        continue
    elif ch.isalpha() != True:
        forwards += ch
        backwards += ch
        continue
    elif ch.islower() and pluscheck > 122: #Minúscula sobrepasa z hacia delante.
        pluscheck -= 26
        #print(pluscheck)
    elif ch.islower() and minuscheck < 97: #Minúscula sobrepasa a hacia atráss.
        minuscheck += 26
        #print(minuscheck)
    elif ch.isupper() and pluscheck > 90: #Mayúscula sobrepasa Z hacia adelanta.
        pluscheck -= 26
        #print(pluscheck)
    elif ch.isupper() and minuscheck < 65: #Mayúscula sobrepasa A hacia atrás.
        minuscheck += 26
        #print(minuscheck)
    forwards += chr(pluscheck)
    backwards += chr(minuscheck)
#print("original: ", message) #DEBUGGING
print(f"Cifrado hacia adelante {cipherange} espacio(s): {forwards}")
print(f"Cifrado hacia atrás {cipherange} espacio(s): {backwards}")
