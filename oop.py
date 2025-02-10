import random 

class character:
    hair_colors = ["Blonde", "Brown", "Black", "Red"]
    sizes = ["Tiny", "Medium", "Large"]
    special_powers = ["Flying", "Invisability", "Super Strength"]

    #Constructor
    def__init__(self):
        self.generate_character()

    def generate_character():
        self.hair_color = random.choice(Character.hair_colors)
        self.size = random.choice(Character.sizes)
        self.size = random.choice(Character.special_powers)
        self.description = (
            f"Your character has (self.hair_color) hair, "
            f"is (self.size) in size and has the power of (self.special power)"
        )

    def__str__(self):
        return self.description

char1 = Character()
char2 = Character2

print(char1)
print(char2)