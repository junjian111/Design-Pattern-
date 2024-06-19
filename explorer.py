from factories import VisualizationFactory
from visitors import JsonBuilderVisitor

class FunnyJsonExplorer:
    def __init__(self, factory: VisualizationFactory):
        self.factory = factory

    def load(self, data):
        self.visualization = self.factory.create_visualization()
        self.visualization.data = data

    def show(self):
        visitor = JsonBuilderVisitor()
        self.visualization.accept(visitor)
        result = visitor.get_product()
        self.draw(result)

    def draw(self, result):
        for line in result:
            print(line)
