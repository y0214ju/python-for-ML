
def vector_size_check(*vector_variables):
    v = len(vector_variables[0])
    for v1 in vector_variables:
        if (len(v1) != v):
            return False
    return True

print(vector_size_check([1,2,3], [2,3,4], [5,6,7])) # Expected value: True
print(vector_size_check([1, 3], [2,4], [6,7])) # Expected value: True
print(vector_size_check([1, 3, 4], [4], [6,7])) # Expected value: False

def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [sum(elements) for elements in zip(*vector_variables)]


def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [elements[0]*2 - sum(elements) for elements in zip(*vector_variables)]


def scalar_vector_product(alpha, vector_variable):
    return [alpha * v for v in vector_variable]

print (scalar_vector_product(5,[1,2,3])) # Expected value: [5, 10, 15]
print (scalar_vector_product(3,[2,2])) # Expected value: [6, 6]
print (scalar_vector_product(4,[1])) # Expected value: [4]


def matrix_size_check(*matrix_variables):
    if vector_size_check(*matrix_variables) == False:
        return False
    for matrix_variable in matrix_variables:
        if vector_size_check(matrix_variable) == False:
            return False
    return True

def is_matrix_equal(*matrix_variables):
    m = matrix_variables[0]
    for matrix_variable in matrix_variables:
        if matrix_variable != m:
            return False
    return True


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError

    return [[sum(row)] for row in zip(*matrix)]
    for matrix in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[row[0] * 2 - sum(row) for row in zip(*matrix)]
            for matrix in zip(*matrix_variables)]

#need to fix
def matrix_transpose(matrix_variable):
    return [[element for element in row] for row in zip(*matrix_variable)]
    return zip(v for v in matrix_variable.split())


def scalar_matrix_product(alpha, matrix_variable):
    return [scalar_vector_product(alpha, row) for row in matrix_variable]



def is_product_availability_matrix(matrix_a, matrix_b):
    if len(col for col in zip(*matrix_a)) != len(matrix_b):
        return False
    return True


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError

    return [[sum(i*j) for i,j in zip(row, col)] for row in matrix_a
            for col zip(*matrix_b)]
