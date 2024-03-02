import os
from Pyro4.util import json
from utils.types.client_type import ClientType


class ManageDataClient:
    def save_data_conecction_client(self, data_client: ClientType):
        name_client = data_client['name']
        if not os.path.exists('clients/data'):
            os.makedirs('clients/data')
        with open(f'clients/data/{name_client}.json', 'w') as file:
            json.dump(data_client, file)

    def get_data_conection_client(self, name_client):
        try:
            with open(f'clients/data/{name_client}.json', 'r') as file:
                data = json.load(file)
                data_client: ClientType = ClientType(**data)
                return data_client
        except FileNotFoundError:
            return None
