def snakefill(n):
	i = 1
	while n*n >= (2**i):
		i += 1
	print(i-1)

snakefill(900)