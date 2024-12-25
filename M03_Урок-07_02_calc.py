import tkinter as tk

window = tk.Tk() # создаем окно "window"
window.title('Калькулятор') # метод для наименования окна "window"
window.geometry('350x350') # формируем размер окна "window"
window.resizable(False, False) # закрепляем(невозможность изменять) размер окна "window")
button_add = tk.Button(window, text='+',  width=2, height=2) # создаем кнопку "+" и указываем размер кнопки
button_add.place(x=100, y=200) # формируем расположение кнопки в окне "window"
button_sub = tk.Button(window, text='-',  width=2, height=2)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text='*',  width=2, height=2)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text='/',  width=2, height=2)
button_div.place(x=250, y=200)
number1_entry = tk.Entry(window, width=28) # создаем текстовое поле для ввода и указываем его размер(длину)
number1_entry.place(x=100, y=75) # формируем расположение текстового поля ввода  в окне "window"
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text='Введите первое число:') # формируем информационное поле в окне "window"
number1.place(x=100, y=50) # формруем расположение информационного поля в окне "window"
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=100, y=125)
answer = tk.Label(window, text='Ответ:')
answer.place(x=100, y=275)


window.mainloop() # обновление экран окна "window"
