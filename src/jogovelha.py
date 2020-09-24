def inicializar():
	tab = [ ]
	for II in range(3):
		linha = [ ]
		for j in range(3):
			linha.append(".")
		tab.ap pend(linha)
	return tab

def main( ):
	jogo = inicializar( )
	print (jogo)

if __name__ == "__main__":
        main()
