from behave import When, Then
from screens.products_screen import ProductosScreen
from screens.shopping_cart_screen import ShoppingCartScreen
from utils.dictionaries.input_data import PRODUCT_TEXTS


@When("Elijo la opcion 'añadir a carrito' del 'producto'")
def step_impl(context):
    productsscreen = ProductosScreen(context)
    productsscreen.tap_element(*productsscreen.lbl_anadir_producto)


@When("Ingreso al carrito de compras")
def step_impl(context):
    productsscreen = ProductosScreen(context)
    productsscreen.tap_element(*productsscreen.opc_carrito)


@Then("Visualizo el 'nombre' del producto agregado al carrito")
def step_impl(context):
    text_nombre_producto = PRODUCT_TEXTS.get("txt_productname")
    shoppingcartscreen = ShoppingCartScreen(context)
    shoppingcartscreen.assert_text(*shoppingcartscreen.lbl_nombre_producto,
                                   text=text_nombre_producto)


@Then("Visualizo el 'precio' del producto agregado al carrito")
def step_impl(context):
    text_precio_producto = PRODUCT_TEXTS.get("txt_price")
    shoppingcartscreen = ShoppingCartScreen(context)
    shoppingcartscreen.assert_text(*shoppingcartscreen.lbl_precio_producto,
                                   text=text_precio_producto)
