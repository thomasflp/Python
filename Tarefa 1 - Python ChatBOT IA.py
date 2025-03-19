produtos = ["Calça Jeans", "Calça Moletom", "Camiseta de Algodão", "Blusa Moletom", "Meia Cano-Alto", "Shorts Jeans"]
precos = [120.00, 65.00, 30.00, 80.00, 20.00, 50.00]
quantidades = [40, 20, 120, 20, 45, 30]

valores = []
for i in range(len(precos)):
    valores.append(precos[i] * quantidades[i])

for i in range(len(produtos)):
    print(f"{produtos[i]}: R$ {valores[i]:.2f}")
