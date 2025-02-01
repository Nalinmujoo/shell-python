import sys
import os

commands = set(['exit', 'echo', 'type'])

def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def find_in_path(command):
    for path in os.environ["PATH"].split(":"):
        if os.path.exists(f"{path}/{command}"):
            return f"{path}/{command}"
    return None

def main():

    while True:
        write("$ ")
        
        # Wait for user input
        command = input()

        args = command.split(" ")

        if args[0] not in commands and find_in_path(args[0]):
            os.system(command)
            continue
        elif args[0] not in commands:
            sys.stdout.write(f"{command}: command not found\n")
            continue 
        else:
            pass
        
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

        if args[0] == "type" and len(args) > 1:
            if args[1] in commands:
                sys.stdout.write(f"{args[1]} is a shell builtin\n")
            elif find_in_path(args[1]):
                sys.stdout.write(f"{args[1]} is {find_in_path(args[1])}\n")
            else:
                sys.stdout.write(f"{args[1]}: not found\n")

        

if __name__ == "__main__":
    main()
