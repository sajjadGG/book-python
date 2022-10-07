from abc import ABC, abstractmethod
from dataclasses import dataclass


class Image:
    pass


class Filter(ABC):
    @abstractmethod
    def apply(self, image: Image) -> None:
        pass


class VividFilter(Filter):
    def apply(self, image: Image) -> None:
        print('Applying Vivid Filter')


class BlackAndWhite3rdPartyFilter:
    def init(self):
        """Required by 3rd party library"""

    def render(self, image: Image):
        print('Applying BlackAndWhite Filter')


@dataclass
class ImageView:
    image: Image

    def apply(self, filter: Filter):
        filter.apply(self.image)


if __name__ == '__main__':
    image_view = ImageView(Image())
    image_view.apply(BlackAndWhite3rdPartyFilter())
    # Traceback (most recent call last):
    # AttributeError: 'BlackAndWhite3rdPartyFilter' object has no attribute 'apply'
