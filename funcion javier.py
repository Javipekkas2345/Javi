def entrada():
     contador = 1
     print("¿desea entrar a la aplicacion del robot?")
     print("pulse 1 para entrar")
     print("pulse 2 para no entrar")
     while(contador==1):
          contador = int(input())
          if(contador==1):
               print("usted ha escogido entrar a la aplicacion")
               print("si quiere salir pulse 2")
               contador==int(input())
          elif(contador==2):
               print("usted ha escogido no entrar a la aplicacion")