import customtkinter as ctk
import math
import tkinter as tk
import random

window = ctk.CTk()
window.geometry("600x450")
window.title("(˶˃ ᵕ ˂˶)")
window.configure(fg_color = '#FADADD')

my_font1= ctk.CTkFont(family="Comic Sans MS", size = 30, weight = "bold")
my_font2 = ctk.CTkFont(family="Comic Sans MS", size = 20, weight = "bold")

QUESTIONS = [
    {
        "compliment": "Кто это тут такой хорошенький?",
        "good": "Я!!!",
        "bad": "Хз",
    },
    {
        "compliment": "Кто моя сладенькая булочка?",
        "good": "Я :3",
        "bad": "Отстань, дура",
    },
    {
        "compliment": "Кто мой самый-самый?",
        "good": "Это яяя",
        "bad": "Бесиш",
    },
    {
        "compliment": "Кого я очень-очень сильно люблюю?",
        "good": "Меня-меня",
        "bad": "Эм бож",
    },
]

label = ctk.CTkLabel(window, text= "Привет, котенок <3", font=my_font1, text_color = "#4a1516")
label.pack(pady = 40)

def next_screen(i):
    if i + 1 < len(QUESTIONS):
        show_question(i+1)
    else:
        show_final()

def fall(canvas, item, speed):
    canvas.move(item, 0, speed)
    x, y = canvas.coords(item)
    if y > 470:
        canvas.coords(item, random.randint(10, 590), -20)
    canvas.after(30, fall, canvas, item, speed)

def make_heart(canvas):
    x = random.randint(10, 590)
    y = random.randint(-300, -20)
    size = random.randint(14, 30)
    speed = random.randint(2, 6)
    color = random.choice(["#ff8a9b", "#ff6b81", "#b9394c", "#ffb3c1"])

    item = canvas.create_text(x, y, text="♥", font=("Segoe UI Symbol", size), fill=color)
    canvas.tag_lower(item)
    fall(canvas, item, speed)

def show_final():
    for widget in window.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(window, width=600, height=450, bg="#FADADD", highlightthickness=0)
    canvas.pack()

    points = []
    scale = 12
    center_x = 300
    center_y = 205

    for deg in range(0, 361, 3):
        t = math.radians(deg)
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        points.append((center_x + x * scale, center_y - y * scale))

    def draw(step):
        if step < len(points):
            canvas.create_line(points[step - 1], points[step], fill="#b9394c", width=4)
            window.after(15, draw, step + 1)
        else:
            canvas.create_polygon(points, fill="#b9394c", outline="")
            canvas.create_text(
                center_x, center_y - 15,
                text="Люблююю ⸜(｡˃ 3 ˂ )⸝♡",
                font=("Comic Sans MS", 30, "bold"),
                fill="white",
                width=300,
                justify="center",
            )
            for _ in range(25):
                make_heart(canvas)

    draw(1)

def run_away(button):
    while True:
        x = random.randint(10, 390)
        y = random.randint(120, 395)
        if not (x < 260 and y > 195):
            break
    button.place(x=x, y=y)

def show_question(i):
    for widget in window.winfo_children():
        widget.destroy()

    q = QUESTIONS[i]

    label1 = ctk.CTkLabel(window, text=q["compliment"], font=my_font1, text_color = "#4a1516")
    label1.pack(pady = 40)

    button1 = ctk.CTkButton(window, text  = q["good"], command=lambda: next_screen(i), fg_color="white", font = my_font2, text_color="#4a1516", width=200, height = 45, corner_radius=15,hover_color="#ff8a9b")
    button1.place(x=40, y=260)
    button2 = ctk.CTkButton(window, text  = q["bad"], command=lambda: run_away(button2), fg_color="white", font = my_font2, text_color="#4a1516", width=200, height = 45, corner_radius=15,hover_color="#ff8a9b")
    button2.place(x=600-40-200, y=260)
    button2.bind("<Enter>", lambda event: run_away(button2))


button = ctk.CTkButton(window, text  = "Начать", command=lambda: show_question(0), fg_color="white", font = my_font2, text_color="#4a1516", width=250, height = 45, corner_radius=15,hover_color="#ff8a9b")
button.pack()

window.mainloop()
