import matplotlib.pyplot as plt

def shape(shape):
    color = 'skyblue'

    def __init__(self, width, height, color):
        super().__init__(self, color=color)
        self.width = width
        self.height = height


    def drawCircle(radius):
        plt.gca().add_patch(plt.Circle((0, 0), radius=radius, fc=color))
        plt.axis('scaled')
        plt.show()   ########

    def drawRect(width, height):
        plt.gca().add_patch(plt.Rectangle((0, 0), width=width, height=height, fc=color))
        plt.axis('scaled')
        plt.show()  ########

    if shape == 'circle':
        return drawCircle
    elif shape == 'rect':
        return drawRect
    else:
        print("Invalld parameter")


circle = shape('circle')
rect = shape('rect')

circle(10)
rect(10, 30)