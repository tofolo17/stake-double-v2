import os

STAGE = "PRODUCAO"  # DESENVOLVIMENTO / PRODUCAO


def env_settings(STAGE):
    if STAGE == "DESENVOLVIMENTO":
        env_file = 'local_config.env'
    else:
        env_file = 'config.env'

    return env_file


def main():
    # Check for updates
    os.system('git pull')

    # Install the required packages
    os.system('pip install -r requirements.txt')
    print('Packages installed.')

    # Requests username and password from the user
    r = input('Do you want to update your account? [Y/N]: ')
    if r.lower() == 'y':
        username = input('Enter your username: ')
        password = input('Enter your password: ')
    else:
        # Get already saved settings
        env_file = env_settings(STAGE)
        with open(env_file, 'r') as file:
            lines = file.readlines()
            username = lines[0].split('=')[1].strip()
            password = lines[1].split('=')[1].strip()

    # PRINTAR OPÇÕES DE MONEY POSSÍVEIS (ABRIR JOGO)

    # Requests how much money the user wants to bet (minimum R$10 / R$5 each column)
    money = input(
        'Enter the amount of money you want to bet: R$'
    )

    # Get settings
    env_file = env_settings(STAGE)

    # Save the username and password in a config environment file
    with open(env_file, 'w') as file:

        file.write(f'USER={username}\n')
        file.write(f'PASSWORD={password}\n')
        file.write(f'MONEY={money}\n')


if __name__ == '__main__':
    main()
