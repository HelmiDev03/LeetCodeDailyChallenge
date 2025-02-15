class Solution:

    rows: list[set[str]]
    cols: list[set[str]]
    boxes: list[set[str]]

    def __init__ (self) -> None:
        for attr in self.__annotations__:
            setattr(self, attr, [set() for _ in range(9)])

    def clear (self) -> None:
        for attr in self.__annotations__:
            for _set in getattr(self, attr):
                _set.clear()

    def box_index (self, row: int, col: int) -> int:
        r, c = row // 3, col // 3
        return r * 3 + c

    def isValidSudoku (self, board: list[list[str]]) -> bool:
        self.clear()
        for row, col in itertools.product(range(9), repeat=2):
            cell = board[row][col]
            if cell == ".": continue

            box = self.box_index(row, col)
            records = (self.rows[row], self.cols[col], self.boxes[box])
            invalid = any(cell in record for record in records)

            if invalid: return False
            for record in records:
                record.add(cell)

        return True