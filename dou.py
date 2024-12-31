import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
import os
import winsound

def verificar_expressao(valor, dia, i, tipo_jornal):
    url = "https://pesquisa.in.gov.br/imprensa/jsp/visualiza/index.jsp?jornal=" + tipo_jornal + "&pagina=1&data=" + dia + "&totalArquivos=947"

    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Analisa o conteúdo da página
        soup = BeautifulSoup(response.text, 'html.parser')

        #print(soup.get_text())
        
        # Verifica se a expressão "Sumário" está presente no conteúdo
        if valor in soup.get_text():
            print("Achei")
            while True:
                os.system('echo -e "\\a"')
                #winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)  # Emite um som padrão do sistema no Windows
                time.sleep(2)            
        else:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{current_time} - Continue tentando: {i}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return False

if __name__ == "__main__":
    i = 0
    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)  # Emite um som padrão do sistema no Windows
    while True:
        i = i + 1
        valor =  "Extra" #"Sumário"
        dia = "31/12/2024"
        tipo_jornal = "600" #515 = normal e 60X = extra
        verificar_expressao(valor, dia, i, tipo_jornal)
        time.sleep(5)
#Página 1 do Diário Oficial da União - Seção 1, número 250, de 30/12/2024 - Imprensa Nacional