import multiprocessing
import socket

def server_process(connection, address):
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("process-%r" % (address,))
    try:
        logger.debug("Connected %r at %r", connection, address)
        while True:
            data = connection.recv(1024)
            if data == "":
                logger.debug("Socket closed remotely")
                break
            logger.debug("Received data %r", data)
            connection.sendall(data)
            logger.debug("Sent data")
    except:
        logger.exception("Problem handling request")
    finally:
        logger.debug("Closing socket")
        connection.close()


def client_process(sock):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    while True:
        data = "some data"
        sock.sendall(data)
        result = sock.recv(1024)
        sock.close()


class Client(object):
    def __init__(self, hostname, port):
        import logging
        self.logger = logging.getLogger("client")
        self.hostname = hostname
        self.port = port

    def start(self):
        self.logger.debug("sending")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.hostname, self.port))

        process = multiprocessing.Process(target=client_process, args=(sock))
        process.daemon = True
        process.start()

class Server(object):
    def __init__(self, hostname, port):
        import logging
        self.logger = logging.getLogger("server")
        self.hostname = hostname
        self.port = port

    def start(self):
        self.logger.debug("listening")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

        while True:
            conn, address = self.socket.accept()
            self.logger.debug("Got connection")
            process = multiprocessing.Process(target=server_process, args=(conn, address))
            process.daemon = True
            process.start()
            self.logger.debug("Started process %r", process)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    server = Server("0.0.0.0", 9000)
    try:
        server.start()
    except:
        logging.exception("Unexpected server exception")
    finally:
        logging.info("Shutting down server process")
        for current_server_process in multiprocessing.active_children():
            logging.info("Shutting down process %r", current_server_process)
            current_server_process.terminate()
            current_server_process.join()

    client = Client("0,0,0,0", 9000)
    try:
        client.start()
    except:
        logging.exception("Unexpected client exception")
    finally:
        logging.info("Shutting down client process")
        for current_client_process in multiprocessing.active_children():
            logging.info("Shutting down process %r", current_client_process)
            current_client_process.terminate()
            current_client_process.join()

    logging.info("All done")