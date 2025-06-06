class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:

        res = 1
        while self.st and self.st[-1][0] <= price:
            val, cnt = self.st.pop()
            res += cnt
        self.st.append((price, res))
        return res

