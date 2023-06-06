import os
import tkinter as tk
from tkinter import messagebox, filedialog


class FileManagerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Менеджер файлов")
        self.current_directory = os.getcwd()
        self.output_text = None
        self.input_entry = None

    def run(self):
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # Вывод текста
        self.output_text = tk.Text(self.root, width=80, height=20, state=tk.DISABLED)
        self.output_text.pack()

        # Ввод команды
        self.input_entry = tk.Entry(self.root, width=80)
        self.input_entry.pack()
        self.input_entry.bind("<Return>", self.process_command)

        # Изменение директории на текущую рабочую директорию
        self.cd_directory(self.current_directory)

    def process_command(self, event):
        command = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        self.execute_command(command)

    def execute_command(self, command):
        command_parts = command.split(" ")
        operation = command_parts[0]

        if operation == "ls":
            self.list_directory_contents()
        elif operation == "cd":
            if len(command_parts) > 1:
                directory_name = command_parts[1]
                self.cd_directory(directory_name)
        elif operation == "touch":
            if len(command_parts) > 1:
                file_name = command_parts[1]
                self.create_file(file_name)
        elif operation == "write":
            if len(command_parts) > 2:
                file_name = command_parts[1]
                content = " ".join(command_parts[2:])
                self.write_to_file(file_name, content)
        elif operation == "cat":
            if len(command_parts) > 1:
                file_name = command_parts[1]
                self.view_file_contents(file_name)
        elif operation == "exit":
            self.exit_file_manager()
        else:
            messagebox.showinfo("Недопустимая команда", "Введена недопустимая команда.")

    def list_directory_contents(self):
        self.output_text.config(state=tk.NORMAL)  # Включение редактирования вывода текста
        self.output_text.delete(1.0, tk.END)  # Очистка предыдущего вывода

        for item in os.listdir(self.current_directory):
            self.output_text.insert(tk.END, "{}\n".format(item))

        self.output_text.config(state=tk.DISABLED)  # Отключение редактирования вывода текста

    def cd_directory(self, directory_name):
        new_directory = os.path.join(self.current_directory, directory_name)
        if os.path.isdir(new_directory):
            self.current_directory = new_directory
            os.chdir(self.current_directory)
            self.list_directory_contents()
        else:
            messagebox.showinfo("Директория не найдена", "Директория '{}' не найдена.".format(directory_name))

    def create_file(self, file_name):
        try:
            file_path = os.path.join(self.current_directory, file_name)
            open(file_path, 'a').close()
            self.list_directory_contents()
        except PermissionError:
            messagebox.showinfo("Отказано в доступе", "Отказано в доступе.")

    def write_to_file(self, file_name, content):
        try:
            file_path = os.path.join(self.current_directory, file_name)
            with open(file_path, 'w') as file:
                file.write(content)
            self.list_directory_contents()
        except FileNotFoundError:
            messagebox.showinfo("Файл не найден", "Файл не найден.")
        except PermissionError:
            messagebox.showinfo("Отказано в доступе", "Отказано в доступе.")

    def view_file_contents(self, file_name):
        try:
            file_path = os.path.join(self.current_directory, file_name)
            with open(file_path, 'r') as file:
                contents = file.read()
            self.output_text.config(state=tk.NORMAL)  # Включение редактирования вывода текста
            self.output_text.delete(1.0, tk.END)  # Очистка предыдущего вывода
            self.output_text.insert(tk.END, contents)
            self.output_text.config(state=tk.DISABLED)  # Отключение редактирования вывода текста
        except FileNotFoundError:
            messagebox.showinfo("Файл не найден", "Файл не найден.")

    def exit_file_manager(self):
        self.root.destroy()


if __name__ == "__main__":
    file_manager = FileManagerGUI()
    file_manager.run()