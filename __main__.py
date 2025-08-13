import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

isExeFound = False

def get_target_folder(target_folder):
    global isExeFound
    while True:
        folder = filedialog.askdirectory(title="Виберіть папку з грою")
        if not folder:
            break

        if sys.platform == "darwin":  # macOS
            game_exe = os.path.join(folder, "Slay the Princess.app", "Contents", "MacOS", "Slay the Princess")
        else:  # Windows або інші
            game_exe = os.path.join(folder, "SlaythePrincess.exe")

        if not os.path.exists(game_exe):
            messagebox.showerror("Помилка", "Не знайдено виконуваний файл гри в обраній папці!")
            isExeFound = False
        else:
            target_folder.set(folder)
            isExeFound = True
            break

def main():
    root = tk.Tk()
    root.withdraw()  # ховаємо головне вікно
    target_folder = tk.StringVar()
    get_target_folder(target_folder)
    if isExeFound:
        messagebox.showinfo("Успіх", f"Гра знайдена у {target_folder.get()}")
    root.mainloop()

if __name__ == "__main__":
    main()
