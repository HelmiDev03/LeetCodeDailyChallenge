class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        available_boxes = dict()
        max_candies = 0
        for box in initialBoxes:
            available_boxes[box] = 1

        while available_boxes:
            opened_boxes = []
            new_boxes = []
            for box in available_boxes.keys():
                if status[box]:
                    max_candies += candies[box]
                    for key in keys[box]:
                        status[key] = 1
                    for contained_box in containedBoxes[box]:
                        new_boxes.append(contained_box)
                    
                    opened_boxes.append(box)

            if not opened_boxes:
                break

            for box in opened_boxes:
                available_boxes.pop(box)

            for box in new_boxes:
                available_boxes[box] = 1

        return max_candies