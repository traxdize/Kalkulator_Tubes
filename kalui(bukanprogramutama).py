from tkinter import *

root = Tk()
root.title("Tubesio Calculator 9981fx-e")

global current_number, stored_number, current_operator
current_number = ''
stored_number = ''
current_operator = ''

# Opsi Awal
def OpsiAwal(choice):
    if choice == '0':
        root.destroy()
    elif choice == '1':
        Opdas()
        ButtonOpdas()
    elif choice == '2':
        trigonometry_root = Toplevel(root)
    elif choice == '3':
        statistic_root = Toplevel(root)

# Label opsi
label = Label(root, text='Opsi: ')
label.grid(row=0, column=1, columnspan=3, padx=100)

button1 = Button(root, text='1. Operasi Dasar', command=lambda: OpsiAwal('1'))
button2 = Button(root, text='2. Trigonometri', command=lambda: OpsiAwal('2'))
button3 = Button(root, text='3. Mode Statistik', command=lambda: OpsiAwal('3'))
button4 = Button(root, text='0. Akhiri Program', command=lambda: OpsiAwal('0'))

button1.grid(row=1, column=1, columnspan=3, padx=100)
button2.grid(row=2, column=1, columnspan=3, padx=100)
button3.grid(row=3, column=1, columnspan=3, padx=100)
button4.grid(row=4, column=1, columnspan=3, padx=100)

# Define operasi dasar
def Opdas():
    create_buttons(root)


# Define button opdas creation
def ButtonOpdas():
    def button_plus():
        global current_operator
        current_operator = '+'
        entry.insert('end', '+')

    buttonplus = Button(button_frame, text='+', padx=40, pady=20, command=lambda: handle_operator('+'))
    buttonminus = Button(button_frame, text='-', padx=40, pady=20, command=lambda: handle_operator('-'))
    buttonmultiply = Button(button_frame, text='x', padx=40, pady=20, command=lambda: handle_operator('x'))
    buttondivision = Button(button_frame, text='/', padx=40, pady=20, command=lambda: handle_operator('/'))
    buttonans = Button(button_frame, text='Ans', padx=40, pady=20, command=lambda: button_add(answer))
    buttonclear = Button(button_frame, text='AC', padx=40, pady=20, command=lambda: clear_screen())
    buttondivision.grid(row=0, column=4)
    buttonmultiply.grid(row=0, column=3)
    buttonplus.grid(row=1, column=3)
    buttonminus.grid(row=2, column=3)
    buttonans.grid(row = 2, column = 4)
    buttonclear.grid(row = 1, column = 4)

# Define kalkulator frame
def create_buttons(root):
    global window
    window = Toplevel(root)
    global entry
    entry = Text(window, width=50, height=10)
    entry.grid(row=0, column=0, columnspan=4)

    # Create a frame for buttons and use grid layout
    global button_frame
    button_frame = Frame(window)
    button_frame.grid(row=1, column=0, columnspan=5)

    global button_add
    def button_add(number):
        global current_number
        current_number += str(number)
        entry.insert('end', str(number))
    
    global clear_screen
    def clear_screen():
        entry.delete('1.0', 'end')

    global handle_operator
    def handle_operator(operator):
        global current_number, stored_number, current_operator
        if current_number:
            if stored_number != '' and current_operator:
                calculate_result()
            else:
                stored_number = current_number
            current_operator = operator
            current_number = ''
            entry.insert('end', operator)

    def calculate_result():
        global current_number, stored_number, current_operator, answer
        if stored_number and current_number and current_operator:
            num1 = int(stored_number)
            num2 = int(current_number)
            if current_operator == '+':
                result = num1 + num2
            elif current_operator == '-':
                result = num1 - num2
            elif current_operator == 'x':
                result = num1*num2
            elif current_operator == '/':
                result = num1/num2
            entry.delete('1.0', 'end')
            entry.insert('end', str(result))
            answer = str(result)
            current_number = ''
            current_operator = ''

    window.bind('<Return>', lambda event=None:calculate_result())

    # Define button creation
    button1 = Button(button_frame, text='1', padx=40, pady=20, command=lambda: button_add(1))
    button2 = Button(button_frame, text='2', padx=40, pady=20, command=lambda: button_add(2))
    button3 = Button(button_frame, text='3', padx=40, pady=20, command=lambda: button_add(3))
    button4 = Button(button_frame, text='4', padx=40, pady=20, command=lambda: button_add(4))
    button5 = Button(button_frame, text='5', padx=40, pady=20, command=lambda: button_add(5))
    button6 = Button(button_frame, text='6', padx=40, pady=20, command=lambda: button_add(6))
    button7 = Button(button_frame, text='7', padx=40, pady=20, command=lambda: button_add(7))
    button8 = Button(button_frame, text='8', padx=40, pady=20, command=lambda: button_add(8))
    button9 = Button(button_frame, text='9', padx=40, pady=20, command=lambda: button_add(9))
    button0 = Button(button_frame, text='0', padx=135, pady=20, command=lambda: button_add(0))
    buttonequal = Button(button_frame, text='=', padx=85, pady=20, command=lambda: calculate_result())

    # Place buttons in grid layout
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)
    button0.grid(row=3, column=0, columnspan=3)
    buttonequal.grid(row=3, column=3, columnspan=2)

# Main Loop
root.mainloop()
