def equipe1(numeros, proucurando_numeros):
    for numero in numeros:
      if numero == proucurando_numeros:
          return True
    return False

print(equipe1([1, 10, 20, 30, 50, 100], 30))

