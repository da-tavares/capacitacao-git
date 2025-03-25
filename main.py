b = 'diego num sabe é nada'

c = "o matheus é meu parceiro"

d = "Um dois tres"

e = "num sei, num consigo"

def funcao():
    alpha =input("Digite uma letra de b a e: ")
    if alpha == 'b':
        print(b)  
    else:
        if alpha == 'c':
            print(c)
        else:
            if alpha == 'd':
                print(d)
            else:
                if alpha == 'e':
                    print(e)
                else:
                    print('você errou, começa de novo')

if __name__ == '__main__':
    funcao()   