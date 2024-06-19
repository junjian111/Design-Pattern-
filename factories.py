from interfaces import VisualizationFactory
from visualization import *
from icon_family import *

class TreeVisualizationFactory(VisualizationFactory):
    def __init__(self, icon_family):
        self.icon_family = icon_families[icon_family]

    def create_visualization(self) -> TreeVisualization:
        return TreeVisualization(self.icon_family)

class RectangleVisualizationFactory(VisualizationFactory):
    def __init__(self, icon_family):
        self.icon_family = icon_families[icon_family]

    def create_visualization(self) -> RectangleVisualization:
        return RectangleVisualization(self.icon_family)
