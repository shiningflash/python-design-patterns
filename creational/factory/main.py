from shape import Shape
from factory import ShapeFactory


if __name__ == '__main__':
    shapeFactory: ShapeFactory = ShapeFactory()
    
    square: Shape = shapeFactory.getShape('square')
    print(square.draw())

    circle: Shape = shapeFactory.getShape('circle')
    print(circle.draw())