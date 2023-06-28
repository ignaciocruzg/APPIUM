from behave import When, Given, Then
from screens.log_in_screen import LoginScreen
from screens.products_screen import ProductosScreen
from screens.shopping_cart_screen import ShoppingCartScreen
from utils.dictionaries.input_data import LOGIN_TEXTS, PRODUCT_TEXTS


@Given("Tengo la aplicacion de saucelabs 1")
def step_impl(context):
    LoginScreen(context)


@Given("Ingreso 'usuario' correcto 1")
def step_impl(context):
    usuario = LOGIN_TEXTS.get("txt_username")
    loginscreen = LoginScreen(context)
    loginscreen.fill_text(*loginscreen.txt_username, text=usuario)


@Given("Ingreso 'contrasena' correcta 1")
def step_impl(context):
    password = LOGIN_TEXTS.get("txt_password")
    loginscreen = LoginScreen(context)
    loginscreen.fill_text(*loginscreen.txt_password, text=password)


@Given("Doy en opcion 'login' 1")
def step_impl(context):
    loginscreen = LoginScreen(context)
    loginscreen.tap_element(*loginscreen.btn_login)


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
