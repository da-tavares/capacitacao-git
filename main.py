c = "o gabriel é meu parceiro"

d = "Um dois tres"

e = "num sei, num consigo"

def funcao():
    alpha =input("Digite uma letra de c a e: ")
    if alpha == "c": #precisaconferir
        print(d, c)
    if alpha == "d":#ta errado, arruma depois.
        print(d)
    else:
        print(e)

if __name__ == '__main__':
     capacitacao = funcao()   