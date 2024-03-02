from clients.client_1 import deploy_client_1

if __name__ == '__main__':
    clients_names = {
        1: "Client Main"
    }
    clients_functions = {
        1: deploy_client_1,
    }
    while True:
        print("Which client do you want to execute?")
        i = 1
        for key, value in clients_names.items():
            print(f"{key}. {value}")
            i += 1

        print(f"{i}. Exit")

        option = input("Enter the number of the client you want to execute: ")
        if option.isdigit():
            option = int(option)
            if option in clients_names:
                clients_functions[option]()
            elif option == i:
                break
            else:
                print("Invalid option. Please enter a valid option.")


