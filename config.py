import os
import subprocess

STAGE = "PRODUCAO"  # DESENVOLVIMENTO / PRODUCAO


def env_settings(STAGE):
    if STAGE == "DESENVOLVIMENTO":
        env_file = 'local_config.env'
    else:
        env_file = 'config.env'

    return env_file


def main():
    # Check if the repo is up to date
    r = subprocess.run(
        ['git', 'pull'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode == 0:
        output = r.stdout.decode('utf-8')
    else:
        error = r.stderr.decode('utf-8')
        print(f"Error: {error}")

    # Check if the username var is empty in the config file
    env_file = env_settings(STAGE)
    with open(env_file, 'r') as file:
        lines = file.readlines()
        username = lines[0].split('=')[1].strip()
        password = lines[1].split('=')[1].strip()

    if (username == '' or password == '') or ("Already up to date" not in output):
        os.system('pip install -r requirements.txt')
        print('Packages installed.')

    # Request the username and password if they are empty, otherwise, check if the user wants to change them
    if (username == '' or password == ''):
        username = input('Enter your username: ')
        password = input('Enter your password: ')
    else:
        change = input(
            'Do you want to change your username and password? (Y/N): ')
        if change.lower() == 'y':
            username = input('Enter your username: ')
            password = input('Enter your password: ')

    # # PRINTAR OPÇÕES DE MONEY POSSÍVEIS (ABRIR JOGO)

    # Requests how much money the user wants to bet (minimum R$10 / R$5 each column)
    money = input(
        'Enter the amount of money you want to bet: R$'
    )

    # Save the username and password in a config environment file
    with open(env_file, 'w') as file:
        file.write(f'USER={username}\n')
        file.write(f'PASSWORD={password}\n')
        file.write(f'MONEY={money}\n')


if __name__ == '__main__':
    main()
