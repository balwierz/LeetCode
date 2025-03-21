class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        missingIng = defaultdict(int)
        neededBy = defaultdict(list) 
        for product, ings in zip(recipes, ingredients):
            missingIng[product] = len(ings)
            for ing in ings:
                neededBy[ing].append(product)
        made = []
        while supplies:
            ing = supplies.pop()
            for product in neededBy[ing]:
                missingIng[product] -= 1
                if not missingIng[product]:
                    supplies.append(product)
                    made.append(product)
        return made
