from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass

class Visitor(ABC):
    @abstractmethod
    def visit_tree_visualization(self, element):
        pass

    @abstractmethod
    def visit_rectangle_visualization(self, element):
        pass

class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

class VisualizationFactory(ABC):
    @abstractmethod
    def create_visualization(self) -> Element:
        pass
