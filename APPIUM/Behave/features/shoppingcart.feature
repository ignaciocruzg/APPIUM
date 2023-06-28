Feature: Shopping Cart

    @smokes
    Scenario: Agregar producto al carrito de compra
      Given Tengo la aplicacion de saucelabs 1
      And Ingreso 'usuario' correcto 1
      And Ingreso 'contrasena' correcta 1
      And Doy en opcion 'login' 1
      When Elijo la opcion 'añadir a carrito' del 'producto'
      And Ingreso al carrito de compras
      Then Visualizo el 'nombre' del producto agregado al carrito
      And Visualizo el 'precio' del producto agregado al carrito
