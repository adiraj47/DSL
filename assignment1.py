"""
Aditya Singh Rajpurohit
SECOD401
"""
class linear_probing:
    def __init__(self, n):
        entry = [0, ""]
        self.hash_table = [entry for i in range(n)]
        self.n = n

    def insert(self, phone, name):
        "This function inserts into hash table using linear probing"
        for i in range(0, self.n):
            index = (phone + i) % self.n
            if self.hash_table[index] == [0, ""]:
                self.hash_table[index] = [phone, name]
                break

            else:
                continue

    def find(self, phone):
        print("search using linear probing")
        comparisons = 0
        for i in range(0, self.n):
            index = (phone + i) % self.n
            comparisons += 1

            if self.hash_table[index][0] == phone:
                print("phone no.", self.hash_table[index][0])
                print("Name;", self.hash_table[index][1])
                print("Comparisons required:", comparisons)
                break
            else:
                continue
        print()

    def print_hashtable(self):
        print("hash table using linear probing")
        for i in range(self.n):
            print(self.hash_table[i][0], "->", self.hash_table[i][1])
        print()


class quadratic_probing:
    def __init__(self, n):
        entry = [0, ""]
        # creating list of phone no. and names
        self.hash_table = [entry for i in range(n)]
        self.n = n

    def insert(self, phone, name):
        "this function inserts into hash table using quadratic probing"
        for i in range(0, self.n):
            index = (phone + i * i) % self.n
            if self.hash_table[index] == [0, ""]:
                self.hash_table[index] = [phone, name]
                break
            else:
                continue

    def find(self, phone):
        # print("search using quadratic probing")
        comparisons = 0
        for i in range(0, self.n):
            index = (phone + i * i) % self.n
            comparisons += 1
            if self.hash_table[index][0] == phone:
                print("phone no.", self.hash_table[index][0])
                print("Name;", self.hash_table[index][1])
                print("Comparisons required:", comparisons)
                break
            else:
                continue
        print()

    def print_hashtable(self):
        print("hash table using quadratic probing")
        for i in range(self.n):
            print(self.hash_table[i][0], "->", self.hash_table[i][1])
        print()


if __name__ == "__main__":
    n = 10
    data = [
        [9660663089, "aa"],
        [9096197668, "bb"],
        [8055166507, "cc"],
        [7709235516, "dd"],
        [9090909090, "ff"],
        [8080808080, "gg"],
        [9696969696, "hh"],
        [8787878787, "ii"],
        [9307987654, "jj"],
        [9787867567, "kk"],
    ]
    print("using linear probing")
    hl = linear_probing(n)
    for i in range(n):
        hl.insert(data[i][0], data[i][1])
    hl.print_hashtable()
    hl.find(9660663089)
    print("using quadratic probing")
    hq = quadratic_probing(n)
    for i in range(n):
        hq.insert(data[i][0], data[i][1])
    hq.print_hashtable()
    hq.find(8055166507)