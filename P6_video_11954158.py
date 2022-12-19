#importando as bibliotecas necessárias
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()

#texto para escrever junto a imagem da câmera
camera.annotate_text = "11954158"

#iniando gravação e local onde salvar
camera.start_recording('/home/sel/SEL0337/11954158/video.h264')
sleep(5)

#finalizando gravação
camera.stop_recording()
camera.stop_preview()
