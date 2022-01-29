class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []
        mem = set(supplies)
        ingre_map = {}
        for i in range(len(recipes)):
            ingre_map[recipes[i]] = ingredients[i]
        def dfs(root, visited):
            if root in mem:  return True
            if root not in ingre_map:   return False
            for ingre in ingre_map[root]:
                if ingre in visited:    return False
                visited.add(ingre)
                if not dfs(ingre, visited): return False
                visited.remove(ingre)
            mem.add(root)
            return True
        for recipe in recipes:
            if dfs(recipe, set([recipe])): ans.append(recipe)
        return ans