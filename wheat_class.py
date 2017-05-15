from crop_class import *

class Wheat(Crop): # (crop) indicates Wheat is a subclass of crop
    """A wheat crop"""
    # constructor
    def __init__(self):
            # call the parent class constructor with default growth rate = 1
            # light need = 3, water need = 6
            super().__init__(1,3,6)
            self._type = "Wheat"

    # override grow method for subclass - polymorphism
    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()

def main():
    #create a new wheat crop
    wheat_crop = Wheat()
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())

if __name__ == "__main__":
    main()
        




