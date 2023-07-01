from behave import When, Then
from screens.products_screen import ProductosScreen
from utils.dictionaries.input_data import PRODUCT_TEXTS


@When("Elijo 'filtro'")
def step_impl(context):
    pass


@When("Doy ordenar por precio 'de menor a mayor'")
def step_impl(context):
    pass


@Then("Visualizo el primer producto con precio menor")
def step_impl(context):
    pass


@Then("Visualizo el ultimo producto con precio mayor")
def step_impl(context):
    pass
