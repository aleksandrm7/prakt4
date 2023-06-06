import socket
import os
import shutil


# Функция для обработки запросов от клиента
def handle_request(connection, address):
    while True:
        request = connection.recv(1024).decode().strip()

        if not request:
            break

        # Разбиение запроса на команду и аргументы
        command, *args = request.split()

        if command == "LIST":
            response = list_files()
        elif command == "MKDIR":
            response = create_directory(args[0])
        elif command == "RMDIR":
            response = delete_directory(args[0])
        elif command == "DELETE":
            response = delete_file(args[0])
        elif command == "RENAME":
            response = rename_file(args[0], args[1])
        elif command == "UPLOAD":
            response = upload_file(connection, args[0])
        elif command == "DOWNLOAD":
            response = download_file(connection, args[0])
        elif command == "GET":
            response = get_file_content(args[0])
        elif command == "QUIT":
            response = "Соединение закрыто."
            break
        else:
            response = "Некорректная команда."

        connection.send(response.encode())

    connection.close()


# Функция для получения списка файлов и папок в текущей директории
def list_files():
    files = os.listdir()
    response = "\n".join(files)
    return response


# Функция для создания папки
def create_directory(directory_name):
    os.mkdir(directory_name)
    response = f"Папка '{directory_name}' успешно создана."
    return response


# Функция для удаления папки
def delete_directory(directory_name):
    shutil.rmtree(directory_name)
    response = f"Папка '{directory_name}' успешно удалена."
    return response


# Функция для удаления файла
def delete_file(file_name):
    os.remove(file_name)
    response = f"Файл '{file_name}' успешно удален."
    return response


# Функция для переименования файла
def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
    response = f"Файл '{old_name}' успешно переименован в '{new_name}'."
    return response


# Функция для загрузки файла с клиента на сервер
def upload_file(connection, file_name):
    with open(file_name, 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)
    response = f"Файл '{file_name}' успешно загружен на сервер."
    return response


# Функция для скачивания файла с сервера на клиент
def download_file(connection, file_name):
    if file_name not in os.listdir():
        response = f"Файл '{file_name}' не существует на сервере."
        connection.send(response.encode())
        return

    with open(file_name, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            connection.send(data)

    response = f"Файл '{file_name}' успешно скачан с сервера."
    return response


# Функция для получения содержимого файла
def get_file_content(file_name):
    if file_name not in os.listdir():
        response = f"Файл '{file_name}' не существует на сервере."
        return response

    with open(file_name, 'r') as file:
        content = file.read()

    response = content
    return response


# Функция для запуска сервера
def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"FTP-сервер запущен на {host}:{port}")

    while True:
        connection, address = server_socket.accept()
        print(f"Установлено соединение с клиентом {address[0]}:{address[1]}")
        handle_request(connection, address)

    server_socket.close()


if __name__ == '__main__':
    start_server('localhost', 8000)
