#funcion input -> retorna string
name = input ('Como te llamas?')
age = int (input('Cuantos años tienes? \n'))
future = int (input('Cuantos años mas? \n'))

print ("hola "+name)
print ("en "+str(future )+ " años tendras "+ str(age+future))

#Format strings 
"""
hola Luis, en 3 años tendras 21 años 
"""


text_complete = "Hola {} , en {} años tendras {} años "
print (text_complete.format(name, future, age+future))
print(f"hola {name}, en {future}años tendras {age+future}años ")