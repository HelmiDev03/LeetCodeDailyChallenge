class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        output = []
        supplies_set = set(supplies)  

        for _ in range(len(recipes)): 
            for i in range(len(recipes)):
                if recipes[i] in output:  
                    continue  

                flag = True  
                for ingredient in ingredients[i]:
                    if ingredient not in supplies_set:
                        flag = False
                        break 

                if flag:
                    output.append(recipes[i])
                    supplies_set.add(recipes[i]) 
        
        return output