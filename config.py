import argparse


def main(args):
    # Save the username and password in a config environment file
    with open('config.env', 'w') as file:
        file.write(f'USERNAME={args.username}\n')
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

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function
    main(args)
