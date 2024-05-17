#Impoetación de libreria_personalizada
import sys

from librerias_personalizadas import goodbye#hello

if len(sys.argv) == 2:
    goodbye(sys.argv[1])#hello(sys.argv[1])