from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ShoppingCartScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_nombre_producto = (By.XPATH, "//*[contains(@text,"
                                              "'Camisa Sauce Labs Bolt')]")
        self.lbl_precio_producto = (By.XPATH, "//*[contains(@text,'$15.99')]")
