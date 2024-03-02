import Pyro4

from utils.types.client_type import ClientType
from utils.get_ip import get_ip


class NameServerClientConnection:

    def __init__(self, data_client: ClientType):
        self.name_client = data_client['name']
        self.description_client = data_client['description']
        self.id_client = data_client['id']
        self.ns_instance = None
        self.name_server = None
        self.ip_name_server = None

    def conect_to_nameserver_automatically(self):
        self.name_server = Pyro4.locateNS()
        self.conect_to_controller()
        self.set_ip_name_server()
        return self.ip_name_server

    def conect_to_nameserver_manually(self,  ip_name_server: str = None):
        self.ip_name_server = ip_name_server
        self.name_server = Pyro4.locateNS(host=self.ip_name_server, port=9090)
        self.conect_to_controller()

    def get_name_server_instance(self):
        return self.ns_instance

    def conect_to_controller(self):
        self.ns_instance = Pyro4.Proxy(self.name_server.lookup("ns_controller"))

    def set_ip_name_server(self):
        self.ip_name_server = str(self.name_server).split("@")[1].split(":")[0]

    def get_data_client(self):
        return {
            "name_agent": self.name_client,
            "description_agent": self.description_client,
            "id_agent": self.id_client,
            "local_ip": get_ip(),
            "ip_name_server": self.ip_name_server,
        }
