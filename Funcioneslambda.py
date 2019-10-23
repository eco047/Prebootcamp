from Funciones1nivel import sumaTodos

#print(sumaTodos(3, lambda x: x**3))

#Ejemplo de funciones anonimas que se usan cuando es un codigo sencillo que no se va a reusar y que es
#autoexplicativo

doble = lambda x : x*2
triple = lambda x : x*3

print(sumaTodos(3, doble))
print(sumaTodos(3, triple))

