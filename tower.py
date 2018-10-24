class Tower:
    def __init__(self):
        self.n, self.k = [int(x) for x in input("Enter two numbers here: ").split()]
        self.a = [int(x) for x in input("Enter two numbers here: ").split()]
        self.rank = []
        count = 1
        for i in self.a:
            self.rank.append([count, i])
            count += 1

    def diff(self):
        self.rank = sorted(self.rank, key= lambda x:x[1])
        bushu = []
        for i in range(0, self.k):
            self.rank[-1][1] -= 1
            self.rank[0][1] += 1
            bushu.append([self.rank[-1][0], self.rank[0][0]])
            self.rank = sorted(self.rank, key=lambda x: x[1])
        print((self.rank[-1][1] - self.rank[0][1], self.k))
        for i in bushu:
            print(i)
        return


if __name__ == '__main__':
    a = Tower()
    a.diff()
