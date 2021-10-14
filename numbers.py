
import math
import turtle

parametr = 30
diag = math.sqrt(2) * parametr
dlina = parametr
const_of_delta_x = 30



#one
def number_one(delta_x):
    turtle.shape('turtle')
    turtle.forward(2 * dlina)
    turtle.left(135)
    turtle.forward(diag)

    turtle.penup()
    turtle.left(90)
    turtle.forward(diag)
    turtle.left(45)
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.pendown()



#two
def number_two(delta_x):
    turtle.left(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)

    turtle.penup()
    turtle.left(90)
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(3 * dlina)
    turtle.left(90)
    turtle.pendown()



def number_three(delta_x):
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(180)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(180)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)

    turtle.penup()
    turtle.left(90)
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(3 * dlina)
    turtle.left(90)
    turtle.pendown()



def number_four(delta_x):
    turtle.forward(2 * dlina)
    turtle.left(180)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)

    turtle.penup()
    turtle.left(180)
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(3 * dlina)
    turtle.left(90)
    turtle.pendown()



def number_five(delta_x):
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(180)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.left(180)
    turtle.forward(dlina)

    turtle.penup()
    turtle.left(90)
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(3 * dlina)
    turtle.left(90)
    turtle.pendown()

def number_six(delta_x):
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.left(180)
    turtle.forward(dlina)

    turtle.penup()
    turtle.left(90)
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(3 * dlina)
    turtle.left(90)
    turtle.pendown()


def number_seven(delta_x):
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(dlina)

    turtle.penup()
    turtle.left(90)
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(3 * dlina)
    turtle.left(90)
    turtle.pendown()


def number_eight(delta_x):
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)

    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(dlina)


    turtle.penup()
    turtle.left(90)
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(3 * dlina)
    turtle.left(90)
    turtle.pendown()



def number_nine(delta_x):
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(180)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.left(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(dlina)

    turtle.penup()
    turtle.left(180)
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(3 * dlina)
    turtle.left(90)
    turtle.pendown()


def number_zero(delta_x):
    turtle.left(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(2 * dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(2 * dlina)
    turtle.right(90)
    turtle.forward(dlina)
    turtle.right(90)
    turtle.forward(2 * dlina)


    turtle.penup()
    turtle.left(180)
    turtle.forward(2 * dlina)
    turtle.left(90)
    turtle.forward(3 * dlina)
    turtle.left(90)
    turtle.pendown()


print('Введите комбинацию из цифр')
input_c = input()
list_of_numbers = []

turtle.left(90)
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()

try:
    for item in input_c:
        if int(item) == 1:
            list_of_numbers.append(number_one)
        elif int(item) == 2:
            list_of_numbers.append(number_two)
        elif int(item) == 3:
            list_of_numbers.append(number_three)
        elif int(item) == 4:
            list_of_numbers.append(number_four)
        elif int(item) == 5:
            list_of_numbers.append(number_five)
        elif int(item) == 6:
            list_of_numbers.append(number_six)
        elif int(item) == 7:
            list_of_numbers.append(number_seven)
        elif int(item) == 8:
            list_of_numbers.append(number_eight)
        elif int(item) == 9:
            list_of_numbers.append(number_nine)
        elif int(item) == 0:
            list_of_numbers.append(number_zero)


except ValueError:
        print('Вы ввели некоректную строку')

alpha_x=0

for i in range(len(list_of_numbers)):
    alpha_x = alpha_x + const_of_delta_x + dlina
    list_of_numbers[i](alpha_x)

x = input()