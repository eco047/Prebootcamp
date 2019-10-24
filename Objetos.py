import turtle

#Creacion de un objeto del modulo turtle de tipo Turtle(clase de objeto siempre en mayuscula)
#Funciones de primer nivel capaces de invocarse a si mismas y generar copias de si mismas, por eso se crean con
#() y a veces con parametros de input

Leonardo = turtle.Turtle()
Rafael = turtle.Turtle()

Leonardo.shape('turtle')
Leonardo.fd(50)

Rafael.color('green')
Rafael.left(90)
Rafael.fd(50)
