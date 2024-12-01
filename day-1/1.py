from collections import Counter
file_path = "input"

with open(file_path, "r") as file:
    l1 = []
    l2 = []
    for l in file.readlines():
        l1.append(int(l.split(" ").pop(0)))
        l2.append(int(l.split(" ").pop(-1)))

    def part1():
        d = []
        l1.sort()
        l2.sort()
        for n1, n2 in zip(l1,l2):
            d.append(abs(n2-n1))
        print(sum(d))
    part1()

    def part2():
        # O(m*n) so inefficient
        #counts = {num: l2.count(num) for num in l1}
        #print(sum(num * counts.get(num, 0) for num in l1))

        # O(m+n)
        l2_counts = Counter(l2)
        print(sum(num * l2_counts.get(num, 0) for num in l1))
    part2()

