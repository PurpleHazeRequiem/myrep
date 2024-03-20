# Импорт модуля tkinter с псевдонимом tk
import tkinter as tk

# Функция обработки клика по кнопке
def on_click(button_value):
    # Получаем текущее значение в поле ввода
    current = entry.get()
    # Очищаем поле ввода
    entry.delete(0, tk.END)
    # Вставляем новое значение в поле ввода
    entry.insert(tk.END, current + button_value)

# Функция для вычисления
def calculate():
    try:
        # Вычисляем значение, введенное в поле ввода
        result = eval(entry.get())
        # Очищаем поле ввода
        entry.delete(0, tk.END)
        # Вставляем результат вычисления в поле ввода
        entry.insert(tk.END, str(result))
    except Exception as e:
        # В случае ошибки очищаем поле ввода и вставляем сообщение об ошибке
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

# Создаем главное окно
root = tk.Tk()
# Устанавливаем заголовок для основного окна
root.title("Калькулятор")

# Создаем поле ввода
entry = tk.Entry(root, width=20, font=('Arial', 16))
# Размещаем поле ввода в сетке основного окна
entry.grid(row=0, column=0, columnspan=4)

# Создаем список кнопок с символами и операторами
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

# Инициализируем переменные для управления расположением кнопок в сетке
row_val = 1
col_val = 0

# Создаем кнопки и размещаем их в сетке
for button in buttons:
    # Создаем кнопку с текстом из списка buttons
    # Привязываем функцию on_click к событию клика на кнопке, используя lambda
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    # Увеличиваем значение col_val для перемещения к следующему столбцу
    col_val += 1
    # Проверяем, достиг ли счетчик столбцов значения 3
    if col_val > 3:
        # Сбрасываем счетчик столбцов, если он превысил 3
        col_val = 0
        # Увеличиваем значение row_val для перемещения к следующей строке
        row_val += 1

# Создаем кнопку для вычисления и размещаем ее в сетке
tk.Button(root, text="=", width=5, height=2, command=calculate).grid(row=row_val, column=col_val)

# Устанавливаем размеры основного окна
root.geometry("250x200")

# Запускаем главный цикл событий tkinter
root.mainloop()