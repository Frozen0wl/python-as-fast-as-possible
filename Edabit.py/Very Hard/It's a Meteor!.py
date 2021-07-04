def will_hit(equation, position):
	x = position[0]
	y = position[1]
	print(x, y)
	equation = "y ==" + equation[3::1]
	print(equation)
	print(eval(equation.replace('x', '*x')))
	return eval(equation.replace('x', '*x'))

will_hit("y = 2x - 5", (0, 0))