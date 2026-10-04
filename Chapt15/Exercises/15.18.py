count = 0

def main():
    n = int(input("Enter number of disks: "))
    print("The moves are")
    move_disks(n, "A", "B", "C")
    global count
    print(f"Total count {count}")

def move_disks(n, from_tower, to_tower, aux_tower):
    global count
    count += 1
    if n == 1:
        print(f"Move disk {n} from {from_tower} to {to_tower}")
    else:
        move_disks(n - 1, from_tower, aux_tower, to_tower)
        print(f"Move disk {n} from {from_tower} to {to_tower}")
        move_disks(n - 1, aux_tower, to_tower, from_tower)

main()
