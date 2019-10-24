def retrocontador(e):
    print("{},".format(e), end="")
    if e <= 0:
        return
    
    retrocontador(e-1)

retrocontador(10)
