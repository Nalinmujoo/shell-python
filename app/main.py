import sys

commands = set(['exit', 'echo'])

def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def main():

    while True:
        write("$ ")
        
        # Wait for user input
        command = input()

        # print("cmd", command)

        args = command.split(" ")

        # print("args", args)

        if args[0] not in commands:
            print(f"{command}: command not found")
            continue

        if args[0] == "exit":
            if len(args) > 1 and args[1].isdigit():
                sys.exit(int(args[1]))       

        if args[0] == "echo":
            if len(args) > 1:
                print(" ".join(args[1:]))
            else:
                print("")

if __name__ == "__main__":
    main()
