class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def transpose(matrix):
            rows = len(matrix)
            cols = len(matrix[0])
            result = [[0] * rows for _ in range(cols)]
            
            for i in range(rows):
                for j in range(cols):
                    result[j][i] = matrix[i][j]
            return result
        def verif(board: List[List[str]])->bool:
            v=[0]*9
            for row in board:
                for i in row:
                    if i != '.' :
                        if v[int(i) -1]:
                            return False
                        v[int(i)-1]=1  
                v=[0]*9
            return True

        def extract_sub_boxes(matrix):
            sub_boxes = []
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    box = []
                    for i in range(3):
                        row = []
                        for j in range(3):
                            row.append(matrix[box_row + i][box_col + j])
                        box.append(row)
                    sub_boxes.append(box)
            return sub_boxes

        def is_valid_subbox(box):
            
            seen = set()
            for i in range(3):
                for j in range(3):
                    val = box[i][j]
                    if val == '.':
                        continue
                    if val in seen:
                        return False
                    seen.add(val)
            return True

       


        if not verif(board):
            return False
        elif not verif(transpose(board)):
            return False 
        else:
            sub_boxes=extract_sub_boxes(board)
            print(sub_boxes)
            for box in  sub_boxes  : 
                if not is_valid_subbox(box):
                    return False
        return True            

        