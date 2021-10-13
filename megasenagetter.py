import requests
from bs4 import BeautifulSoup as bs
from csv import DictWriter

print("\n\nAguarde um momento...")

url = "http://www.loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbwMPI0sDBxNXAOMwrzCjA0sjIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wNnUwNHfxcnSwBgIDUyhCvA5EawAjxsKckMjDDI9FQE-F4ca/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K8DBC0QPVN93KQ10G1/res/id=historicoHTML/c=cacheLevelPage/=/"

pagina = requests.get(url)
sopa = bs(pagina.text, "html.parser")

tr = sopa.find("tr")
td = tr.find_all("td")



#de 24 em 24 para mudar de linha

#3 - data 
# do 4 ao 9 são os números 

dados_brutos = []


for dado in td:
    try:
        d = int(dado.text)
    except:
        pass
    else:
        if len(dado.text) == 3 and dado.text[0] == '0':
            dados_brutos.append(int(dado.text))
    finally:
        try:
            if dado.text[2] == "/":
                dados_brutos.append(dado.text)
        except:
            pass
        
            

dados_prontos = []

array_temp = []

for dado in dados_brutos:
    array_temp.append(dado)
    if len(array_temp) == 7:
        dados_prontos.append(array_temp)
        array_temp = []
         
        
with open("dados_mega_sena.csv", "w", encoding="utf-8") as arquivo:
    cabecalho = ['Data', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6']
    escritor = DictWriter(arquivo, fieldnames=cabecalho)
    escritor.writeheader()
    for v in dados_prontos:
        escritor.writerow({"Data": v[0], 'N1':v[1], 'N2':v[2], 'N3':v[3], 'N4':v[4], 'N5':v[5], 'N6':v[6]})

print("\n\nInformações obtidas com sucesso")
        

    
    

    
    