import tkinter as tk
from tkinter import messagebox

# Quiz questions and answers 
quiz_data = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Pune", "Chennai"],
        "correct_answer": "Delhi",
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "correct_answer": "4",
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Venus", "Jupiter", "Mars", "Neptune"],
        "correct_answer": "Mars",
    },
    {
        "question": "Who invented Zero?",
        "options": ["Oppenheminer", "Mithlesh", "Aryabhatta", "Adison"],
        "correct_answer": "Aryabhatta",
    },
]

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.current_question = 0

        self.title("Quiz Game By Mithlesh")
        self.geometry("600x500")

        self.label_question = tk.Label(self, text="", wraplength=300, font=('Book Antiqua', 20, 'bold'))
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set(-1) 

        self.radio_buttons = []
        for i in range(4):
            radio = tk.Radiobutton(self, text="", variable=self.radio_var, value=i)
            self.radio_buttons.append(radio)
            radio.pack()

        self.button_next = tk.Button(self, text="Next", command=self.next_question, font=('Book Antiqua', 12, 'bold'))
        self.button_next.pack(pady=10)
        self.load_question(0)

    def load_question(self, question_index):
        if question_index < len(quiz_data):
            self.label_question.config(text=quiz_data[question_index]["question"])
            for i in range(4):
                self.radio_buttons[i].config(text=quiz_data[question_index]["options"][i], font=('Book Antiqua', 15, 'bold'))
        else:
            self.show_result()

    def next_question(self):
        selected_option = int(self.radio_var.get())

        if selected_option == -1:
            messagebox.showwarning("Warning", "Please select an option.", font=('Book Antiqua', 10, 'bold'))
        else:
            correct_answer = quiz_data[self.current_question]["correct_answer"]
            if quiz_data[self.current_question]["options"][selected_option] == correct_answer:
                self.score += 1

            self.current_question += 1
            self.radio_var.set(-1)  

            if self.current_question < len(quiz_data):
                self.load_question(self.current_question)
            else:
                self.show_result()

    def show_result(self):
        messagebox.showinfo("Result", f"You scored {self.score}/{len(quiz_data)}")
        self.quit()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()