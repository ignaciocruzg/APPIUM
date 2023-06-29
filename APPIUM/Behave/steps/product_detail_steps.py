from behave import When, Given, Then
from screens.log_in_screen import LoginScreen
from screens.products_screen import ProductosScreen
from screens.product_detail_screen import ProductDetailScreen
from utils.dictionaries.input_data import LOGIN_TEXTS, PRODUCT_TEXTS


@When("Elijo el 'producto'")
def step_impl(context):
    productsscreen = ProductosScreen(context)
    productsscreen.tap_element(*productsscreen.lbl_nombre_producto)


@Then("Visualizo el 'titulo' de 'detalle'")
def step_impl(context):
    text_title_product_detail = PRODUCT_TEXTS.get("txt_title_product_detail")
    productdetailscreen = ProductDetailScreen(context)
    productdetailscreen.assert_text(*productdetailscreen.lbl_title_product_detail, text=text_title_product_detail)


@Then("Visualizo el 'nombre' del 'producto' seleccionado")
def step_impl(context):
    text_nombre_producto = PRODUCT_TEXTS.get("txt_productname")
    productdetailscreen = ProductDetailScreen(context)
    productdetailscreen.assert_text(*productdetailscreen.lbl_nombre_producto, text=text_nombre_producto)


@Then("Visualizo el 'precio' del 'producto' seleccionado")
def step_impl(context):
    text_precio_producto = PRODUCT_TEXTS.get("txt_price")
    productdetailscreen = ProductDetailScreen(context)
    productdetailscreen.assert_text(*productdetailscreen.lbl_precio_producto, text=text_precio_producto)
