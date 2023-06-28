from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ProductDetailScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_product_detail = (By.XPATH, "//*[contains(@text,'REGRESO A PRODUCTOS')]")
        self.lbl_nombre_producto = (By.XPATH, "//*[contains(@text,'Camisa Sauce Labs Bolt')]")
        self.lbl_precio_producto = (By.XPATH, "//*[contains(@text,'$15.99')]")
