print("Olá mundo :D")

print("olá 2")


num = 10
num = "Adriel"
num = 10.98

a = num * 10

print( "O resultado é {}, certo ?".format(num) )

nome = "Adriel"
print( "{}, o resultado é {}, certo?".format(nome, num) )


num = 5 ** 2 #5 ao quadrado


if(num % 2 == 0):
    print("0 número {} é par !".format(num))

print("Fim do IF")

if(True):

        print("Pertence ao IF interno")

        while(True):
            print("Código do while")

            break

i = 0
num = input("Digite um número: ")
num = int(num)
   while(i <= 10):
       res = i * num
       print("{} X {} = {}".format(num,i,res))
       i += 1

vetor = []
vetor.append(10)

vetorDefinido = [""] * 10
vetorDefinido[0] = 19
vetorDefinido[1] = 5


vetor = [""] * 4
i = 0
while(i < len(vetor)):
    vetor[i] = int( input("Número: ") )
    i = i+1


for x in vetor:
    print("O vetor tem o valor {}".format(x) )


def somar(a,b,b):
    print(a+b+c)


class Aluno(Pessoa):
