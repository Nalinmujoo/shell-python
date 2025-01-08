import sys

commands = []

def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def main():
    write("$ ")

    # Wait for user input
    command = input()

    if command not in commands:
        print(f"{command}: command not found\n")
        main()


if __name__ == "__main__":
    main()
