import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import rpatool  # Додано імпорт

def get_target_folder(target_folder):
    while True:
        folder = filedialog.askdirectory(title="Виберіть папку з грою")
        if not folder:
            return False

        if sys.platform == "darwin":
            game_exe = os.path.join(folder, "Slay the Princess.app", "Contents", "MacOS", "Slay the Princess")
        else:
            game_exe = os.path.join(folder, "SlaythePrincess.exe")

        if not os.path.exists(game_exe):
            messagebox.showerror("Помилка", "Не знайдено виконуваний файл гри в обраній папці!")
            continue
        else:
            target_folder.set(folder)
            return True

def main():
    root = tk.Tk()
    root.withdraw()
    target_folder = tk.StringVar()
    if get_target_folder(target_folder):
        messagebox.showinfo("Успіх", f"Гра знайдена у {target_folder.get()}")
    root.mainloop()

if __name__ == "__main__":
    main()