import uuid

from domain.class_for_client.conect_client_and_nameserver import NameServerClientConnection
from utils.types.client_type import ClientType
from utils.get_ip import get_ip
from utils.validate_ip import validate_ip


def request_data_client(name_client: str):
    description_client = input('Enter the description of the client: ')
    id_client = str(uuid.uuid4())
    while True:
        ip_name_server = input("Enter the IP of the nameserver. If it is the same as the NameServer, press enter: ")
        if ip_name_server:
            is_valid_ip = validate_ip(ip_name_server)
            if not is_valid_ip:
                print("The IP entered is not valid. Please enter a valid IP.")
                continue
            break
        ip_name_server = get_ip()
        break

    data_client = {
        "name": name_client,
        "description": description_client,
        "id": id_client,
        "local_ip": get_ip(),
        "ip_name_server": ip_name_server,
    }
    nameserver_conection = NameServerClientConnection(data_client)
    nameserver_conection.conect_to_nameserver_manually(ip_name_server)
    return nameserver_conection, data_client


def connect_client_to_nameserver(data_client: ClientType, name_client: str):
    data_client_saved = data_client
    nameserver_conection = None

    while True:
        opt_select = input("Do you want to use the nameserver IP saved in the configuration file? (y/n): ")
        if opt_select.lower() == 'y':
            is_valid_ip = False
            if data_client_saved:
                is_valid_ip = validate_ip(data_client_saved["ip_name_server"])
            if not is_valid_ip or not data_client_saved:
                print("The IP of the ns saved in the configuration file is not valid. Please enter a valid IP.")
                nameserver_conection, data_client_saved = request_data_client(name_client)
            nameserver_conection = NameServerClientConnection(data_client_saved)
            nameserver_conection.conect_to_nameserver_manually(data_client_saved["ip_name_server"])
            break
        elif opt_select.lower() == 'n':
            nameserver_conection, data_client_saved = request_data_client(name_client)
            break
        else:
            print("Invalid option. Please enter a valid option.")

    return nameserver_conection, data_client_saved
