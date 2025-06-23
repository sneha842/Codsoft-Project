import tkinter as tk
import random

# Window setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.config(bg="#f2f2f2")

# Score
user_score = 0
comp_score = 0
choices = ["Rock", "Paper", "Scissors"]


def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)

    user_label.config(text=f"You chose: {user_choice}")
    comp_label.config(text=f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
            (user_choice == "Paper" and comp_choice == "Rock") or \
            (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        comp_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")


# Title
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#f2f2f2").pack(pady=20)

# Buttons
btn_frame = tk.Frame(root, bg="#f2f2f2")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play("Rock")).grid(row=0, column=0,
                                                                                                   padx=10)
tk.Button(btn_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: play("Paper")).grid(row=0, column=1,
                                                                                                     padx=10)
tk.Button(btn_frame, text="Scissors", font=("Arial", 14), width=10, command=lambda: play("Scissors")).grid(row=0,
                                                                                                           column=2,
                                                                                                           padx=10)

# Labels
user_label = tk.Label(root, text="", font=("Arial", 12), bg="#f2f2f2")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="", font=("Arial", 12), bg="#f2f2f2")
comp_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="#f2f2f2")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="#f2f2f2")
score_label.pack(pady=10)

tk.Button(root, text="Exit", command=root.quit, bg="#ff4d4d", fg="white", font=("Arial", 12)).pack(pady=20)

root.mainloop()
