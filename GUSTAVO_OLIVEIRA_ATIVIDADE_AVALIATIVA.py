#ATIVIDADE_AVALIATIVA
#Atividade baseada no algoritmo de chave pública RSA;
#Ler números positivos e inteiros, encerrando a leitura ao digitar "-1";
#Ignorar números negativos (exceto -1) e repetidos;
#Se o valor for primo considerar seus divs. 1 e ele mesmo;
#Armazenar números lidos no vetor 'vet_seu_nome';
#Armazenar primeiros divisores no vetor 'seu_nome_div1' e os segundos no 'seu_nome_div2'.

vet_gustavo = [0] * 10000
gustavo_div1 = [0] * 10
gustavo_div2 = [0] * 10
gustavo_div = [0] * 10
i = 0
d = 0

while True:
    nrepetido = False
    print("Digite um número inteiro e positivo: ")
    num = int(input())
    if num == -1:
        break
    vet_gustavo[i] = num
    if vet_gustavo[i] == 1 or vet_gustavo[i] == 0 or vet_gustavo[i] <= -2:
        print(f"{vet_gustavo[i]}, Invalido")
        continue
    for c in range(i):
        if vet_gustavo[c] == vet_gustavo[i]:
            nrepetido = True
    if not nrepetido and vet_gustavo[i] > 1:
        i += 1
        d += 1
print("\n" * 50)
print("=================================================")
print(f"FORAM DIGITADOS: {d} NÚMEROS COM DIVISORES")
print("=================================================")
print("ESSES SÃO OS NÚMEROS E SEUS DIVISORES:")
for c in range(d):
    print("")
    m = 0
    if vet_gustavo[c] <= 1:
        primo = False
    else:
        primo = True

    for i_div in range(2, vet_gustavo[c]):
        if vet_gustavo[c] % i_div == 0:
            primo = False

    if not primo:
        for g in range(2, vet_gustavo[c]):
            if vet_gustavo[c] % g == 0:
                m += 1
                if m == 1:
                    gustavo_div1[c] = g
                elif m == 2:
                    gustavo_div2[c] = g
                elif m > 2:
                    for n in range(m):
                        gustavo_div[c] = g
        if m == 1 or m == 2:
            print(f"{vet_gustavo[c]} tem divisores {gustavo_div1[c]} e {gustavo_div2[c]}")
        else:
            print(f"{vet_gustavo[c]} tem mais de 2 divisores, e são eles: ", end="")
            for g in range(2, vet_gustavo[c]):
                if vet_gustavo[c] % g == 0:
                    print(f"{g}, ", end="")
            print("")
    if m <= 2 and primo:
        gustavo_div1[c] = 1
        gustavo_div2[c] = vet_gustavo[c]
        print(f"{vet_gustavo[c]} tem divisores {gustavo_div1[c]} e {gustavo_div2[c]}")
    print("")