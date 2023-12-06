hello = int(input('Введите размер игрового квадратного поля (например, 3): '))
matrix_hello = []

#функция формирования квадратной матрицы по размеру, указанному пользователем:
def matrix_hello_func():
    k, t = 0, 0

    #строим матрицу, равную переменной 'hello' и заполняем элементами '-'
    for i in range(hello+1):
        row = []
        for j in range(hello+1):
            row.append('-')
        matrix_hello.append(row)

    #нумеруем строки и столбцы игрового поля:
    for i in range(hello+1):
        matrix_hello[0][i] = k
        k += 1
    for i in range(hello+1):
        matrix_hello[i][0] = t
        t += 1

    #вместо '0' в клетке 0:0 отобразим пустую ячейку ' ':
    matrix_hello[0][0] = ' '


#функция построения матрицы в нужном виде (отображении):
def matrix_func():
    for row in matrix_hello:
        for element in row:
            print(element, end=" ")
        print()


#функция для ввода 'X':
def x_func():
    x = (input("Укажите номер клетки для Х в формате 'номер по вертикали:номер по горизонтали' (пример - 1:2) "))
    x_row = int(x[:1])
    x_col = int(x[2:3])
    if matrix_hello[x_row][x_col] == "-":
        matrix_hello[x_row][x_col] = "X"
        matrix_func()
    else:
        print("Данная клетка занята.")
        x_func()

#функция для ввода '0':
def y_func():
    y = (input("Укажите номер клетки для 0 в формате 'номер по вертикали:номер по горизонтали' (пример - 2:2) "))
    y_row = int(y[:1])
    y_col = int(y[2:3])
    if matrix_hello[y_row][y_col] == "-":
        matrix_hello[y_row][y_col] = "0"
        matrix_func()
    else:
        print("Данная клетка занята.")
        y_func()


matrix_hello_func()
matrix_func()

def data_since_func():
    if (matrix_hello[1][1] == matrix_hello[1][2] == matrix_hello[1][3]!='-'
        or matrix_hello[2][1] == matrix_hello[2][2] == matrix_hello[2][3] != "-"
        or matrix_hello[3][1] == matrix_hello[3][2] == matrix_hello[3][3] != "-"
        or matrix_hello[1][1] == matrix_hello[2][1] == matrix_hello[3][1] != "-"
        or matrix_hello[1][2] == matrix_hello[2][2] == matrix_hello[3][2] != "-"
        or matrix_hello[1][3] == matrix_hello[2][3] == matrix_hello[3][3] != "-"
        or matrix_hello[1][1] == matrix_hello[2][2] == matrix_hello[3][3] != "-"
        or matrix_hello[3][1] == matrix_hello[2][2] == matrix_hello[1][3] != "-"):
        return True
    else:
        return False


count = 0
for i in range((hello**2)-1):

    x_func()
    if data_since_func() == True:
        print('Выиграл крестик!')
        break

    if data_since_func() == False and count == 4:
        print('Ничья!')
        break

    y_func()
    if data_since_func() == True:
        print('Выиграл нолик!')
        break

    count += 1