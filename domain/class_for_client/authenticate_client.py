from utils.errors import ErrorTypes
from utils.types.client_type import ClientType
import Pyro4


class AuthenticateClient:
    def __init__(self, data_client: ClientType, ns_instance):
        self.ns_instance = ns_instance
        self.data_client = data_client

    def authenticate(self, code_otp: str = None):

        try:
            gateway_instance = self.ns_instance.authenticate_client_in_gateway({
                "name": self.data_client["name"],
                "description": self.data_client["description"],
                "id": self.data_client["id"],
                "code_otp": code_otp
            })
            return self.validate_response_gateway(gateway_instance)
        except Exception as e:
            message = str(e)
            return None, False, True, message

    def validate_response_gateway(self, gateway_instance):
        error = False
        message = ""
        is_authenticated = gateway_instance.get('is_authenticated', False)
        gateway_proxy = None

        if is_authenticated:
            gateway_uri = gateway_instance.get('gateway_uri', None)
            if not gateway_uri:
                print("A gateway URI was not provided.")
                exit()

            gateway_proxy = Pyro4.Proxy(gateway_uri)
            print("Gateway located. Starting client...", gateway_uri)
        if "error" in gateway_instance:
            message = f'{gateway_instance["error"]} - {gateway_instance["message"]}'
            is_exit = False
            if ErrorTypes.ip_blocked.value[0] == gateway_instance["error"]:
                is_exit = True
            return gateway_proxy, False, True, message, is_exit

        return gateway_proxy, is_authenticated, error, message, False
