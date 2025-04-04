#Ejercicio 1
zen_text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
"""lista = zen_text.split('.')
word= "aeiouAEIOU"
nueva_lista= [oracion.strip().split() for oracion in lista]
num= len(lista)
for i in range(num):
    print(lista[i] if nueva_lista[i][1][0] in word else '.')"""

rules = """Respeta a los demás. No se permiten insultos ni lenguaje
 ofensivo.
 Evita el spam. No publiques enlaces sospechosos o repetitivos.
 No compartas información personal.
 Usa los canales adecuados para cada tema.
 Sigue las instrucciones de los moderadores."""
"""list = rules.split('.')
new_list = [rule.strip().split() for rule in list]
word = input('Ingrese una palabra clave: ')
for i in range(len(list)):
    print(list[i] if word in new_list[i] else ")"""

"""usuario= input('Ingrese un nombre de usuario: ')
cumple= False
num="0123456789"
if len(usuario) >= 5:
    for letter in usuario:
        if letter in num:
            cumple = True
print(cumple)"""

usuario= input('Ingrese un nombre de usuario: ')
requisito_uno = False
if len(usuario) >= 5:
    requisito_uno = True
requisito_dos = False
for letter in usuario:
    if letter>= "0" and letter<= "9":
        requisito_dos= True 
requisito_tres= False
for letter in usuario:
    if letter >= "A" and letter <= "Z":
        requisito_tres = True
requisito_cuatro = True
for letter in usuario:
        if not(48 <= ord(letter) <= 57 or 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122):
           requisito_cuatro = False
print(requisito_cuatro)
if ((requisito_uno) and (requisito_dos) and (requisito_tres) and (requisito_cuatro)):
    print('El nombre de usuario es valido')
else:
    print('El nombre de usuario no cumple con los requisitos')
    