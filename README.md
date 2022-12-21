# SEL0337
Prática 6 - Aplicação de microprocessadores II

Luis Felipe dos Reis Feitosa 10821061
Eric Sonagli Abbade 10310505


NESTE ARQUIVO SE TEM A EXPLICAÇÃO DOS 2 CÓDIGOS DA PRÁTICA 6 (O DA CÂMERA E O DA ESTAÇÃO CLIMÁTICA)





EXPLICAÇÃO DO CÓDIGO PARA CONTROLAR A CÂMERA:


Será feita uma breve explicação sobre o código. Primeiramente se importou as bibliotecas necessárias, com as seguintes linhas:
from picamera import PiCamera
from time import sleep

Depois se inicializou a função da câmera, com os seguintes comandos da biblioteca PiCamera: 
camera = PiCamera()
camera.start_preview()

Como era um dos objetivos da prática que se escrevesse os números USPs da dupla na foto, se usou o seguinte comando para realizar tal tarefa: 
camera.annotate_text= '10821061 e 10310505'

Para que se esperasse um tempo de 5 segundos até tirar a foto se usou o seguinte comando: 
sleep(5)

Então finalmente, para que se pudesse tirar a foto salvando-a no local: “/home/sel/Desktop/foto_NUSPs”, usou-se o seguinte comando: 
camera.capture('/home/sel/Desktop/foto_NUSPs.jpg') 

Por fim, se encerrou a função da câmera, com os seguintes comandos da biblioteca PiCamera: 
camera.stop_preview()






EXPLICAÇÃO DO CÓDIGO DA ESTAÇÃO CLIMÁTICA:


Primeiro se importou as bibliotecas, com os seguintes comandos:
from requests import get
import json
from pprint import pprint

Depois se declararam as variáveis relativas aos URLs da estação climática e dos últimos dados de clima, com os seguintes comandos:
stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

Então, já que a estação climática mais próxima está desativada, conforme explicado e pedido pelo relatório, se usou a ID correspondente a base climática: ID 966583 (da base climática instalada na UFSC), com os seguintes comandos:
closest_stn = 966583 

Assim, se adicionou o valor mencionado acima (966583) ao final da variável: “weather” que armazena o URL mencionada anteriormente, com os seguintes comandos:
weather = weather + str(closest_stn)

Por fim, se usou requests para se conseguir os dados da estação climática e imprimi-los na tela, com os seguintes comandos:
my_weather = get(weather).json()['items']
pprint(my_weather)
