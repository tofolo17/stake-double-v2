import argparse


def env_settings(STAGE):
    if STAGE == "DESENVOLVIMENTO":
        env_file = 'local_config.env'
    else:
        env_file = 'config.env'

    return env_file


def main(args):
    # Get settings
    env_file = env_settings(args.stage)

    # Save the username and password in a config environment file
    with open(env_file, 'w') as file:
        file.write(f'USER={args.username}\n')
        file.write(f'PASSWORD={args.password}\n')


if __name__ == '__main__':
    # Create a new ArgumentParser instance
    parser = argparse.ArgumentParser()

    # Login arguments
    parser.add_argument(
        '--username',
        help='The username to use for authentication'
    )

    # Password arguments
    parser.add_argument(
        '--password',
        help='The password to use for authentication'
    )

    # Stage arguments
    parser.add_argument(
        '--stage',
        help='The stage to use for the environment',
        default='PRODUCAO'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function
    main(args)
