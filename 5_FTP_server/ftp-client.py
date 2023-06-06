import socket


# Функция для установления соединения с сервером
def connect_to_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket


# Функция для отправки запроса на сервер
def send_request(socket, request):
    socket.send(request.encode())


# Функция для получения ответа от сервера
def receive_response(socket):
    response = socket.recv(1024).decode()
    return response


# Функция для просмотра списка файлов и папок в текущей директории
def list_files(socket):
    send_request(socket, "LIST")
    response = receive_response(socket)
    print(response)


# Функция для создания папки
def create_directory(socket, directory_name):
    send_request(socket, f"MKDIR {directory_name}")
    response = receive_response(socket)
    print(response)


# Функция для удаления папки
def delete_directory(socket, directory_name):
    send_request(socket, f"RMDIR {directory_name}")
    response = receive_response(socket)
    print(response)


# Функция для удаления файла
def delete_file(socket, file_name):
    send_request(socket, f"DELETE {file_name}")
    response = receive_response(socket)
    print(response)


# Функция для переименования файла
def rename_file(socket, old_name, new_name):
    send_request(socket, f"RENAME {old_name} {new_name}")
    response = receive_response(socket)
    print(response)


# Функция для копирования файла с клиента на сервер
def upload_file(socket, file_name):
    send_request(socket, f"UPLOAD {file_name}")
    response = receive_response(socket)
    print(response)


# Функция для копирования файла с сервера на клиент
def download_file(socket, file_name):
    send_request(socket, f"DOWNLOAD {file_name}")
    response = receive_response(socket)
    print(response)


# Функция для получения содержимого файла
def get_file_content(socket, file_name):
    send_request(socket, f"GET {file_name}")
    response = receive_response(socket)
    print(response)


# Функция для отключения от сервера
def disconnect_from_server(socket):
    send_request(socket, "QUIT")
    socket.close()


# Пример использования клиента
def main():
    # Параметры подключения к серверу
    host = 'localhost'
    port = 8000

    # Подключение к серверу
    client_socket = connect_to_server(host, port)

    # Основной цикл работы клиента
    while True:
        command = input("Введите команду (LIST, MKDIR, RMDIR, DELETE, RENAME, UPLOAD, DOWNLOAD, GET, QUIT): ")

        if command == "LIST":
            list_files(client_socket)
        elif command == "MKDIR":
            directory_name = input("Введите название папки: ")
            create_directory(client_socket, directory_name)
        elif command == "RMDIR":
            directory_name = input("Введите название папки: ")
            delete_directory(client_socket, directory_name)
        elif command == "DELETE":
            file_name = input("Введите название файла: ")
            delete_file(client_socket, file_name)
        elif command == "RENAME":
            old_name = input("Введите текущее название файла: ")
            new_name = input("Введите новое название файла: ")
            rename_file(client_socket, old_name, new_name)
        elif command == "UPLOAD":
            file_name = input("Введите название файла для загрузки: ")
            upload_file(client_socket, file_name)
        elif command == "DOWNLOAD":
            file_name = input("Введите название файла для скачивания: ")
            download_file(client_socket, file_name)
        elif command == "GET":
            file_name = input("Введите название файла: ")
            get_file_content(client_socket, file_name)
        elif command == "QUIT":
            disconnect_from_server(client_socket)
            break
        else:
            print("Некорректная команда.")


if __name__ == '__main__':
    main()
