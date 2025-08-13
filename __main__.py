import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import rpatool
import logging
import subprocess

logging.basicConfig(level=logging.INFO)

class LocalizationInstaller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.game_path = ""
        self.mod_files = [
            "mod/scripts.rpa",
            "mod/images.rpa",
            "mod/audio.rpa"
        ]

    def find_game(self):
        while True:
            try:
                folder = filedialog.askdirectory(title="Виберіть папку з грою Slay the Princess")
                if not folder:
                    return False

                exe_path = self._get_executable_path(folder)
                if not os.path.exists(exe_path):
                    messagebox.showerror("Помилка", "Не знайдено виконуваний файл гри в обраній папці!")
                    continue

                self.game_path = folder
                logging.info(f"Гра знайдена у: {self.game_path}")
                return True

            except Exception as e:
                logging.error(f"Помилка пошуку гри: {e}")
                messagebox.showerror("Помилка", f"Сталася помилка: {e}")
                return False

    def _get_executable_path(self, folder):
        if sys.platform == "darwin":
            return os.path.join(folder, "Slay the Princess.app", "Contents", "MacOS", "Slay the Princess")
        return os.path.join(folder, "SlaythePrincess.exe")

    def install_mod(self):
        try:
            # Створюємо папку для бекапу
            backup_dir = os.path.join(self.game_path, "backup_original")
            os.makedirs(backup_dir, exist_ok=True)

            # Копіюємо оригінальні файли
            for mod_file in self.mod_files:
                original_file = os.path.join(self.game_path, os.path.basename(mod_file))
                if os.path.exists(original_file):
                    shutil.copy2(original_file, backup_dir)

            # Встановлюємо мод
            for mod_file in self.mod_files:
                target = os.path.join(self.game_path, os.path.basename(mod_file))
                shutil.copy2(mod_file, target)

            messagebox.showinfo("Успіх", "Українська локалізація успішно встановлена!\n\n"
                                "Оригінальні файли збережено в папці 'backup_original'.")
            return True

        except Exception as e:
            logging.error(f"Помилка встановлення: {e}")
            messagebox.showerror("Помилка", f"Помилка встановлення: {e}")
            return False

    def run(self):
        if self.find_game():
            if messagebox.askyesno("Підтвердження", 
                                 f"Встановити українську локалізацію для гри у папці:\n{self.game_path}?"):
                if self.install_mod():
                    if messagebox.askyesno("Завершено", "Інсталяція завершена. Запустити гру?"):
                        exe_path = self._get_executable_path(self.game_path)
                        try:
                            if sys.platform == "darwin":
                                subprocess.Popen(["open", os.path.dirname(os.path.dirname(os.path.dirname(exe_path)))])
                            else:
                                subprocess.Popen([exe_path])
                        except Exception as e:
                            logging.error(f"Помилка запуску гри: {e}")

if __name__ == "__main__":
    app = LocalizationInstaller()
    app.run()