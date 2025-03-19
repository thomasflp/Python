class Cubo:
	"""Classe que calcula o cubo de um número"""
	def __init__(self, valor):
		self.x = valor
		print('Cubo criado com sucesso!')
	def calcula_cubo(self):
		cubo = self.x ** 3
		return 'Cubo calculado: ' + str(cubo)

teste = Cubo(34)
c = teste.calcula_cubo()
print(c)