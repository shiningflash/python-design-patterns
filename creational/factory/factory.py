from shape import Shape, Square, Circle


class ShapeFactory:
    """
    Factory Class : ShapeFactory
    """

    def getShape(self, shapeType) -> Shape:
        if shapeType.lower() == 'square':
            return Square()
        elif shapeType.lower() == 'circle':
            return Circle()
        return None