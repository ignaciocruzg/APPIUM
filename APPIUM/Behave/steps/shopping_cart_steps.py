from behave import When, Then
from screens.products_screen import ProductosScreen
from screens.product_detail_screen import ProductDetailScreen
from screens.shopping_cart_screen import ShoppingCartScreen
from utils.dictionaries.input_data import PRODUCT_TEXTS, CART_TEXTS


@When("Elijo 'producto'")
def step_impl(context):
    productsscreen = ProductosScreen(context)
    productsscreen.tap_element(*productsscreen.scroll_down_product_name)


@When("Elijo 'Añadir a carrito'")
def step_impl(context):
    productdetailscreen = ProductDetailScreen(context)
    productdetailscreen.tap_element(*productdetailscreen.scroll_down_product_add_cart)


@When("Elijo el 'carrito de compra'")
def step_impl(context):
    productdetailscreen = ProductDetailScreen(context)
    productdetailscreen.tap_element(*productdetailscreen.opc_carrito)


@Then("Visualizo el carrito")
def step_impl(context):
    text_titulo_tu_carrito = CART_TEXTS.get("txt_title_carttxt_title_cart")
    shoppingcartscreen = ShoppingCartScreen(context)
    shoppingcartscreen.assert_text(*shoppingcartscreen.title_tu_carrito,
                                   text=text_titulo_tu_carrito)


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
