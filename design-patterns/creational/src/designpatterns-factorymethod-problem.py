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
    def render(self, view_name: str, context: dict[str, Any], engine: ViewEngine) -> None:
        html = engine.render(view_name, context)
        print(html)


class ProductsController(Controller):
    def list_products(self) -> None:
        context: dict[str, Any] = {}
        # get products from a database
        # context[products] = products
        self.render('products.html', context, MatchaViewEngine())
