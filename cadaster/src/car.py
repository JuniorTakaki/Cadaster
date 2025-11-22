import datetime
class Car:
    def __init__(self, brand="", model ="", year="",color=""):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def car_brand(self) -> None:
        while True:
            brand_input = input("Marca= ").strip()
            if not brand_input:
                print("O campo não pode ficar vázio.")
            elif not brand_input.isalpha():
                print("Use apenas letras, sem números ou símbolos")
                continue
            self.brand = brand_input
            break

    def car_model(self) -> None:
        while True:
            model_input = input("Model: ").strip()
            if not model_input:
                print("Model is required.")
                continue
            # allow letters, numbers, spaces, hyphens and slashes in model names
            allowed = all(c.isalnum() or c in " -/" for c in model_input)
            if not allowed:
                print("Use only letters, numbers, spaces, hyphens or slashes for model.")
                continue
            self.model = model_input
            break

    def car_year(self) -> None:
        current_year = datetime.datetime.now().year
        while True:
            age_input = input("Year: ").strip()
            if not age_input:
                print("Year is required.")
                continue
            try:
                self.year = int(age_input)
                if self.year < 1886 or self.year > current_year + 1:
                    print(f"Enter a valid year between 1886 and {current_year + 1}.")
                    continue
                self.year = age_input
                break
            except ValueError:
                print("Enter a numeric year (e.g., 2020).")

    def car_color(self) -> None:
        while True:
            color_input = input("Color: ").strip()
            if not color_input:
                print("Color is required.")
                continue
            if not color_input.replace(" ", "").isalpha():
                print("Use only letters and spaces for color.")
                continue
            self.color = color_input
            break
        