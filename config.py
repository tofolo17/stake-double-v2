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
    # Check if the username var is empty in the config file
    env_file = env_settings(STAGE)
    with open(env_file, 'r') as file:
        lines = file.readlines()
        username = lines[0].split('=')[1].strip()
        password = lines[1].split('=')[1].strip()
        money = lines[2].split('=')[1].strip()

    # Reset the repo keeping a specific file
    os.system('git reset --hard')
    print('')

    # Check if the repo is up to date
    r = subprocess.run(
        ['git', 'pull'], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if r.returncode == 0:
        output = r.stdout.decode('utf-8')
        if 'Already up to date' not in output:
            # Ask user to rerun the code
            print('The code has been updated. Please run the code again.')
            update_env(username, password, money, env_file)
            exit()
    else:
        error = r.stderr.decode('utf-8')
        print(f"Error: {error}")

    if (username == '' or password == ''):
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

    # Print the betting options
    print('You can bet R$10, R$20, R$50 or R$250.')

    # Requests how much money the user wants to bet (minimum R$10 / R$5 each column)
    money = float(input(
        'Enter the amount of money you want to bet: R$'
    ))
    if money not in [2, 5, 10, 20, 50, 250]:  # ALTERAR PARA 10, 20, 50, 250
        print('Invalid amount. Please enter a valid amount.')
        money = int(input(
            'Enter the amount of money you want to bet: R$'
        ))

    # Save the username and password in a config environment file
    update_env(username, password, money, env_file)


# Update the environment variables
def update_env(username, password, money, env_file):
    with open(env_file, 'w') as file:
        file.write(f'USER={username}\n')
        file.write(f'PASSWORD={password}\n')
        file.write(f'MONEY={money}\n')


if __name__ == '__main__':
    main()
