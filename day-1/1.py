file_path = "input"

with open(file_path, "r") as file:
    l1 = []
    l2 = []
    d = []
    for l in file.readlines():
        l1.append(int(l.split(" ").pop(0)))
        l2.append(int(l.split(" ").pop(-1)))
    l1.sort()
    l2.sort()
    for n1, n2 in zip(l1,l2):
        d.append(abs(n2-n1))
    print(sum(d))

