def quantificarSaldo (vit, der): # função para calcular o saldo entre vitórias e derrotas
    saldo = vit - der
    return saldo

nome = input("Digite o nome do herói: ")
vitorias = int(input("Digite o número de vitórias: "))
derrotas = int(input("Digite o número de derrotas: "))

saldoTotal = quantificarSaldo (vitorias, derrotas)

if (saldoTotal <= 10):
    ranking = "Ferro"
elif (saldoTotal >= 11 and saldoTotal <= 20):
    ranking = "Bronze"
elif (saldoTotal >= 21 and saldoTotal <= 50):
    ranking = "Prata"    
elif (saldoTotal >= 51 and saldoTotal <= 80):
    ranking = "Ouro"  
elif (saldoTotal >= 81 and saldoTotal <= 90):
    ranking = "Diamante"                 
elif (saldoTotal >= 91 and saldoTotal <= 100):
    ranking = "Lendário"
elif (saldoTotal >= 101):
    ranking = "Imortal"  

print(f"O herói {nome} tem o saldo de {saldoTotal} e está no nível {ranking}.")                    