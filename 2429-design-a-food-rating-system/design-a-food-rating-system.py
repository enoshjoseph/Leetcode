class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisins_food = defaultdict(SortedSet)
        self.cuisins = {}
        self.rating = {}

        for i in range(len(foods)):
            self.cuisins_food[cuisines[i]].add((-ratings[i], foods[i]))
            self.cuisins[foods[i]] = cuisines[i]
            self.rating[foods[i]] = ratings[i]
            

        
        

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.cuisins[food]
        r = self.rating[food]
        self.cuisins_food[c].remove((-r, food))
        self.cuisins_food[c].add((-newRating, food))
        self.rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisins_food[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)