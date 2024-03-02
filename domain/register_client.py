import Pyro4
from domain.class_for_client.authenticate_client import AuthenticateClient
from domain.class_for_client.manage_data_client import ManageDataClient
from domain.conect_client_to_naverserver import connect_client_to_nameserver
from utils.types.client_type import ClientType
from utils.get_ip import get_ip
import uuid
from utils.validate_ip import validate_ip


class RegisterClient:
    def execute(self):
        name_client = input('Enter the name of the client: ')
        print('Connecting to the nameserver...')
        nameserver_conection = None
        data_client = ManageDataClient().get_data_conection_client(name_client)
        nameserver_conection, data_client = connect_client_to_nameserver(data_client, name_client)
        ns_instance = nameserver_conection.get_name_server_instance()
        ManageDataClient().save_data_conecction_client(data_client)
        autenticate_client = AuthenticateClient(data_client, ns_instance)
        gateway_proxy, is_authenticated, error, message = autenticate_client.authenticate()
        if error and not is_authenticated:
            print(message)
            exit()

        while not is_authenticated:
            print('OTP is required. Please enter the OTP: ')
            code_otp = input('Enter the OTP code: ')
            gateway_proxy, is_authenticated, error, message = autenticate_client.authenticate(code_otp)
            if error and not is_authenticated:
                print(message)
                exit()

        print('Authenticated successfully.')
        return gateway_proxy
