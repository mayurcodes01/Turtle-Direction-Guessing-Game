#Creator:Mayur Dhole
#Idea:self driven guessing system
import turtle
import random
import tkinter as tk
from tkinter import messagebox, ttk
screen=turtle.Screen()
screen.title("Turtle Direction Guessing Game - Play Well")
player=turtle.Turtle()
player.shape("turtle")
player.speed(1)
directions=["up","down","left","right"]
score=0
def move_turtle(direction):
    if direction=="up":
        player.setheading(90)
        player.forward(50)
    elif direction=="down":
        player.setheading(270)
        player.forward(50)
    elif direction=="left":
        player.setheading(180)
        player.forward(50)
    elif direction=="right":
        player.setheading(0)
        player.forward(50)

def make_guess(direction):
    global score
    actual=random.choice(directions)
    if direction==actual:
        score+=1
        result_label.config(text=f"Correct... Turtle moved: {actual.upper()}", fg="green")
    else:
        result_label.config(text=f"Wrong... Turtle moved: {actual.upper()}", fg="red")
    score_label.config(text=f"Score: {score}")
    move_turtle(actual)

def exit_game():
    app.destroy()
    screen.bye()

app = tk.Tk()
app.title("Direction Guessing Game GUI")
app.geometry("400x400")
app.config(bg="#1e1e2f")

title_label = tk.Label(app, 
                       text="Direction Guessing Game", 
                       font=("Arial", 20, "bold"),
                       fg="white", bg="#1e1e2f")
title_label.pack(pady=10)

score_label = tk.Label(app, 
                       text="Score: 0", 
                       font=("Arial", 16),
                       fg="cyan", bg="#1e1e2f")
score_label.pack(pady=5)

result_label = tk.Label(app, 
                        text="Click a direction to guess!",
                        font=("Arial", 14),
                        fg="white", bg="#1e1e2f")
result_label.pack(pady=10)

style = ttk.Style()
style.configure("TButton",
                font=("Arial", 14, "bold"),
                padding=10)

btn_frame = tk.Frame(app, bg="#1e1e2f")
btn_frame.pack(pady=20)

up_btn = ttk.Button(btn_frame, text="UP", width=10, command=lambda: make_guess("up"))
down_btn = ttk.Button(btn_frame, text="DOWN", width=10, command=lambda: make_guess("down"))
left_btn = ttk.Button(btn_frame, text="LEFT", width=10, command=lambda: make_guess("left"))
right_btn = ttk.Button(btn_frame, text="RIGHT", width=10, command=lambda: make_guess("right"))
up_btn.grid(row=0, column=1, padx=10, pady=10)
left_btn.grid(row=1, column=0, padx=10, pady=10)
right_btn.grid(row=1, column=2, padx=10, pady=10)
down_btn.grid(row=2, column=1, padx=10, pady=10)
exit_btn = ttk.Button(app, text="EXIT GAME", command=exit_game)
exit_btn.pack(pady=20)
app.mainloop()
