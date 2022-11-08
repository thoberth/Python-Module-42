from vector import Vector

if (__name__ == "__main__"):
	v1 = Vector([[3.0], [4.0], [5.0], [6.0], [7.0]])
	print(v1.shape)
	print('Value = ', v1.values)
	print('T() Value = ', v1.T().values, v1.T().shape, '\n\n')

	v2 = Vector([[3.0, 4.0, 5.0, 6.0, 7.0]])
	print(v2.shape)
	print('Value = ', v2.values)
	print('T() Value = ', v2.T().values, v2.T().shape,'\n\n')

	try:
		5 / v2
	except NotImplementedError as error:
		print(error, "\n\n")

	try:
		v2 / 0
	except ZeroDivisionError as error:
		print(error, "\n\n")

	print('v2 / 2 = ', v2 / 2, "\n\n")

	print('v1 / 3 = ', v1 / 3, "\n\n")

	print('v2 * 2 = ', v2 * 2, "\n\n")

	print('v1 * 3 = ', v1 * 3, "\n\n")

	print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
	print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)

# Example 2:
	v3 = Vector([[0.0, 1.0, 2.0, 3.0]])
	print(v3.shape)
# Expected output:
# (1,4)

	print(v3.T())
# Expected output:
# Vector([[0.0], [1.0], [2.0], [3.0]])

	print(v3.T().shape)
# Expected output:
# (4,1)
	print(Vector(3))
	print(Vector(3, 12), '\n\n')

	print(v1.dot(v2.T()), '\n\n')
	print(v2.dot(v1.T()), '\n\n')

	print("Sum of Vector:\n", v2 + v1.T())
	print(v2.T() + v1, "\n\n")

	print("Subtraction of Vector:\n", v2 - v1.T())
	print(v2.T() - v1, "\n\n")