import sys

commands = set(['exit', 'echo', 'type'])

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
            else:
                sys.exit()       

        if args[0] == "echo":
            if len(args) > 1:
                sys.stdout.write(" ".join(args[1:])+ "\n")
            else:
                sys.stdout.write("\n")

        if args[0] == "type":
            if len(args) > 1 and args[1] in commands:
                sys.stdout.write(f"{args[1]} is a shell builtin\n")
            else:
                sys.stdout.write(f"{args[1]}: not found\n")


if __name__ == "__main__":
    main()
