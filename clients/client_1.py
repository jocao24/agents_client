from domain.register_client import RegisterClient


def deploy_client_1():
    gateway_proxy = RegisterClient().execute()

    while True:
        skills = gateway_proxy.get_skills()
        if not skills:
            print('No skills available.')
            exit()

        print('Available skills: ')
        i = 1
        for skill in skills:
            print(f"{i}. {skill}")
            i += 1
        print(f"{i}. Exit")

        skill = None
        request_skill = True
        while request_skill:
            skill = input(f'Enter the number of the skill you want to use. For exit, enter {len(skills) + 1}: ')
            if skill == str(len(skills) + 1):
                exit()
            elif skill.isdigit() and 1 <= int(skill) <= len(skills):
                request_skill = False
            else:
                print('Invalid number. Please enter a valid number.')

        skill = skills[int(skill) - 1]
        request_numbers = True
        while request_numbers:
            try:
                num1 = float(input('Enter the first number: '))
                num2 = float(input('Enter the second number: '))

                print('Sending request to the gateway...')
                result = gateway_proxy.execute_operation(skill, num1, num2)
                print(f"Result: {result}")
                request_numbers = False
            except ValueError:
                print('Invalid number. Please enter a valid number.')
