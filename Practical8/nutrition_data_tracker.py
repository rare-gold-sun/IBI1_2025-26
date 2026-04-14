class food_item:
    def __init__(self,name,calories,protein,carbohydrates,fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat


apple = food_item("apple",60,0.3,15,0.5)


def onedayrepo(foodlist):
    tocal = sum(food.calories for food in foodlist)
    tofa = sum(food.fat for food in foodlist)
    topro = sum(food.protein for food in foodlist)
    tocarb = sum(food.carbohydrates for food in foodlist)
    repo = [f"Total calories: {tocal}",f"Total fat: {tofa}g",f"Total protein: {topro}g",f"Total carbohydrates: {tocarb}g"]  
    if tocal > 2500:
        repo.append("WARNING: too much CALORIES")
    if tofa > 90:
        repo.append("WARNING: too much FAT")

    return "\n".join(repo)



print(onedayrepo([apple]))