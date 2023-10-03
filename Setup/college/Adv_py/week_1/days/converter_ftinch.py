from abc import ABC, abstractmethod

class Feet:
    feet_list = list(map(int, input("Enter the size in feet: ").split()))

class Inch:
    inch_list = list(map(int, input("Enter the size in inch: ").split()))

class Transform(ABC):
    @abstractmethod
    def convert(self, feet_list):
        inch_list = [feet * 12 for feet in feet_list]
        return inch_list

class Sum(Transform):
    def convert(self, feet_list):
        inch_list = super().convert(feet_list)
        return [feet + inch/12 for feet, inch in zip(feet_list, inch_list)]

# Example usage
sum_obj = Sum()
result = sum_obj.convert(Feet.feet_list)
print(result)
