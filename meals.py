def recipes(cook_book):
  with open("recipes.txt", encoding="utf-8") as file_recipes:
    while True:
      line_book = file_recipes.readline()
      if not line_book:
        break
      if line_book.strip() != "":
        cook_book[line_book.strip()] = []
        count = int(file_recipes.readline().strip())
        for i in range(count):
          ingridient = file_recipes.readline().strip().split(" | ")
          cook_book[line_book.strip()].append({"ingridient_name": ingridient[0], "quantity": int(ingridient[1]), "measure": ingridient[2]})

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    order = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient["ingridient_name"] not in order.keys():
                order[ingridient["ingridient_name"]] = {"measure": ingridient["measure"], "quantity": ingridient["quantity"] * person_count,}
            else:
                order[ingridient["ingridient_name"]]["quantity"] += ingridient["quantity"] * person_count
    return order


def main():
    cook_book = {}
    recipes(cook_book)
    print('Cook book: ')
    print(cook_book)
    print('=' * 10)
    print('Meal: ')
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book))

if __name__ == "__main__":
    main()