#importando a biblioteca para utilziar a câmera
from picamera import PiCamera
from time import sleep

#definindo câmera
camera = PiCamera()

#definição de resolução e framerate
camera.resolution = (2592, 1944)
camera.framerate = 15

camera.start_preview()

#local para salvar e texto para aparecer na imagem
camera.annotate_text = "11954158"
sleep(2)
camera.capture('/home/sel/SEL0337/11954158/image.jpg')

camera.stop_preview()
