b = 'diego num sabe é nada'

c = "o matheus é meu parceiro"

d = "Um dois tres"

e = "num sei, num consigo"

def funcao():
    alpha =input("Digite uma letra de c a e: ")
    if alpha == 'b':
        print(b)
    if alpha == "c":
        print(d, c)
    if alpha == 'd':
        print(d)
    else:
        print(e)

if __name__ == '__main__':
     capacitacao = funcao()   