from abc import ABC, abstractmethod
from typing import Any


TEMPLATE = """

<h1>Products</h1>

{% for product in products %}
    <p>{{ product.title }}</p>

"""

class ViewEngine(ABC):
    @abstractmethod
    def render(self, view_name: str, context: dict[str, Any]): ...



class MatchaViewEngine(ViewEngine):
    def render(self, view_name: str, context: dict[str, Any]) -> str:
        return 'View rendered by Matcha'

class Controller:
    def _create_view_engine(self) -> ViewEngine:
        return MatchaViewEngine()

    def render(self, view_name: str, context: dict[str, Any]) -> None:
        engine = self._create_view_engine()
        html = engine.render(view_name, context)
        print(html)



class SharpViewEngine(ViewEngine):
    def render(self, view_name: str, context: dict[str, Any]):
        return 'View rendered by Sharp'

class SharpController(Controller):
    def _create_view_engine(self) -> ViewEngine:
        return SharpViewEngine()



class ProductsController(SharpController):
    def list_products(self) -> None:
        context: dict[str, Any] = {}
        # get products from a database
        # context[products] = products
        self.render('products.html', context)


if __name__ == '__main__':
    ProductsController().list_products()
