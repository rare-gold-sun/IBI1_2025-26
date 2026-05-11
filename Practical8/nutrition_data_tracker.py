class FoodItem:
    def __init__(self,name,calories,protein,carbohydrates,fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat


apple = FoodItem("apple",60,0.3,15,0.5)


def onedayrepo(foodlist):
    total_calories = sum(food.calories for food in foodlist)
    total_fat = sum(food.fat for food in foodlist)
    total_protein = sum(food.protein for food in foodlist)
    total_carbohydrates = sum(food.carbohydrates for food in foodlist)
    repo = [f"Total calories: {total_calories}",f"Total fat: {total_fat}g",f"Total protein: {total_protein}g",f"Total carbohydrates: {total_carbohydrates}g"]  
    if total_calories > 2500:
        repo.append("WARNING: too much CALORIES")
    if total_fat > 90:
        repo.append("WARNING: too much FAT")

    return "\n".join(repo)



print(onedayrepo([apple]))