# Polygon Area Calculator
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator

class Rectangle():

    def __init__(self, width, height):
        
        if not isinstance(width, (int, float)):
            raise TypeError("Widht must be a float or an int.")
            
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be a float or an int.")
        
        self.width = width
        self.height = height

       
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    
    def set_width(self, new_width):
        self.width = new_width
    
    
    def set_height(self, new_height):
        self.height = new_height
    
    
    def get_area(self):
        return self.width * self.height
    
    
    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)
    
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        
        picture = ""
        for i in range(self.height):
            for k in range(self.width):
                picture += "*"
            picture += "\n"        
        return picture

    
    def get_amount_inside(self, polygono):
        return int(self.get_area() / polygono.get_area())


class Square(Rectangle):
    
    def __init__(self, side):
        self.side = side
        width = height = self.side
        super().__init__(width, height)
    
        
    def __str__(self):
        return f"Square(side={self.side})"
    
    
    def set_side(self, new_side):
        self.side = new_side
        width = height = self.side
        super().__init__(width, height)


    def set_height(self, new_side):
        self.set_side(new_side),
        
        
    def set_width(self, new_side):
        self.set_side(new_side)