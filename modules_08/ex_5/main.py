from modules_08.ex_5.core import create_sequence, locate_number

command = input()
seq = None

while command != "Stop":
    if command.startswith("Create"):
        data = command.split()
        n = int(data[-1])
        seq = create_sequence(n)
        print(*seq, sep=' ')
    elif command.startswith("Locate"):
        data = command.split()
        number_to_locate = int(data[-1])
        if seq:
            print(locate_number(seq, number_to_locate))
        else:
            print("First create a sequence")
    else:
        print("Invalid command")
    command = input()
