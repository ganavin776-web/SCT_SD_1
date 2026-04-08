import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance

def convert():
    try:
        temp = float(entry.get())
        choice = var.get()

        if choice == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result_label.config(text=f"Fahrenheit: {f:.2f}\nKelvin: {k:.2f}")

        elif choice == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result_label.config(text=f"Celsius: {c:.2f}\nKelvin: {k:.2f}")

        elif choice == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result_label.config(text=f"Celsius: {c:.2f}\nFahrenheit: {f:.2f}")

    except:
        result_label.config(text="Enter valid number!")

# Window
root = tk.Tk()
root.title("Temperature Converter")
root.state('zoomed')  # Full screen

# Screen size
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Load image
bg_image = Image.open("bg.jpg")

# --- PERFECT FIT (crop + resize) ---
img_width, img_height = bg_image.size
screen_ratio = width / height
img_ratio = img_width / img_height

if img_ratio > screen_ratio:
    new_width = int(img_height * screen_ratio)
    left = (img_width - new_width) // 2
    bg_image = bg_image.crop((left, 0, left + new_width, img_height))
else:
    new_height = int(img_width / screen_ratio)
    top = (img_height - new_height) // 2
    bg_image = bg_image.crop((0, top, img_width, top + new_height))

bg_image = bg_image.resize((width, height))

# Slight dim
enhancer = ImageEnhance.Brightness(bg_image)
bg_image = enhancer.enhance(0.7)

bg = ImageTk.PhotoImage(bg_image)

# Canvas
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, image=bg, anchor="nw")

# UI
var = tk.StringVar(value="Celsius")

canvas.create_text(width//2, 80,
                   text="🌡 Temperature Converter",
                   font=("Arial", 28, "bold"),
                   fill="white")

entry = tk.Entry(root, font=("Arial", 16), justify="center")
canvas.create_window(width//2, 180, window=entry)

dropdown = tk.OptionMenu(root, var, "Celsius", "Fahrenheit", "Kelvin")
canvas.create_window(width//2, 240, window=dropdown)

button = tk.Button(root, text="Convert",
                   font=("Arial", 14, "bold"),
                   bg="#4CAF50", fg="white",
                   command=convert)
canvas.create_window(width//2, 300, window=button)

result_label = tk.Label(root, text="",
                        font=("Arial", 16, "bold"),
                        bg="black", fg="white")
canvas.create_window(width//2, 380, window=result_label)

root.mainloop()