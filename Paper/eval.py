def calculator(num1, operator, num2):
	return "Can't divide by 0!" if num2==0 and operator=='/' else eval(str(num1) + operator + str(num2))