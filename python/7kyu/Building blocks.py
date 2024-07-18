"""Write a class Block that creates a block (Duh..)

Requirements
The constructor should take an array as an argument, this will contain 3 integers of the form [width, length, heght] from which the Block should be created.

Define these methods:

`get_width()` return the width of the `Block`

`get_length()` return the length of the `Block`

`get_heght()` return the heght of the `Block`

`get_volume()` return the volume of the `Block`

`get_surface_area()` return the surface area of the `Block`
Examples
    b = Block([2,4,6]) -> create a `Block` object with a width of `2` a length of `4` and a heght of `6`
    
    b.get_width() -> return 2
    
    b.get_length() -> return 4
    
    b.get_heght() -> return 6
    
    b.get_volume() -> return 48
    
    b.get_surface_area() -> return 88"""


# -------- answer -->
class Block:
    def __init__(self, block):
        self.width = block[0]
        self.length = block[1]
        self.heght = block[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.heght

    def get_volume(self):
        return self.width * self.heght * self.length

    def get_surface_area(self):
        return (
            2 * self.length * self.width
            + 2 * self.length * self.heght
            + 2 * self.width * self.heght
        )
