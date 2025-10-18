#Convertor de temperatura de Kelvin,Celsius e Fahrenheit

def clsFar(nmr):
   return (nmr * 1.8)+32

def clsKel(nmr):
   return nmr+273.15

def farCel(nmr):
   return (nmr-32)/1.8

def farKel(nmr):
   return ((nmr-32)/1.8)+273.15

def kelFar(nmr):
   return ((nmr-273.15)*1.8)+32

def kelCel(nmr):
   return nmr-273.15

while True:
   print("1 - Celsius para Fahrenheit\n" "2 - Celsius para Kelvin\n" "3 - Fahrenheit para Celsius\n" "4 - Fahrenheit para Kelvin\n" "5 - Kelvin para Fahrenheit\n" "6 - Kelvin para Celsius")
   opcoes ={
      1 : clsFar,
      2 : clsKel,
      3 : farCel,
      4 : farKel,
      5 : kelFar,
      6 : kelCel
   }
   opcao = int(input("Digite a opção que você deseja ultilizar: "))
   if opcao in opcoes:
      temperatura = float(input("Digite a temperatura: "))
      resultado = opcoes[opcao](temperatura)
      print(f"Temperatura convertida: {resultado:.2f}")
   else:
      print("Opção inválida, tente novamente!")



      

