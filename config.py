import os


def env_settings(STAGE):
    if STAGE == "DESENVOLVIMENTO":
        env_file = 'local_config.env'
    else:
        env_file = 'config.env'

    return env_file


def main():
    # Install the required packages
    os.system('pip install -r requirements.txt')
    print('Packages installed.')

    # Requests username and password from the user
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    # PRINTAR OPÇÕES DE MONEY POSSÍVEIS (ABRIR JOGO)

    # Requests how much money the user wants to bet (minimum R$10 / R$5 each column)
    money = input('Enter the amount of money you want to bet (minimum R$10 / R$5 each column): ')

    # Get settings
    env_file = env_settings("PRODUCAO")

    # Save the username and password in a config environment file
    with open(env_file, 'w') as file:
        file.write(f'USER={username}\n')
        file.write(f'PASSWORD={password}\n')
        file.write(f'MONEY={money}\n')


if __name__ == '__main__':
    main()
