Feature: Shopping Cart

    @smoke
    Scenario: Agregar producto al carrito de compra
      Given Tengo la aplicacion de saucelabsss
      And Ingreso 'usuario' correcto
      And Ingreso 'contrasena' correcta
      And Doy en opcion 'login'
      When Elijo la opcion 'añadir a carrito' del 'producto'
      And Ingreso al carrito de compras
      Then Visualizo el 'nombre' del producto agregado al carrito
      And Visualizo el 'precio' del producto agregado al carrito
