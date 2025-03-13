from tkinter import *

def button_press(num):
    global equation_text

    if equation_label.get() == "A expressão\nerrada":
        equation_label.set(" ")
    equation_text += str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text, history
    try:
        total = str(eval(equation_text.replace("x", "*")))
        equation_label.set(total)
        history.append(equation_text + " = " + total)
        if len(history) > 5:
            history.pop(0)  # Mantém apenas os últimos 5 cálculos
        equation_text = total
    except:
        equation_label.set("A expressão\nerrada")
        equation_text = ""

def clear():
    global equation_text

    equation_label.set("")
    equation_text = ""

def show_history():
    history_window = Toplevel(window)
    history_window.title("Histórico de Cálculos")
    history_window.geometry("300x200")
    
    Label(history_window, text="Últimos 5 cálculos:", font=("consolas", 20, "bold")).pack()
    for calc in history:
        Label(history_window, text=calc, font=("consolas", 15)).pack()

window = Tk()
window.title("Calculadora do William")
window.geometry("500x550")

equation_text = ""
equation_label = StringVar()
history = [] 

label = Label(window, textvariable=equation_label, font=("consolas",35),
              bg="white",width=15,height=2)
label.pack()

frame = Frame(window)
frame.pack()

# Botões dos números
buttons = []
number = 9
for num in range(3):
    for column in range(3):
        btn = Button(frame,text=number,height=4,width=9,font=35,
                        command=lambda num=number: button_press(num))
        btn.grid(row=num,column=column)
        buttons.append(btn)
        number -= 1

btn = Button(frame,text=number,height=4,width=9,font=35,
                        command= lambda:button_press(number))
btn.grid(row=3,column=1)

# Botões dos sinais

# Virgula
float_point = Button(frame,text=",",height=4,width=9,font=35,bg="#3933E0", fg="white",
                        command= lambda:button_press("."))
float_point.grid(row=3,column=0)
# Resultado
equal = Button(frame,text="=",height=4,width=9,font=100,bg="#3933E0", fg="white",
                        command= lambda:equals())
equal.grid(row=3,column=2)
# Soma
sum = Button(frame,text="+",height=4,width=9,font=35,bg="#3933E0", fg="white",
                        command= lambda:button_press("+"))
sum.grid(row=0,column=3)
# Subtração
subtrac = Button(frame,text="-",height=4,width=9,font=35,bg="#3933E0", fg="white",
                        command= lambda:button_press("-"))
subtrac.grid(row=1,column=3)
# Divisão
division = Button(frame,text="/",height=4,width=9,font=35,bg="#3933E0", fg="white",
                        command= lambda:button_press("/"))
division.grid(row=2,column=3)
# Multiplicação
multiply = Button(frame,text="x",height=4,width=9,font=35,bg="#3933E0", fg="white",
                        command= lambda:button_press("x"))
multiply.grid(row=3,column=3)

# Botão de limpar
clear_btn = Button(frame, text="Limpar", height=4, width=9, font=35, bg="Red", fg="white",
                   command=clear)
clear_btn.grid(row=4, column=0)

# Botão para exibir histórico
display_history_btn = Button(frame, text="Histórico", height=4, width=9, font=35, bg="#28A745", fg="white", 
                             command=show_history)
display_history_btn.grid(row=4, column=1, columnspan=1)

window.mainloop()