from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.annotate_text= '10821061 e 10310505' #Linha para se escrever os números USPs da dupla na foto.
sleep(5)
camera.capture('/home/sel/Desktop/foto_NUSPs.jpg') #Linha para se informar o lugar onde se irá salvar a foto tirada.
camera.stop_preview()