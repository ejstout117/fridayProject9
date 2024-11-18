import tkinter as tk
from tkinter import messagebox
import openai
from dotenv import load_dotenv
import os

# Load API key from .env file with explicit path
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if not os.path.exists(dotenv_path):
    raise FileNotFoundError(f".env file not found at {dotenv_path}. Please create one with 'OPENAI_API_KEY'.")

load_dotenv(dotenv_path=dotenv_path)
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("API key not found in the .env file. Please ensure 'OPENAI_API_KEY' is set.")

def generate_completion():
    """Generate completion using OpenAI API."""
    prompt = input_box.get("1.0", tk.END).strip()
    if not prompt:
        messagebox.showwarning("Input Error", "Prompt cannot be empty!")
        return

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can change this to another model
            prompt=prompt,
            max_tokens=100
        )
        output = response.choices[0].text.strip()
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output)
        output_box.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("API Error", f"An error occurred: {str(e)}")

# Create the main application window
root = tk.Tk()
root.title("AI Completion GUI")
root.geometry("500x400")

# Input prompt box
tk.Label(root, text="Enter your prompt:").pack(pady=5)
input_box = tk.Text(root, height=5, width=50)
input_box.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=generate_completion)
submit_button.pack(pady=10)

# Output box
tk.Label(root, text="Output:").pack(pady=5)
output_box = tk.Text(root, height=10, width=50, state=tk.DISABLED, bg="#f0f0f0")
output_box.pack(pady=5)

# Run the application
root.mainloop()



