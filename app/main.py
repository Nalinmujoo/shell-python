import sys

commands = []

def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()

    if command not in commands:
        print(f"{command}: command not found\n")
        main()


if __name__ == "__main__":
    main()
