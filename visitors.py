from interfaces import Visitor
from visualization import *

class JsonBuilderVisitor(Visitor):
    def __init__(self):
        self.output = []

    def visit_tree_visualization(self, element: TreeVisualization):
        element.create_conversion(element.data)
        element.rebuild_output()
        self.output = element.output

    def visit_rectangle_visualization(self, element: RectangleVisualization):
        element.create_conversion(element.data)
        element.rebuild_output()
        self.output = element.output

    def get_product(self):
        return self.output
