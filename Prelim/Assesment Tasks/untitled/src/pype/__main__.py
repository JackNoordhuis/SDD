from src.pype.Server import Server


def main():
    server = Server()
    server.interface.open_socket()

if __name__ == '__main__':
    main()
