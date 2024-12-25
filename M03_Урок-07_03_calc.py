import tkinter as tk
# print(help(tk))
'''Функция(возвращающая) для ввода первого и второго числа'''
def get_vales():
    num1 = int(number1_entry.get())  # формируем ввод первого числа и переводим из формата str в int
    num2 = int(number2_entry.get())  # формируем ввод второго числа и переводим из формата str в int
    return num1, num2


'''Функция(принимающая) для вывода ответа'''
def insert_values(value):
    answer_entry.delete(0, 'end')  # очищаем текстовое поле ответа
    answer_entry.insert(0, value)  # формируем вывод ответа


''' функция сложения'''
def add():
    num1, num2 = get_vales()
    res = num1 + num2
    insert_values(res)

''' функция вычитания'''
def sub():
    num1, num2 = get_vales()
    res = num1 - num2
    insert_values(res)

''' функция деления'''
def div():
    num1, num2 = get_vales()
    res = num1 / num2
    insert_values(res)

''' функция умножения'''
def mul():
    num1, num2 = get_vales()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=2, height=2, command=add)  # связываем кнопку "+" с функцией "add()"
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text='-', width=2, height=2, command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text='/', width=2, height=2, command=div)
button_div.place(x=250, y=200)
number1_entry = tk.Entry(window, width=28)  # создаем текстовое поле для ввода и указываем его размер(длину)
number1_entry.place(x=100, y=75)  # формируем расположение текстового поля ввода  в окне "window"
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text='Введите первое число:')  # формируем информационное поле в окне "window"
number1.place(x=100, y=50)  # формруем расположение информационного поля в окне "window"
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=100, y=125)
answer = tk.Label(window, text='Ответ:')
answer.place(x=100, y=275)
window.mainloop()  # обновление экран окна "window"


