import tkinter as tk
import ttkbootstrap as tp
import math as m

root = tp.Window(themename='cyborg')
root.title("Calculator Pro")
root.state("zoomed")

def change_theme(theme_name):
    root.style.theme_use(theme_name)
def clicked(value):
    display.config(state="normal")
    if value == "AC":
        display.delete(0, tk.END)
    elif value == "CE":
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current[:-1])
    elif value == "=":
        try:
            current = display.get()
            display.delete(0, tk.END)
            result = eval(current)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == "^":
        display.insert(tk.END, "**")
    elif value == "√":
        current = display.get()
        result = m.sqrt(float(current))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    else:
        display.insert(tk.END, value)
    display.config(state="readonly")


def click_btn(txt, r, c, style):
    tp.Button(button_frame, text=txt, bootstyle=style, **btn_params, command=lambda: clicked(txt)).grid(
        row=r, column=c, padx=10, pady=10)

themes = [
    "cyborg", "superhero", "darkly", "solar", "vapor",
    "cosmo", "flatly", "litera", "minty", "pulse"
]
theme_menu = tp.Menubutton(root, text="Themes", bootstyle="info-outline")
theme_menu.place(relx=0.13, rely=0.01, anchor="ne")

menu = tk.Menu(theme_menu, tearoff=False)
for t in themes:
    menu.add_command(label=t.title(), command=lambda t=t: change_theme(t))
theme_menu['menu'] = menu

button_frame = tk.Frame(root)
title = tp.Label(root, text="Welcome to Claculator Pro", font=("Arial", 10, 'bold'), bootstyle="primary")
title.place(relx=0.5, rely=0.25, anchor="n")
title = tp.Label(root, text="Normal Calculator", font=("Arial", 10, 'bold'), bootstyle="primary")
title.place(relx=0.5, rely=0.3, anchor="n")
button_frame.place(relx=0.5, rely=0.5, anchor="center")
display = tp.Entry(button_frame, font=("Arial", 10), justify="right", bootstyle="primary", state="readonly")
display.grid(row=0, column=1, columnspan=4, pady=20, padx=0, sticky="nsew", ipadx=40)
btn_params = {"width": 10, "padding": 15}
tp.Button(button_frame, text="CE", bootstyle="danger-outline-toolbutton", command=lambda: clicked("CE")).grid(
    row=1, column=1, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="7", bootstyle="info-outline-toolbutton", command=lambda: clicked("7")).grid(
    row=2, column=1, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="4", bootstyle="info-outline-toolbutton", command=lambda: clicked("4")).grid(
    row=3, column=1, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="1", bootstyle="info-outline-toolbutton", command=lambda: clicked("1")).grid(
    row=4, column=1, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="0", bootstyle="info-outline-toolbutton", command=lambda: clicked("0")).grid(
    row=5, column=1, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="^", bootstyle="info-outline-toolbutton", command=lambda: clicked("^")).grid(
    row=1, column=2, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="8", bootstyle="info-outline-toolbutton", command=lambda: clicked("8")).grid(
    row=2, column=2, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="5", bootstyle="info-outline-toolbutton", command=lambda: clicked("5")).grid(
    row=3, column=2, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="2", bootstyle="info-outline-toolbutton", command=lambda: clicked("2")).grid(
    row=4, column=2, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text=".", bootstyle="info-outline-toolbutton", command=lambda: clicked(".")).grid(
    row=5, column=2, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="AC", bootstyle="danger-outline-toolbutton", command=lambda: clicked("AC")).grid(
    row=1, column=4, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="√", bootstyle="info-outline-toolbutton", command=lambda: clicked("√")).grid(
    row=1, column=3, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="9", bootstyle="info-outline-toolbutton", command=lambda: clicked("9")).grid(
    row=2, column=3, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="6", bootstyle="info-outline-toolbutton", command=lambda: clicked("6")).grid(
    row=3, column=3, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="3", bootstyle="info-outline-toolbutton", command=lambda: clicked("3")).grid(
    row=4, column=3, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="=", bootstyle="primary-outline-toolbutton",
          command=lambda: clicked("=")).grid(row=5, column=3, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="/", bootstyle="success-outline-toolbutton",
          command=lambda: clicked("/")).grid(row=2, column=4, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="*", bootstyle="success-outline-toolbutton",
          command=lambda: clicked("*")).grid(row=3, column=4, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="-", bootstyle="success-outline-toolbutton",
          command=lambda: clicked("-")).grid(row=4, column=4, padx=10, pady=10, columnspan=1)
tp.Button(button_frame, text="+", bootstyle="success-outline-toolbutton",
          command=lambda: clicked("+")).grid(row=5, column=4, padx=10, pady=10, columnspan=1)
exit_btn = tp.Button(root, text="X", bootstyle="danger-outline-toolbutton", command=root.destroy)
exit_btn.place(relx=0.02, rely=0.05, anchor="s", width=50)
root.mainloop()