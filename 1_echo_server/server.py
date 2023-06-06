import socket


def start_server():
    # Создание TCP-сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Получение имени хоста и порта
    host = socket.gethostname()
    port = 12345

    # Привязка сокета к указанному хосту и порту
    server_socket.bind((host, port))

    # Начало прослушивания порта
    server_socket.listen(5)
    print("Сервер запущен. Ожидание подключений...")

    while True:
        # Принятие подключения от клиента
        client_socket, addr = server_socket.accept()
        print("Подключение от", addr)

        while True:
            # Получение данных от клиента
            data = client_socket.recv(1024).decode()

            if not data:
                break

            print("Получено от клиента:", data)

            # Проверка условия разрыва соединения
            if data == "exit":
                break

            # Отправка данных клиенту (эхо)
            client_socket.send(data.encode())

        # Закрытие соединения с клиентом
        client_socket.close()
        print("Клиент отключен")

        # Проверка условия разрыва соединения
        if data == "exit":
            break

    # Закрытие серверного сокета
    server_socket.close()
    print("Сервер остановлен")


# Запуск сервера
start_server()
