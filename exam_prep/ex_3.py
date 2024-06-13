def cookbook(*args):
    cookbook_data = {}

    for data in args:
        recipe, cuisine, ingredients = data
        if cuisine not in cookbook_data:
            cookbook_data[cuisine] = {}

        cookbook_data[cuisine][recipe] = ingredients

    sorted_cookbook_data = sorted(cookbook_data.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ""

    for cuisine, data in sorted_cookbook_data:
        result += f"{cuisine} cuisine contains {len(data)} recipes:\n"
        sorted_recipes = sorted(data.items(), key=lambda kvp: kvp[0])

        for recipe, ingredients in sorted_recipes:
            result += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"

    return result

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))


