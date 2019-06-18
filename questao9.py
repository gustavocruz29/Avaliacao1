morango = float(input('Quanto Kg de morango você deseja: '))
maca = float(input('Quanto Kg de maçã você deseja: '))
precoMorango = 0
precoMaca = 0
totalKg = morango+maca
if morango > 5:
    precoMorango = morango*2.20
else:
    precoMorango = morango*2.50
if maca > 5:
    precoMaca = maca*1.50
else:
    precoMaca = maca*1.80
precoTotal = precoMorango+precoMaca
if (totalKg > 8) or (precoTotal > 25):
    precoTotal = precoTotal - (precoTotal*0.1)
print('você irá pagar:R$',precoTotal)
    
