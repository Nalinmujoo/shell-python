import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    commands = []
    # Wait for user input
    command = input()

    if command not in commands:
        print(f"{command}: command not found\n")
        main()


if __name__ == "__main__":
    main()
