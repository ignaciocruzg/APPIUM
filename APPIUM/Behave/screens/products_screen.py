from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ProductosScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (By.XPATH,
                              "//*[contains(@text,"
                              "'PRODUCTOS')]")
        self.lbl_nombre_producto = (By.XPATH,
                                    "//*[contains(@text,"
                                    "'Chamarra Sauce Labs')]")
        self.lbl_anadir_producto = (By.XPATH,
                                    "//*[contains(@text,"
                                    "'AÑADIR A CARRITO')]")
        self.opc_carrito = (By.XPATH,
                            "//android.view.ViewGroup"
                            "[@content-desc=\"test-Carrito\"]")
