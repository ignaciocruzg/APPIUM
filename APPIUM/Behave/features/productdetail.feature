Feature: Product Detail

    @smoke
    Scenario: Visualizar el detalle de un producto
      Given Tengo la aplicacion de saucelabs 2
      And Ingreso 'usuario' correcto 2
      And Ingreso 'contrasena' correcta 2
      And Doy en opcion 'login' 2
      When Elijo el 'producto'
      Then Visualizo el 'titulo' de 'detalle'
      And Visualizo el 'nombre' del 'producto' seleccionado
      And Visualizo el 'precio' del 'producto' seleccionado