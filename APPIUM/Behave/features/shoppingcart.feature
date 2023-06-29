Feature: Shopping Cart

    @regression
    Scenario: Agregar producto al carrito de compra
      Given Ingreso a la app y hago login exitoso
      When Elijo la opcion 'añadir a carrito' del 'producto'
      And Ingreso al carrito de compras
      Then Visualizo el 'nombre' del producto agregado al carrito
      And Visualizo el 'precio' del producto agregado al carrito
