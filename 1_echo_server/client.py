import socket


def start_client():
    # Создание TCP-сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Получение имени хоста и порта сервера
    host = socket.gethostname()
    port = 12345

    try:
        # Подключение к серверу
        client_socket.connect((host, port))
        print("Соединение с сервером установлено")

        while True:
            # Ввод строки с клавиатуры
            message = input("Введите строку для отправки серверу: ")

            # Отправка данных серверу
            client_socket.send(message.encode())

            if message == "exit":
                break

            # Прием данных от сервера
            data = client_socket.recv(1024).decode()
            print("Получено от сервера:", data)

    except ConnectionRefusedError:
        print("Не удалось подключиться к серверу")

    # Закрытие соединения с сервером
    client_socket.close()
    print("Соединение с сервером закрыто")


# Запуск клиента
start_client()
