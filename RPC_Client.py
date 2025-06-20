import xmlrpc.client

class RPC_Client:
    def __init__(self):
        self.proxy = None
        self.server_url = None

    def connect_to_server(self, server_url="http://ip address:8000"):
        self.server_url = server_url
        try:
            self.proxy = xmlrpc.client.ServerProxy(self.server_url)
            print(f"Connected to RPC Server at {self.server_url}")
            return self.proxy, True
        except ConnectionRefusedError as e:
            print(f"Error: Could not connect to server at {self.server_url}. {e}")
            self.proxy = None
            return None, False

    def call_add(self, x, y):
        if self.proxy:
            try:
                result = self.proxy.add(x, y)
                print(f"{x} + {y} = {result}")
                return result
            except xmlrpc.client.Fault as e:
                print(f"Server Fault: {e}")
            except ConnectionRefusedError as e:
                print(f"Error: Connection to server refused. {e}")
        return None

    def call_subtract(self, x, y):
        if self.proxy:
            try:
                result = self.proxy.subtract(x, y)
                print(f"{x} - {y} = {result}")
                return result
            except xmlrpc.client.Fault as e:
                print(f"Server Fault: {e}")
            except ConnectionRefusedError as e:
                print(f"Error: Connection to server refused. {e}")
        return None

    def call_unknown_function(self, func_name, *args):
        if self.proxy:
            try:
                result = getattr(self.proxy, func_name)(*args)
                print(f"Call to '{func_name}' with {args} returned: {result}")
                return result
            except xmlrpc.client.Fault as e:
                print(f"Server Fault: {e}")
            except AttributeError:
                print(f"Error: Function '{func_name}' not found on the server.")
            except ConnectionRefusedError as e:
                print(f"Error: Connection to server refused. {e}")
        return None

if __name__ == '__main__':
    client = RPC_Client()
    if client.connect_to_server("http://ip address:8000"):
        client.call_add(5, 3)
        client.call_subtract(10, 4)
        client.call_unknown_function("multiply", 2, 6)








































# # client.py
# import xmlrpc.client

# if __name__ == '__main__':
#     # Create a client proxy to connect to the server
#     with xmlrpc.client.ServerProxy("http://192.168.8.212:8000") as proxy:
#         # Call the 'add' function on the server
#         result_add = proxy.add(5,5)
#         print(f"{result_add}")
#         if result_add == 10:
#             print("Why nigga???")
#         # Call the 'subtract' function on the server
#         # result_subtract = proxy.subtract(10, 4)
#         # print(f"10 - 4 = {result_subtract}")

#         # You can also handle exceptions if the server raises any
#         try:
#             # Let's try calling a non-existent function (will raise an error on the server)
#             proxy.multiply(2, 6)
#         except xmlrpc.client.Fault as e:
#             print(f"Error from server: {e}")
#         except ConnectionRefusedError as e:
#             print(f"Could not connect to server: {e}")










# import xmlrpc.client
# import errno

# def connect_to_server(self):
#     try:
# # here put server ip address
#         with xmlrpc.client.ServerProxy("http://192.168.8.212:8000") as proxy:
#             print("Hello")
#             result = proxy.keylogger_file()                
#             print(f"Result: {result}")
#             return True

#     except Exception as e:
#         if e.errno == errno.ECONNREFUSED:
#             QMessageBox.critical(None, "Error", "Failed to connect. Server offline.")
#             return False
#         QMessageBox.critical(None, "Error", f"{e}")
#         return False
        
