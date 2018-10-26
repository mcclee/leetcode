
class Solution:

    def __init__(self):
        self.ele = [1, 5, 10, 50, 100, 500, 1000]
        self.dictionary = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        i = 0
        sym = num
        string = ''
        while sym > 0:
            st = ''
            cur = sym % 10
            if 9 > cur >= 5:
                cur -= 5
                st = st + self.dictionary[5 * pow(10, i)]
                while cur > 0:
                    st = st + self.dictionary[pow(10, i)]
                    cur -= 1
            elif cur == 9:
                st = st + self.dictionary[pow(10, i)] + self.dictionary[pow(10, i + 1)]
            elif cur == 4:
                st = st + self.dictionary[pow(10, i)] + self.dictionary[5 * pow(10, i)]
            elif cur < 4:
                while cur > 0:
                    st = st + self.dictionary[pow(10, i)]
                    cur -= 1
            i += 1
            string = st + string
            sym = int(sym/10)
        return string
