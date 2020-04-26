from abc import abstractmethod, ABC


class RenderableObjectBase(ABC):
    @abstractmethod
    def render(self) -> None:
        pass
