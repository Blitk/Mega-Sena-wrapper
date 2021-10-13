
dados = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0, "30": 0, "31": 0, "32": 0, "33": 0, "34": 0, "35": 0, "36": 0, "37": 0, "38": 0, "39": 0, "40": 0, "41": 0, "42": 0, "43": 0, "44": 0, "45": 0, "46": 0, "47": 0, "48": 0, "49": 0, "50": 0, "51": 0, "52": 0, "53": 0, "54": 0, "55": 0, "56": 0, "57": 0, "58": 0, "59": 0, "60": 0}

with open("dados_mega_sena.csv", "r") as arquivo:
    for linha in arquivo:
        dado = linha.split(",")
        for item in dado:
            try:
                num = int(item)
            except:
                pass
            else:
                dados[f"{num}"] += 1
                

print("\n FREQUÊNCIA\n")
for i in sorted(dados, key = dados.get, reverse=True):
    print(f"\n{i} já apareceu {dados[i]} vezes")


print("\n PORCENTAGEM\n")
for i in sorted(dados, key = dados.get, reverse=True):
    porc = round((dados[i]*100)/2417, 2)
    print(f"\n{i} tem {porc}% de frequencia")
print("\n")
