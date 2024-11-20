import tkinter as tk
from tkinter import messagebox
import openai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("API key not found. Please add 'OPENAI_API_KEY' to your .env file.")

def generate_completion():
    """Generate response using OpenAI Chat API."""
    prompt = input_box.get("1.0", tk.END).strip()
    if not prompt:
        messagebox.showwarning("Input Error", "Prompt cannot be empty!")
        return

    try:
        # Generate response using ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        output = response.choices[0].message.content.strip()
        output_box.config(state=tk.NORMAL, fg="black")  # Ensure output text is black
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output)
        output_box.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("API Error", f"An error occurred: {e}")

# Set up the GUI
root = tk.Tk()
root.title("AI Chat")
root.geometry("500x400")

tk.Label(root, text="Enter your prompt:").pack(pady=5)
input_box = tk.Text(root, height=5, width=50)
input_box.pack(pady=5)

tk.Button(root, text="Submit", command=generate_completion).pack(pady=10)

tk.Label(root, text="Output:").pack(pady=5)
output_box = tk.Text(root, height=10, width=50, state=tk.DISABLED, bg="#f0f0f0", fg="black")
output_box.pack(pady=5)

root.mainloop()

