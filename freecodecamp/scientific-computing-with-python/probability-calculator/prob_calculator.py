# Probability Calculator

# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator


import random
import copy
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):       
        self.contents = []
        self.kwargs = kwargs
        if self.kwargs == {}:
            raise TypeError("Parameters must be equal or bigger than 1.")
        
        for key in self.kwargs:
            for i in range(self.kwargs[key]):
                self.contents.append(key)           

                    
    def draw(self, balls):
        balls_draw = []
  
        if balls >= len(self.contents):
            return self.contents
            
# I could use random.sample to get all the balls at once,
# but the test checks for the number of balls removed
        for i in range(balls):
            ball_draw = random.choice(self.contents)
            balls_draw.append(ball_draw)
            self.contents.remove(ball_draw)
        return balls_draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    expected = []
    for key in expected_balls:
        for i in range(expected_balls[key]):
            expected.append(key)

    counter = 0     
    for i in range(num_experiments):
        balls_draw = copy.deepcopy(hat).draw(num_balls_drawn)
        expect = copy.copy(expected)
        compare = []     

        for elem in balls_draw:
            try:
                expect.remove(elem)
                compare.append(elem)
            except:
                pass
    
        compare.sort()
        expected.sort()
        if compare == expected:
            counter += 1
            
    return counter / num_experiments