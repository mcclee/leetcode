class Cost:

    def totalcost(self, num):
        if num > 2:
            s = int(pow(num, 0.5))
            for i in range(2, s + 1):
                if num % i == 0:
                    return self.totalcost(num - num // i) + i - 1
            return self.totalcost(num - 1) + num - 1
        elif num == 2:
            return 1
        else:
            return 0


if __name__ == '__main__':
    n = int(input())
    c = Cost()
    print(c.totalcost(n))