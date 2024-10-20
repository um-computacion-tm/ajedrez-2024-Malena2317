# Changelog

Todos los cambios importantes en este proyecto serán documentados en este archivos.

[1.46.0] - 2024-10-14

**clase Pawn**
Cambios en la Función is_valid_move

Refactorización de Complejidad Cognitiva:Se simplificó el flujo de control eliminando la variable is_valid y utilizando return de manera directa en los puntos de salida.

implificación de Condicionales:Se reorganizaron las condiciones relacionadas con el movimiento del peón, utilizando return en lugar de asignar valores a una variable intermedia

evisiones de Lógica:

Condiciones para Peones Blancos:
      Se verificó si el peón blanco solo puede avanzar hacia adelante y se establecieron las condiciones correspondientes para un movimiento de dos casillas en su primer movimiento.

Condiciones para Peones Negros:
      Se consolidó la lógica que verifica los movimientos permitidos y se aseguraron condiciones claras y concisas para determinar si un movimiento es válido.

Comprobación de Movimiento a la Posición de Destino:Se realizó la verificación de si se puede mover a la posición de destino utilizando el método can_move_to de manera más directa, eliminando la necesidad de utilizar una variable temporal para almacenar el estado.

Separación de Lógica: Las funciones is_valid_white_move e is_valid_black_move se mantienen para manejar la lógica de validación de forma clara y concisa, lo que reduce la complejidad cognitiva de la función principal is_valid_move

**Clase Rook**

Método move:Se implementó un método move que actualiza la posición de la torre en el tablero si el movimiento es válido.

Método is_valid_move:Se añadió la verificación de si el movimiento está dentro del tablero usando is_within_board y si el camino está libre mediante _is_path_clear

**Tests de Rook**

Método Rook_Move: Se ajustó para trabajar directamente con la lista board y realizar las verificaciones de movimientos y actualizaciones del tablero.

Pruebas Añadidas: 
      Movimiento a una casilla ocupada por una pieza del mismo color.
      Movimiento a una casilla ocupada por una pieza de diferente color.
      Movimiento fuera del tablero con coordenadas negativas.


[1.45.0] - 2024-10-13

**Cambios en la Clase King**

Método is_valid_move:
      Se mejoró la validación del movimiento del rey para asegurar que solo pueda moverse a una casilla adyacente.
      El cálculo de la distancia entre la posición actual y la posición de destino se realiza usando diferencias absolutas entre filas y columnas.
      Se verifica que la casilla de destino esté vacía o que contenga una pieza de un color diferente. Si hay una pieza del mismo color en la casilla de destino, el movimiento es inválido.
      Se agregó un mensaje de diagnóstico "Movimiento inválido para el Rey." para ayudar a identificar por qué un movimiento es rechazado durante la ejecución.

Método move:
      El método move ahora solo actualiza las coordenadas del rey si el movimiento es válido, utilizando el método is_valid_move para verificar la validez del mismo.
      Si el movimiento es válido, se actualiza la posición de la pieza en el tablero, reemplazando la casilla anterior con None y colocando el rey en la nueva casilla.
      Si el movimiento no es válido, el método devuelve False sin realizar cambios en el tablero.

**Cambios en los Tests Unitarios para la Clase King**

Método move_and_assert:
      Este método intenta mover el rey a una posición especificada y verifica que el resultado coincida con el esperado.
      Se agrega una verificación de la posición actual del rey tras el movimiento utilizando self.assert_king_position.
      Esto asegura que, si el movimiento es válido, el rey se encuentra efectivamente en la nueva posición, y si es inválido, permanece en su posición original.

Método place_piece_and_move:
      Se creó este método para facilitar la colocación de otras piezas en el tablero y probar cómo el rey interactúa con ellas.
      Se coloca otra pieza (otro rey, ya sea blanco o negro) en la posición de destino y se prueba si el movimiento del rey original es válido o no.
      Esto es útil para verificar que el rey no pueda ocupar una casilla ya ocupada por otra pieza del mismo color y que pueda capturar una pieza de un color contrario.

Casos de Prueba Específicos:
test_mover_una_casilla_hacia_abajo: Verifica que el rey puede moverse una casilla hacia abajo.
test_mover_en_diagonal: Verifica que el rey puede moverse en diagonal una casilla.
test_mover_fuera_del_tablero: Verifica que el rey no puede moverse fuera de los límites del tablero.
test_mover_a_una_posicion_invalida: Verifica que el rey no puede realizar un movimiento que no esté permitido por las reglas (como mover más de una casilla).
test_mover_a_una_posicion_ocupada_por_una_pieza_del_mismo_color: Verifica que el rey no puede moverse a una posición donde ya hay una pieza de su mismo color.
test_mover_a_una_posicion_ocupada_por_una_pieza_de_diferente_color: Verifica que el rey puede capturar una pieza de un color contrario moviéndose a su posición.


[1.44.0] - 2024-10-11

**Clase Queen**
Cambios en el constructor __init__:Se ha agregado la asignación explícita del atributo color en el constructor para mejorar la claridad y la accesibilidad del color de la reina.

Cambios en el método is_valid_move:
      -Validación de tablero: Se agregó una verificación para asegurarse de que la posición de destino esté dentro de los límites del tablero y que no sea la misma que la posición actual de la reina.
      -Verificación de ocupación: Se añadió una comprobación para verificar si la posición de destino está ocupada por una pieza del mismo color, evitando que la reina se mueva a una casilla que contenga una pieza aliada.
      -Lógica de movimiento: La lógica se ha mantenido, pero se mejoró con la verificación de los movimientos diagonales, horizontales y verticales. Se implementaron bucles para asegurarse de que no haya piezas en el camino de la reina durante el movimiento diagonal o recto.
      -Nuevo método move:Se implementó un nuevo método move que incorpora verificaciones adicionales para asegurarse de que el movimiento de la reina sea válido y que la posición de destino esté dentro del tablero.

**Clase de Test TestQueen**

Cambios en la estructura de los tests:

      -Se eliminaron las verificaciones de posición en auxiliar_move, en su lugar se optó por usar self.assertEqual únicamente para el resultado del movimiento. Esto simplifica la lógica de los tests.

Se agregaron nuevos tests para validar situaciones adicionales:
      -Movimientos fuera del tablero: Se introdujo un nuevo test test_move_out_of_board para asegurar que la reina no se pueda mover fuera de los límites del tablero.
      -Movimiento a la misma posición: Se agregó un test test_move_to_same_position para verificar que no se permita mover a la misma posición.
      -Pruebas para movimientos diagonales: Se introdujeron tests específicos para validar movimientos diagonales ocupados por piezas del mismo color o del oponente.

[1.43.0] - 2024-10-10

**Cambios en la Clase Pawn**
Adición de atributo has_moved:
      Se añadió el atributo has_moved en el constructor para rastrear si el peón ha sido movido.

Nuevo método move:
      Se introdujo un método move que maneja la lógica de movimiento y verifica si el movimiento es válido llamando a is_valid_move.

Modificaciones en is_valid_move:    
      -Se mejoró la lógica para comprobar movimientos permitidos según el color del peón (blanco o negro).
      -Se incluyó la lógica para permitir que los peones avancen dos casillas solo en su primer movimiento.
      -Se eliminaron mensajes de depuración en caso de un movimiento inválido.

**Cambios en las Pruebas (TestPawn)**

Actualización del método mover_peon_y_verificar:
      -Se renombró a move_pawn_and_verify.
      -Se añadió impresión del estado del tablero antes y después de los movimientos para facilitar la depuración.

Pruebas adicionales y ajustes:
      -Se añadieron pruebas para verificar el movimiento de dos espacios hacia adelante para peones blancos y negros.
      -Se incluyó una prueba para verificar si un peón intenta moverse a una casilla ocupada por otra pieza.
      -Se mejoró la verificación de movimientos fuera de los límites del tablero

**TestBishop**

Refactorización de place_piece: 
      Se mejoró la reutilización de la función place_piece, eliminando la duplicación de código para posicionar piezas en el tablero.

Nuevo método _assert_move: 
      Se introdujo el método _assert_move para simplificar y estandarizar la verificación de movimientos válidos e inválidos, reduciendo la repetición de lógica en los tests.

Eliminación de código redundante: 
      Se eliminaron las llamadas repetitivas a assertTrue y assertFalse en cada prueba, sustituyéndolas por el nuevo método _assert_move para una mayor claridad y eficiencia.

Manejo de errores en _assert_move: 
      Se añadió un control de excepciones (try-except) en el método _assert_move para manejar situaciones en las que se intenta mover a una posición inválida, garantizando un resultado más robusto.

Cambio de nombre de variables: 
      Se ajustaron los nombres de las variables para mejorar la claridad del código, usando row y col en lugar de nombres menos descriptivos.

Se eliminó el código duplicado:
       Varias pruebas como test_move_diagonal_free y test_move_to_enemy_piece reutilizan la misma lógica a través de _assert_move, eliminando la redundancia previa.

Nueva prueba test_invalid_move_horizontal: 
      Se añadió una prueba para verificar que el alfil no puede moverse horizontalmente, asegurando una cobertura más completa de los posibles movimientos inválidos.



[1.42.0] - 2024-10-09

Cambios Realizados

Refactorización de Métodos de Prueba:
      Se introdujo el método assert_valid_move(self, row, col, expected) para centralizar la verificación de movimientos válidos, lo que mejora la legibilidad y la reutilización del código.
      
Consolidación de Pruebas:
      Se eliminó la duplicación de pruebas individuales y se agruparon pruebas de movimientos inválidos en el nuevo método test_invalid_moves(), donde se testean múltiples movimientos no válidos en un solo método, simplificando así el código.

Nueva Prueba para Movimiento a Casilla Ocupada:
      Se añadió test_move_to_occupied_square() para comprobar que el caballo no puede moverse a una casilla ocupada por una pieza del mismo color, mejorando la cobertura de pruebas.

Validación de Captura de Pieza Enemiga:
      Se modificó test_move_to_enemy_piece() para confirmar que el caballo puede moverse a una casilla ocupada por una pieza enemiga.

Prueba para Movimiento a la Misma Posición:     
      Se incluyó test_move_to_same_position() para asegurarse de que el caballo no puede moverse a la posición en la que ya se encuentra.

Actualización en la Prueba de Movimientos Válidos en 'L':
      Se añadió test_valid_L_shape_moves() para verificar todos los movimientos válidos en 'L' desde la posición actual del caballo, asegurando una mejor cobertura de las reglas de movimiento


[1.41.0] - 2024-10-08

Refactorización de tests:
      Se introdujeron métodos auxiliares para reducir redundancia en el código de test.
      Se utilizaron métodos como place_piece para colocar piezas en el tablero y centralizar la lógica.
      Se mejoró la verificación de movimientos inválidos y de intentos de mover a una casilla ocupada por una pieza del mismo color.

Cambios en TestBishop:

Nuevos tests:
      Se añadió un test test_move_out_of_board para verificar que el alfil no se pueda mover fuera del tablero.
      Se añadió un test test_move_diagonal_up_left para verificar movimientos diagonales hacia arriba e izquierda.
      Se añadieron tests test_move_to_enemy_piece y test_move_to_same_color_piece para probar movimientos a casillas ocupadas por piezas enemigas y del mismo color, respectivamente.

Refactorización:
      El método place_piece se utiliza para evitar repetir código al colocar piezas en el tablero.
      Se reemplazaron assertEqual con llamadas a assertTrue y assertFalse para verificar los movimientos válidos o inválidos antes de realizar movimientos efectivos.
      Uso de get_coordinates en vez de acceder directamente a las variables de fila y columna.

Cambios en TestKnight:

Nuevos tests:
      Se añadieron varios tests para movimientos en todas las direcciones posibles de "L" (hacia arriba, abajo, izquierda y derecha), como test_move_L_shape_up_left y test_move_L_shape_down_right.
      Se añadió un test test_move_out_of_board para verificar que el caballo no se pueda mover fuera del tablero.

Refactorización:
      Se implementó el método auxiliar place_piece para colocar piezas en el tablero y evitar redundancia.
      Uso del método is_valid_move antes de mover piezas para verificar la validez del movimiento.
      Mejora en la verificación de movimientos hacia casillas ocupadas por piezas enemigas y del mismo color con assertTrue y assertFalse antes de realizar el movimiento.
      
      
[1.40.0] - 2024-10-06

Refactorización del método move:

Clase Base (Piece):

      -Se mantuvo el método move, que implementa la lógica de movimiento común para todas las piezas
      -Se eliminó la duplicación del método move en las subclases, simplificando así la implementación del movimiento de piezas.

Subclases (Rook, King, Queen, Pawn, Knight, Alfil):

      -Se eliminó el método move de todas las subclases, que antes redefinían la lógica de movimiento.
      -Cada subclase ahora utiliza directamente el método move de la clase base Piece, lo que evita la duplicación de código.
      -Cada subclase continúa implementando su propia lógica de validación de movimientos a través del método is_valid_move.

[1.39.0] - 2024-10-05

Método _is_path_clear:

      -Se agregó una nueva lógica para calcular la dirección del movimiento utilizando el método _get_step.
      -Se modificó la lógica para recorrer el camino desde la posición actual hasta la de destino utilizando un bucle while.

Método _get_step:
      
      -Se agregó un nuevo método para calcular la dirección del movimiento en lugar de utilizar condicionales.

[1.38.0] - 2024-10-04

método is_valid_move:
      Se ha agregado el método is_valid_move para validar si un movimiento es legal. Este método recibe una pieza y las coordenadas de destino, verificando si el movimiento cumple con las reglas del juego en el contexto del tablero.

Método move:
      El método move utiliza el nuevo método is_valid_move para validar los movimientos antes de realizarlos.

Método convert_position:
       Se ha añadido el método convert_position, que convierte una posición en notación de ajedrez (como 'D2') a coordenadas de tablero (fila, columna). Este método permite validar la entrada del jugador y verificar que la posición sea válida.

Método play_turn:
      El método play_turn sigue el mismo flujo, pero con la validación mejorada gracias al nuevo método convert_position. La conversión de las entradas en coordenadas ahora es más robusta, manejando errores como posiciones fuera de los límites.


[1.37.0] - 2024-10-03

Modificación del método move
      Se ha añadido la validación de movimientos con el método is_valid_move, que se asegura de que la pieza pueda moverse a la posición deseada antes de cambiar el turno.

Reescritura del método play_turn
      Se corrigió el formato y la indentación del método play_turn para que funcione correctamente. Ahora es un método regular en lugar de ser una propiedad.
      Se corrigió la lógica de manejo de la rendición.
      Se agregó la conversión de las posiciones ingresadas por el usuario (origin y destination) en coordenadas utilizables con el método convert_position.
      Se incluyó la validación de que las posiciones ingresadas por el usuario sean correctas antes de realizar el movimiento.

Nueva función is_valid_move
      Se introdujo una nueva función is_valid_move dentro del método move para validar si un movimiento es legal antes de realizarlo.

Manejo de posiciones
      Se implementó la conversión de posiciones de origen y destino usando convert_position, lo que asegura que las entradas de texto del jugador (como "D2") se conviertan correctamente en coordenadas de tablero.

[1.36.0] - 2024-10-02

-**class chess**
Agregado:

-Se añadió el atributo game_over en el constructor __init__ para llevar un control sobre si el juego ha terminado.
-Se agregó un nuevo método play_turn (dentro de la propiedad), que permite controlar el flujo de cada turno del juego. Incluye lógica para imprimir el tablero y obtener las    posiciones de origen y destino de una pieza, además de la posibilidad de que un jugador se rinda ingresando 'q'.
-En el nuevo método play_turn, se agregó la validación para terminar el juego cuando game_over es True, mostrando el tablero y solicitando las coordenadas del usuario en cada turno.

[1.35.0] - 2024-10-01

-**KING**
Eliminación de código duplicado en move:

Se ha eliminado el código redundante que verificaba si el movimiento era válido dos veces.
La nueva versión encapsula la lógica de movimiento en una sola llamada, lo que mejora la claridad y evita repeticiones:
Llama a is_valid_move y, si el movimiento es válido, realiza el movimiento con super().move, todo en una sola líne

-**PAWN**

Modificación del constructor:

Se utiliza super().__init__(0, 0, color) para inicializar la posición en (0, 0) y llamar al constructor de la clase base Piece. Se elimina la referencia a self.__color__.

Reestructuración de is_valid_move:

Refactorización:
      El código fue reorganizado para hacer el flujo de la lógica más claro y evitar duplicación innecesaria.
      Se agrega una variable is_valid para realizar todas las verificaciones y luego devolver el resultado de una sola vez, en lugar de devolver False en cada error.

Validaciones de movimiento:
      Se sigue verificando que el peón solo puede moverse en la misma columna.
      El cálculo de la diferencia de filas (row_diff) es ahora más conciso y se usa para validar que el peón avanza en la dirección correcta (blanco hacia adelante y negro hacia adelante) y que no avanza más de una casilla.
      Se eliminan las verificaciones redundantes sobre el movimiento de los peones negros que estaban duplicadas en la versión anterior.

[1.34.0] - 2024-09-30

 Clase Pawn :
      Se agregó un nuevo método move que verifica si el peón realiza movimientos válidos:
      Impide mover el peón hacia atrás.
      Verifica que no se mueva lateralmente.
      Permite avanzar solo una fila por turno.
      Se implementaron condiciones específicas para peones blancos y negros.

Clase Alfil:

      Se agregó el método is_valid_diagonal_move para validar movimientos en diagonal de manera detallada:
      Verifica que el movimiento sea diagonal.
      Comprueba si la casilla destino está vacía.
      El método mover ahora actualiza la posición del Alfil en el tablero y devuelve True si el movimiento es válido.
      Se incluyó un método get_row y get_col para obtener la posición actual del Alfil.

Clase Knight:

      Se eliminó el uso de la clase base Piece, y se reemplazó por un método move específico que realiza las verificaciones de movimiento:
      Verifica que el movimiento sea en forma de "L".
      Comprueba si la casilla destino está vacía o si está ocupada por una pieza enemiga.
      Se añadieron los métodos get_row, get_col, set_row, y set_col para obtener y actualizar la posición del caballo

[1.33.0] - 2024-09-29

Eliminación de la clase Position:
Se eliminó la clase Position y su lógica de manejo de posiciones (coordenadas y verificación de límites del tablero) ahora está directamente dentro de la clase Piece.

Cambio en el método de movimiento:
El método move ahora se implementa completamente dentro de la clase Piece en lugar de delegar la lógica a la clase Position. Esto hace que la clase Piece sea responsable tanto de la validación del movimiento como de la actualización de las coordenadas de la pieza.

Nuevo método get_coordinates:
Se agregó el método get_coordinates que devuelve la posición actual de la pieza como una tupla (row, col).

Nuevo método update_coordinates:
Se introdujo el método update_coordinates, que actualiza las coordenadas de la pieza con una nueva fila y columna. Anteriormente, la lógica de actualización de posición estaba en la clase Position.

Iconos en lugar de strings:
En la nueva versión, se agregó el método display_icon para devolver el icono correspondiente al color de la pieza (white_icon o black_icon), en lugar de utilizar los atributos white_str y black_str como en la versión anterior.


Verificación del tablero (is_within_board):
Ahora, la validación de si una posición está dentro del tablero se realiza directamente en la clase Piece mediante el método is_within_board. Anteriormente, esta lógica estaba en la clase Position.

Método can_move_to:
Se integró el método can_move_to en la clase Piece, que verifica si una pieza puede moverse a una nueva posición, comprobando tanto los límites del tablero como la ocupación de la casilla. Antes, esto se realizaba mediante la clase Position.

Excepción NotImplementedError:
Se mantuvo el método is_valid_move que lanza una excepción NotImplementedError, indicando que las subclases deben implementar su propia lógica de validación de movimiento, similar a la versión anterior.


[1.32.0] - 2024-09-27

Reestructuración de la inicialización:

El método initialize_board fue creado para separar la lógica de inicialización de piezas del método __init__.Ahora se inicializa el tablero y se colocan las piezas en sus posiciones iniciales dentro de este método.

Nuevo método de impresión:
Se agregó el método print_board para imprimir el tablero de forma visual en la consola, con un formato más claro para el usuario, representando casillas vacías con guiones ("-").

Nuevo método de movimiento:
Se añadió el método move_piece para mover una pieza de una casilla a otra, permitiendo especificar las coordenadas de origen y destino.

Cambio en el uso de la representación:
El método __str__ ahora convierte el tablero a una cadena de texto utilizando self.__positions__, pero la lógica de impresión ha sido mejorada con el nuevo método print_board.


[1.31.0] - 2024-09-26
-**TEST ALFIL**
Cambios realizados:

Refactorización del código repetido:
Se creó un método auxiliar privado _mover_alfil para encapsular la lógica común de prueba que se repetía en varios métodos de prueba. Esto elimina la duplicación y hace que el código sea más limpio y fácil de mantener.

Simplificación de las pruebas:
Los métodos de prueba ahora utilizan el nuevo método _mover_alfil, lo que reduce la cantidad de líneas de código en cada prueba y mejora la claridad del propósito de cada una.

-**PIEZA ALFIL**

Cambios realizados:

Inicialización del tablero:
-En el constructor __init__, se actualizó la inicialización de self.board para crear un nuevo tablero vacío por defecto si no se proporciona uno. Esto asegura que el alfil tenga un tablero para interactuar sin depender de un argumento externo.

Método is_valid_diagonal_move:
-Se agregó un nuevo método is_valid_diagonal_move, que encapsula la lógica para validar si el movimiento del alfil es diagonal y si la casilla de destino está vacía. Esto mejora la legibilidad y reutilización del código.

Refactorización del método mover:
-El método mover ahora utiliza is_valid_diagonal_move para validar los movimientos. Si el movimiento no es válido, devuelve False en lugar de lanzar una excepción, lo que simplifica el manejo de errores y hace que el código sea más fácil de seguir.
-Si el movimiento es válido, se actualiza la posición de la pieza en el tablero y se libera la casilla de origen.

[1.30.0] - 2024-09-25

-**Factrorizando funcion move**

-Se introdujo una nueva función move_valid, separando la validación del movimiento de la actualización de la posición. Esto mejora la legibilidad y reutilización del código.

-La lógica de validación del movimiento (distancia de una casilla y verificación de la ocupación del destino) se extrajo a move_valid, eliminando la duplicación en el método move.


[1.29.0] - 2024-09-24

-**PAWN**

Corrección en el Método move:

Se han reorganizado y corregido las validaciones de movimiento del peón:
La validación de movimiento en la misma fila se mantiene.
Se han corregido las condiciones de movimiento hacia adelante para los peones:
Peón Blanco: Se ha cambiado de to_pos.row < start_pos.row a to_pos.row < start_pos.row para validar el movimiento hacia adelante.
Peón Negro: Se ha cambiado de to_pos.row > start_pos.row a to_pos.row > start_pos.row para validar el movimiento hacia adelante.

Eliminación de Código Duplicado:
Se ha eliminado el código duplicado al final del método move, asegurando que solo se mueva el peón si las verificaciones son exitosas.

Lógica de Retorno:
El método move ahora devuelve False si el movimiento no es válido, en lugar de un resultado implícito, para mejorar la claridad del flujo de control.

-**PAWN TEST**

Método mover_peon_y_verificar:
Se introdujo el método mover_peon_y_verificar, que encapsula la lógica para mover el peón y verificar el resultado.
Esto reduce la duplicación de código y mejora la legibilidad.

Pruebas de Movimiento:
Las pruebas utilizan mover_peon_y_verificar, lo que hace que cada prueba sea más concisa, mejorando la claridad y la estructura del código de pruebas al eliminar la redundancia y agrupar la lógica común.

[1.28.0] - 2024-09-23

**Uso de métodos auxiliares para simplificar las pruebas:**

Se introdujeron dos nuevos métodos privados: _setup_patches y _run_test. Esto elimina la repetición de código en las pruebas individuales al encapsular el comportamiento repetitivo de los parches (patch) y la ejecución de las pruebas.
**_setup_patches:** Encapsula los parches para los métodos input, print y Chess.move, permitiendo reutilizar esta lógica en las pruebas sin duplicación de código.
**_run_test:** Este método simplifica la lógica principal de las pruebas. Recibe los efectos secundarios de la entrada (input_side_effect), el número de llamadas esperadas para input, print, y move, y los verifica tras la ejecución de la prueba.

**Reducción de duplicación de código:**

La versión anterior contenía bloques de código duplicados en las tres pruebas (test_happy_path, test_not_happy_path, test_more_not_happy_path), con pequeñas variaciones en las entradas y verificaciones. La nueva versión usa el método _run_test para unificar esta lógica

**Claridad en las entradas y verificaciones:**

En la nueva versión, se pasa una lista de los efectos de input directamente como argumento a _run_test, junto con los valores esperados para el conteo de llamadas de input, print, y move. 

[1.27.0] - 2024-09-22

-**solucionando problemas en los test de rook**

**Inicialización de las piezas en el tablero:**

En la nueva versión, durante el método setUp, se agregaron las torres blanca y negra directamente en sus posiciones iniciales en el tablero (self.board.set_piece(0, 0, self.rook_blanca) y self.board.set_piece(7, 7, self.rook_negra)). Esto asegura que las piezas estén correctamente ubicadas antes de realizar las pruebas.

**Validación de posiciones iniciales:**

Se añadió una verificación para asegurarse de que la posición inicial de la torre (start_row y start_col) no sea None. En caso de que alguna de estas coordenadas sea inválida, se lanza un error utilizando self.fail("Start row or column is None"). Esto garantiza que siempre se trabajará con piezas correctamente posicionadas antes de intentar moverlas.

**Ajustes en la prueba test_mover_torre_horizontal:**

En la versión antigua, la torre negra se movía horizontalmente en la primera fila (fila 0). En la nueva versión, esta prueba fue modificada para que la torre negra se mueva en la última fila (su posición inicial en la fila 7), manteniendo consistencia con su ubicación inicial definida en setUp.

**Agregado explícito de obstáculos en la prueba test_mover_torre_con_obstaculo:**

En la nueva versión, se añade un obstáculo explícito en el tablero para esta prueba (self.board.set_piece(2, 0, Piece(2, 0, "WHITE"))), lo que simula una pieza en el camino de la torre blanca. En la versión anterior, se asumía que había un obstáculo sin definirlo explícitamente. 

[1.26.0] - 2024-09-20

-**Refactorización de métodos duplicados**:

Se eliminó la duplicación de código en los métodos _is_valid_horizontal_move y _is_valid_vertical_move.
Se creó un nuevo método privado llamado _is_path_clear que unifica la lógica para verificar si el camino está libre tanto en movimientos horizontales como verticales.

-**Parámetros**:
**start**: posición inicial (puede ser fila o columna, según el tipo de movimiento).
**end**: posición final (puede ser fila o columna, según el tipo de movimiento).
**fixed**: valor fijo que se mantiene constante durante la iteración (por ejemplo, la fila en un movimiento horizontal o la columna en un movimiento vertical).
**is_horizontal**: booleano que indica si se trata de un movimiento horizontal o vertical, para acceder a las piezas correspondientes del tablero.

[1.25.0] - 2024-09-19

Cambios realizados en la nueva versión:

-**Refactorización del código repetido en funciones auxiliares**:Se creó la función auxiliar auxiliar_move que maneja la lógica común de verificación de movimientos (válidos e inválidos) y la actualización de las coordenadas de la reina.

Se agregó la función auxiliar_move_to_occupied para manejar los casos en los que la reina intenta moverse a una posición ocupada por otra pieza (tanto del mismo color como del oponente).

-**Limpieza y reducción de la duplicación de código**:Las funciones de prueba test_move_horizontal, test_move_vertical, test_move_diagonal, y test_invalid_move ahora utilizan la función auxiliar auxiliar_move para eliminar la duplicación de la lógica de prueba.

Las pruebas de movimientos hacia posiciones ocupadas ahora usan la nueva función auxiliar_move_to_occupied, lo que simplifica la creación de piezas ocupantes y reduce la repetición de código.

-**Uso más claro de parámetros**:En lugar de escribir directamente la lógica dentro de cada prueba, se pasó a usar parámetros (row, col, color, expected_result) en las funciones auxiliares para hacer las pruebas más flexibles y fáciles de leer.

[1.24.0] - 2024-09-17

-**REY**:
Cambios Introducidos:

Validación de Movimiento del Rey: Se simplificó el cálculo utilizando la diferencia absoluta entre las filas y columnas. Esto asegura que el rey puede moverse solo una casilla en cualquier dirección de manera más directa y precisa.

Verificación de la Casilla Destino:La verificación se mantiene igual, pero se ha simplificado la lógica. Ahora se usa is None para comprobar si la casilla está vacía y se mantiene la verificación del color contrario en una sola condición.

Movimiento del Rey:El movimiento se realiza si las condiciones se cumplen, con la lógica simplificada y la operación realizada en un bloque condicional más compacto.

-**TEST REY**:

Refactorización de Métodos de Prueba:Se crearon métodos de utilidad move_and_assert y place_piece_and_move para reducir la duplicación y mejorar la legibilidad del código.

Nuevo Método move_and_assert: Se introdujo el método move_and_assert para mover el rey y verificar su posición de manera consistente.

Nuevo Método place_piece_and_move: Se introdujo el método place_piece_and_move para manejar la colocación de una nueva pieza y verificar el movimiento en un solo lugar, reduciendo la repetición y facilitando la actualización de la lógica de prueba.

Mejora en assert_king_position:El método assert_king_position se ajustó para incluir un comentario aclaratorio y se mantiene el comportamiento sin cambios significativos.



[1.23.0] - 2024-09-16
-**clase queen**:

-**Constructor (__init__)**:Se reemplazó la inicialización manual de atributos por super().__init__ para aprovechar la clase base Piece.
-**Método move**:Se simplificó al delegar la lógica de movimiento en métodos auxiliares (is_horizontal_or_vertical, is_diagonal, y make_move).
-**Nuevo Método is_valid_move**:Se agregó para verificar si un movimiento es válido.
-**Nuevo Método make_move**:Se introdujo para realizar movimientos tras validar la jugada.
-**Nuevos Métodos Auxiliares**:is_horizontal_or_vertical y is_diagonal se añadieron para manejar la lógica de los movimientos específicos.


-**clase position y piece**:

-**Cambios en la Clase Piece**:

Constructor (__init__): Ahora inicializa también las posiciones row y col junto con el color.
Método move: Ahora delega la lógica de movimiento en la clase Position, utilizando to_position para realizar el movimiento.
Cambio en la Interacción con la Clase Position: Se delega la lógica de validación de movimiento a Position, mejorando la separación de responsabilidades y la modularidad del código.

-**Cambios en la Clase Position**:
Constructor (__init__):Cambia a usar atributos privados __row__ y __col__, mejorando el encapsulamiento.
-**Método can_move_to**:Agregado para verificar si la pieza puede moverse a una nueva posición, considerando la presencia de otras piezas y el color.
-**Método move**:Ahora realiza la verificación completa del movimiento, incluyendo si la nueva posición está dentro del tablero y si el movimiento es válido según el color de la pieza.

[1.22.0] - 2024-09-15

Eliminación de Código Repetitivo:

Se eliminó el código repetitivo al utilizar el nuevo método Mover_y_Verificar, que ahora encapsula la lógica de mover y verificar el resultado en lugar de repetirla en cada prueba.

Modificación en Mover_y_Verificar:

Se simplificó la firma del método Mover_y_Verificar, eliminando parámetros individuales y utilizando una tupla para la posición esperada.

Refactorización de Pruebas:

Las pruebas test_move_L_shape, test_move_not_L_shape, test_move_to_same_color_piece y ahora usan el método move_and_check, lo que reduce la duplicación de código y mejora la mantenibilidad.

Actualización en place_piece:

La función place_piece se mantiene igual, pero se mejoró el uso en las pruebas para colocar piezas en el tablero de manera más limpia.

[1.21.0] - 2024-09-13
-Refactorización de Test_Move:

-Cambio: Se actualizó el método Test_Move para simplificar la prueba de movimientos de la pieza. -Acción: Ahora se pasa la posición inicial de la pieza (fila y columna) directamente al método en lugar de obtenerla dentro de Test_Move. -Resultado: Esta modificación facilita la verificación del movimiento de la pieza, asegurando que se coloque correctamente en la nueva posición o permanezca en la original según el resultado esperado. Nuevo Método get_piece_position:

Cambio: Se introdujo un nuevo método para obtener la posición de una pieza en el tablero. Acción: Este método recorre el tablero para encontrar y retornar las coordenadas de la pieza especificada. Resultado: Permite obtener fácilmente la posición actual de cualquier pieza en el tablero, facilitando la gestión de movimientos en las pruebas.

[1.21.0] - 2024-09-12
Se creó el método auxiliar assert_king_position(row, col, result) para eliminar la duplicación de código en la validación de la posición del rey después de cada movimiento. -Mejoras: Se reemplazaron las verificaciones individuales de la posición del rey en los tests (test_mover_una_casilla_hacia_abajo, test_mover_en_diagonal, etc.) con llamadas al nuevo método assert_king_position, haciendo el código más limpio y reutilizable. -Metodos: Se eliminó la repetición de las sentencias assertEqual para validar las posiciones del rey en múltiples pruebas, centralizando la lógica de validación. -Mantenibilidad: Ahora, cualquier cambio en la forma de verificar la posición del rey solo necesita realizarse en un único lugar (assert_king_position), simplificando futuras modificaciones.

[1.21.0] - 2024-09-11
-Cambios Realizados:

-Refactorización: Se ha creado el método Test_Move para consolidar la lógica de prueba repetida en un solo lugar. -Código Anterior: Los métodos de prueba (test_mover_torre_vertical, test_mover_torre_horizontal, etc.) contenían bloques de código repetitivos para colocar la pieza, realizar el movimiento y verificar el resultado. -Código Nuevo: Los métodos de prueba utilizan Test_Move para realizar estas tareas de manera más concisa y evitar la duplicación de código. Verificación del Movimiento: -Código Anterior: Cada método verificaba el movimiento, la posición inicial, y la posición final directamente en el mismo método. -Código Nuevo: La verificación se realiza en el método Test_Move, simplificando los métodos de prueba individuales.

[1.21.0] - 2024-09-10
-Introducción de movimiento_valido: -Se creó la variable movimiento_valido al inicio de la función, inicializándola en True. Esta variable se usa para determinar si el movimiento es válido o no. -Anteriormente, el código contenía múltiples return para salir de la función en cada caso en que el movimiento no era válido. Ahora, movimiento_valido se actualiza en cada verificaciónn.

-Eliminación de múltiples return: Ahora solo hay un único return al final, que devuelve el valor de movimiento_valido.

-Flujo más claro: Todas las verificaciones se realizan antes de decidir si el movimiento es válido, haciendo el código más legible sin cambiar la lógica.

[1.20.0] - 2024-09-08
-Agregando funcion es is_valid_diagonal_move:

-Descripción -Constructor de la clase InvalidMoveBishop ahora guarda la posición del error y un mensaje personalizado que incluye la posición en la que ocurre el error. -Se sobreescribió el método str en InvalidMoveBishop para proporcionar un mensaje de error más claro cuando se muestra la excepción. -Se incluyó la función is_valid_diagonal_move dentro de la clase InvalidMoveBishop para verificar si un movimiento diagonal es válido en un tablero de ajedrez: -Verifica que el movimiento sea diagonal al comparar las diferencias absolutas entre las filas y columnas. -Lanza una excepción InvalidMoveDiagonal si el movimiento no es diagonal. -Verifica si la casilla de destino está ocupada, lanzando una excepción si es así.

[1.19.0] - 2024-09-07
-Refactorización de la Función move en la Clase Piece

-Descripción: La función move en la clase Piece ha sido refactorizada para ajustar el número de argumentos, cumpliendo así con el límite permitido de cinco argumentos.

-Problema Original: La función move original tenía seis argumentos (self, start_row, start_col, to_row, to_col, board), lo que excedía el límite de cinco argumentos permitidos por las reglas de diseño.

-Solución: Se ha simplificado la función para utilizar dos objetos Position que encapsulan la información de las posiciones de inicio y destino. Esto permite que la función move acepte sólo cinco argumentos en total, reduciendo la complejidad y cumpliendo con las restricciones.

[1.18.0] - 2024-09-06
-Descripción del Cambio: Se realizó una refactorización en la función is_valid_move para reducir su complejidad cognitiva. La versión anterior tenía una complejidad cognitiva de 20, lo que supera el límite recomendado de 15. La refactorización incluye la simplificación de las verificaciones de movimiento horizontal y vertical, así como la mejora en la legibilidad del código.

-Cambios Realizados Refactorización de is_valid_move: -Motivo: Reducir la complejidad cognitiva de la función que originalmente supera el límite recomendado. -Acción: Simplificación de la lógica de validación de movimientos horizontales y verticales.

[1.17.0] - 2024-09-05
-Corrección de Acceso a Atributos Privados: Se reemplazó el acceso directo a los atributos privados row y col de la clase Caballo con métodos getter y setter (get_row(), get_col(), set_row(row), set_col(col)) para seguir las buenas prácticas de encapsulamiento en Python.

-Actualización de la Función mover_caballo: Modificada la función para utilizar métodos getter y setter en lugar de acceder directamente a los atributos privados. Añadido manejo de la excepción InvalidMoveKnight cuando el movimiento no es válido para el caballo. La función verifica si la casilla destino está vacía antes de mover el caballo y retorna True si el movimiento es exitoso y False si la casilla está ocupada.

-Definición de Excepción: Se ha incluido la definición de la excepción InvalidMoveKnight, que ahora es utilizada en la función mover_caballo para indicar movimientos inválidos del caballo con un mensaje de error claro.

[1.16.0] - 2024-09-04
-Nueva clase InvalidMoveBishop: -Se añadió una excepción personalizada que maneja movimientos inválidos del alfil. Incluye: -Atributo position para indicar la posición no válida. -Mensaje personalizado indicando el error de movimiento. -Nueva función mover_alfil: -Implementada para gestionar el movimiento del alfil en el tablero. Incluye: -Verificación de movimientos diagonales válidos. -Lógica para mover el alfil solo si la casilla destino está vacía. -Manejo de la excepción en caso de movimiento inválido.

[1.16.0] - 2024-09-03
-Agregado: -Creación inicial de la clase PieceNotFoundException para manejar errores cuando no se encuentra una pieza en una posición específica. -Implementación del método str en PieceNotFoundException para mostrar un mensaje de error básico. -Añadida la función get_piece_at para verificar la presencia de una pieza en una posición y lanzar una excepción si no se encuentra ninguna.

[1.16.0] - 2024-09-2
-Funcionalidad: Implementación del método move para verificar si una pieza se mueve fuera de los límites del tablero.

-Descripción del Cambio:

-Comprobación de límites: Se añade una verificación para asegurarse de que las coordenadas de destino (to_row, to_col) estén dentro del rango válido del tablero (0 a 7). -Manejo de errores: Si las coordenadas están fuera de los límites del tablero, se imprime un mensaje de error en lugar de lanzar una excepción. Detalles del Código: -Verificación de coordenadas: Se usa una condición para verificar si to_row o to_col están fuera del rango de 0 a 7. -mensaje de error: En caso de que las coordenadas estén fuera del tablero, se imprime el mensaje "¡Ouch! Te saliste del tablero!" en lugar de lanzar una excepción.

[1.15.0] - 2024-09-1
-Función verificar_si_posicion_ocupada añadida:

  Se implementó una nueva función para verificar si una posición en el tablero está ocupada por una pieza del mismo color.
-Detalles: La función toma como parámetros el tablero (board), la fila y columna de destino (to_row, to_col), y la pieza que intenta moverse (pieza). Utiliza board.get_piece(to_row, to_col) para obtener la pieza en la posición de destino. Comprueba si la posición de destino está ocupada por una pieza. Si la pieza en la posición de destino es del mismo color que la pieza que intenta moverse, se imprime un mensaje de error y la función devuelve True. Si la posición de destino está vacía o está ocupada por una pieza de otro color, la función devuelve False.

-Manejo básico de errores: Se agregó un mensaje de error que se imprime cuando la posición de destino está ocupada por una pieza del mismo color

[1.14.0] - 2024-08-31
-InvalidMoveNoPiece: Añadida una excepción personalizada para indicar que un movimiento no es válido. -Constructor (init): Inicializa el mensaje de error predeterminado "Movimiento no válido". -Modificación de la Clase de Movimiento: InvalidMoveRookMove: Actualizada la implementación del método move para verificar la validez del movimiento. -Verificación de Movimiento: Se comprueba si el movimiento es válido usando self.is_valid_move(). -Manejo de Errores: Se imprime un mensaje de error si el movimiento no es válido. El código no maneja excepciones pero indica el error mediante un mensaje en la consola.

[1.13.0] - 2024-08-29
-Creación del TestKing: Se añadió la clase TestKing para probar los movimientos de la pieza del Rey. Implementación de setUp para inicializar un tablero vacío y colocar un Rey blanco en la posición (0, 4).

-Pruebas de movimientos:

Movimiento hacia abajo: Se agregó la prueba test_mover_una_casilla_hacia_abajo para verificar que el Rey se pueda mover una casilla hacia abajo.
Movimiento en diagonal: Se añadió la prueba test_mover_en_diagonal para comprobar el movimiento diagonal del Rey.
Movimiento a casilla ocupada por misma pieza: Implementación de la prueba test_colocar_otra_pieza_y_moverla para asegurar que el Rey no se mueva a una casilla ocupada por una pieza del mismo color.
Movimiento a casilla ocupada por pieza contraria: Se creó la prueba test_mover_pieza_negra para verificar que el Rey puede capturar una pieza de color contrario.
[1.12.0] - 2024-08-28
-Creación de la clase King con atributos row, col y color para representar la posición y el color del rey en el tablero. -Movimiento del Rey: Implementación del método move para permitir al Rey moverse una casilla en cualquier dirección. -Condiciones de movimiento: El Rey puede moverse horizontal, vertical o diagonalmente a una casilla adyacente. Se permite el movimiento solo si la casilla de destino está vacía o si contiene una pieza de color contrario

[1.12.0] - 2024-08-27
-Se agregó un método setUp que inicializa un tablero de ajedrez vacío y coloca una Reina blanca en la posición inicial (0, 0). -Se implementaron seis pruebas unitarias para verificar el comportamiento de la Reina: - Movimiento horizontal: Verifica que la Reina se pueda mover horizontalmente en la misma fila. - Movimiento vertical: Verifica que la Reina se pueda mover verticalmente en la misma columna. - Movimiento diagonal: Verifica que la Reina se pueda mover en diagonal. - Movimiento inválido: Verifica que la Reina no se mueva a una posición inválida. - Movimiento a casilla ocupada por la misma pieza: Verifica que la Reina no se pueda mover a una casilla ocupada por otra pieza del mismo color. - Movimiento a casilla ocupada por una pieza oponente: Verifica que la Reina pueda capturar una pieza del oponente moviéndose a su posición.

[1.12.0] - 2024-08-26
-Inicialización de la clase Queen: Se agregó el constructor init para definir la posición inicial (row, col) y el color (color) de la Reina en el tablero.

-Implementación del método move: Se añadió la lógica para permitir que la Reina se mueva horizontalmente, verticalmente y diagonalmente. Se añadió una verificación para permitir el movimiento solo si la casilla de destino está vacía o si contiene una pieza del color contrario. Se añadió la restricción para devolver False si el movimiento no es válido.

-Creación del tablero de ajedrez vacío: Se implementó la creación de un tablero de 8x8 con casillas vacías representadas por None.

-Instanciación y prueba de la Reina: Se creó una instancia de la Reina en la posición inicial (0, 0) con el color blanco. Se añadieron pruebas para mover la Reina a diferentes posiciones y verificar la validez de los movimiento

[1.11.0] - 2024-08-25
-Pruebas unitarias para la clase Knight: test_move_L_shape: Verifica movimiento en "L" válido. test_move_not_L_shape: Asegura que no se permite un movimiento inválido. test_move_to_same_color_piece: Impide moverse a una casilla ocupada por una pieza del mismo color. test_move_to_opponent_piece: Permite moverse a una casilla ocupada por una pieza del color opuesto.

[1.11.0] - 2024-08-26
-Pruebas unitarias para la clase Knight: test_move_L_shape: Verifica movimiento en "L" válido. test_move_not_L_shape: Asegura que no se permite un movimiento inválido. test_move_to_same_color_piece: Impide moverse a una casilla ocupada por una pieza del mismo color. test_move_to_opponent_piece: Permite moverse a una casilla ocupada por una pieza del color opuesto.

[1.10.0] - 2024-08-24
-Clase Knight: Implementada la clase para representar al caballo en el juego de ajedrez. init: Inicializa el caballo con una fila (start_row), una columna (start_col), y un color. move: Implementado el método para mover el caballo. Calcula la diferencia en filas y columnas para verificar movimientos en forma de "L" (2 casillas en una dirección y 1 en la otra). Verifica si la casilla destino está vacía o ocupada por una pieza del otro color. Mueve el caballo a la nueva posición si el movimiento es válido.

[1.9.0] - 2024-08-23
-Método is_valid_move: Implementado el método para verificar si un movimiento de la torre es válido. -Verificación de línea recta: La torre solo puede moverse en línea recta, ya sea vertical u horizontal. Si el movimiento no es en línea recta, se devuelve False. -Movimiento vertical:Si la columna de inicio es igual a la columna de destino, se verifica que no haya piezas en la ruta vertical entre el punto de inicio y el punto de destino. Si se encuentra alguna pieza, se devuelve False. -Movimiento horizontal:Si la fila de inicio es igual a la fila de destino, se verifica que no haya piezas en la ruta horizontal entre el punto de inicio y el punto de destino. Si se encuentra alguna pieza, se devuelve False. -Movimiento al mismo lugar: Se verifica que el punto de destino no sea el mismo que el punto de inicio. Si el punto de destino es el mismo, se devuelve False.

[1.8.0] - 2024-08-22
-Cambios en la Configuración de Importaciones -Configuración del Path: Se ha agregado código para configurar el path de importación en el archivo de pruebas import sys import os sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(file), '..'))) Esto resuelve problemas con las importaciones relativas, asegurando que los módulos y clases necesarios se importen correctamente desde el directorio padre.

-Método de Prueba: test_mover_diagonal_libre Verifica que el alfil puede moverse correctamente en diagonal a una posición libre. Se asegura de que el alfil se mueva a la posición (3, 3) y que la operación sea exitosa.

-Método de Prueba: test_mover_no_diagonal

  Verifica que el alfil no puede moverse a una posición que no está en diagonal.
  Se asegura de que el alfil permanezca en la posición original (1, 1) si el movimiento no es válido.
-Método de Prueba:test_mover_posicion_ocupada

  Verifica que el alfil no puede moverse a una posición ocupada por otra pieza.
  Se asegura de que el alfil permanezca en la posición original (1, 1) si la posición destino está ocupada.
[1.7.0] - 2024-08-21
-Agregado: -Método get_piece(row, col) para acceder a la pieza en una posición específica del tablero. -Clase de pruebas TestCli utilizando unittest y unittest.mock.patch para simular entradas y verificar el comportamiento de la función play en diferentes escenarios: -test_happy_path: Verifica un flujo exitoso donde el usuario introduce valores válidos. -test_not_happy_path: Maneja el caso donde la entrada inicial no es válida. -test_more_not_happy_path: Maneja el caso donde una entrada inválida ocurre después de algunas entradas válidas. -Clase Alfil con métodos para inicializar la posición y color de la pieza, moverla en el tablero si el movimiento es válido, y obtener la posición actual (get_row() y get_col()). -Modificado:

Método str() para generar una representación visual del tablero en forma de cadena, mostrando las piezas y celdas vacías. -Nuevo: -Implementación de una clase de prueba TestBoard utilizando unittest para verificar que el método str() del tablero produce la salida esperada en formato de cadena.
[1.6.0] - 2024-08-20
Añadido
-Funcionalidad Principal: Implementación de la clase TestPawn para realizar pruebas unitarias sobre los movimientos de la pieza de ajedrez Pawn en un tablero de ajedrez. -Nuevas Características: -Pruebas de Movimiento Adelante: Se agregó la prueba para verificar que un peón blanco y negro pueda moverse hacia adelante en el tablero. -Pruebas de Movimiento Hacia Atrás: Se agregó la prueba para asegurar que un peón blanco y negor no pueda moverse hacia atrás en el tablero. -Pruebas de Movimiento en la Misma Fila: Se agregó la prueba para confirmar que un peón no pueda moverse lateralmente en la misma fila. -Pruebas de Movimiento a una Columna Diferente: Se agregó la prueeba para validar que un peón no pueda moverse diagonalmente a una columna diferente

[1.5.0] - 2024-08-19
Añadido
-Implementada la clase Pawn (Peón) que hereda de Piece. -Métodos: -'init(self, color)': Inicializa un peón con un color específico ("WHITE" o "BLACK"). El símbolo del peón se asigna como "P" para blanco y "p" para negro. -'mover(self, tablero, start_row, start_col, to_row, to_col)': Permite mover el peón en el tablero. Las reglas de movimiento aplicadas son: El peón no puede moverse en la misma fila (start_row debe ser diferente de to_row). El peón solo puede moverse verticalmente en la misma columna (start_col debe ser igual a to_col). El peón blanco solo se mueve hacia adelante (a un número mayor de fila). El peón negro solo se mueve hacia adelante (a un número menor de fila). El peón es movido en el tablero y la posición original se libera.

[1.4.0] - 2024-08-18
Añadido
Tests de Rook: Implementación de pruebas unitarias para la clase Rook utilizando unittest.
test_rook_initialization(): Verifica que el símbolo de la torre sea correcto según su color.
test_rook_valid_move_horizontal(): Verifica que la torre pueda moverse horizontalmente en el tablero.
test_rook_valid_move_vertical(): Verifica que la torre pueda moverse verticalmente en el tablero.
test_rook_invalid_move(): Verifica que la torre no pueda moverse a una posición inválida.
[1.3.0] - 2024-08-18
Añadido
Chess: Implementación de la clase Chess que maneja la lógica del juego de ajedrez, incluyendo el tablero y el turno de los jugadores.

move(): Método que permite mover piezas en el tablero y cambia el turno después de cada movimiento.
change_turn(): Método para alternar el turno entre los jugadores.
turn: Propiedad que retorna el turno actual del jugador.
Interfaz de Juego: Función main() y play() para interactuar con el juego a través de la consola.

play(): Función que maneja la interacción con el usuario, permitiendo realizar movimientos y mostrar el turno actual.
[1.2.0] - 2024-08-18
Añadido
Board: Implementación de la clase Board que maneja la posición de las piezas en el tablero de ajedrez.

Rook Inicial: Colocación de las torres (Rook) en sus posiciones iniciales en el tablero.
get_piece(): Método que devuelve la pieza en una posición específica del tablero.
Interfaz Gráfica con Pygame: Implementación inicial de la interfaz gráfica para visualizar el tablero de ajedrez usando Pygame.

**Dibujo del Tabler


## [1.21.0] - 2024-09-13

-**Refactorización de Test_Move**:

-**Cambio**: Se actualizó el método Test_Move para simplificar la prueba de movimientos de la pieza.
-**Acción**: Ahora se pasa la posición inicial de la pieza (fila y columna) directamente al método en lugar de obtenerla dentro de Test_Move.
-**Resultado**: Esta modificación facilita la verificación del movimiento de la pieza, asegurando que se coloque correctamente en la nueva posición o permanezca en la original según el resultado esperado.
Nuevo Método get_piece_position:

Cambio: Se introdujo un nuevo método para obtener la posición de una pieza en el tablero.
Acción: Este método recorre el tablero para encontrar y retornar las coordenadas de la pieza especificada.
Resultado: Permite obtener fácilmente la posición actual de cualquier pieza en el tablero, facilitando la gestión de movimientos en las pruebas.

## [1.21.0] - 2024-09-12

Se creó el método auxiliar assert_king_position(row, col, result) para eliminar la duplicación de código en la validación de la posición del rey después de cada movimiento.
-**Mejoras**: Se reemplazaron las verificaciones individuales de la posición del rey en los tests (test_mover_una_casilla_hacia_abajo, test_mover_en_diagonal, etc.) con llamadas al nuevo método assert_king_position, haciendo el código más limpio y reutilizable.
-**Metodos**: Se eliminó la repetición de las sentencias assertEqual para validar las posiciones del rey en múltiples pruebas, centralizando la lógica de validación.
-**Mantenibilidad**: Ahora, cualquier cambio en la forma de verificar la posición del rey solo necesita realizarse en un único lugar (assert_king_position), simplificando futuras modificaciones.

## [1.21.0] - 2024-09-11

-**Cambios Realizados**:

-**Refactorización**: Se ha creado el método Test_Move para consolidar la lógica de prueba repetida en un solo lugar.
-**Código Anterior**: Los métodos de prueba (test_mover_torre_vertical, test_mover_torre_horizontal, etc.) contenían bloques de código repetitivos para colocar la pieza, realizar el movimiento y verificar el resultado.
-**Código Nuevo**: Los métodos de prueba utilizan Test_Move para realizar estas tareas de manera más concisa y evitar la duplicación de código.
Verificación del Movimiento:
-**Código Anterior**: Cada método verificaba el movimiento, la posición inicial, y la posición final directamente en el mismo método.
-**Código Nuevo**: La verificación se realiza en el método Test_Move, simplificando los métodos de prueba individuales.



## [1.21.0] - 2024-09-10

-**Introducción de movimiento_valido**: 
      -Se creó la variable movimiento_valido al inicio de la función, inicializándola en True. Esta variable se usa para determinar si el movimiento es válido o no.
      -Anteriormente, el código contenía múltiples return para salir de la función en cada caso en que el movimiento no era válido. Ahora,  movimiento_valido se actualiza en cada verificaciónn.

-**Eliminación de múltiples return**: 
      Ahora solo hay un único return al final, que devuelve el valor de movimiento_valido.

-**Flujo más claro**: 
      Todas las verificaciones se realizan antes de decidir si el movimiento es válido, haciendo el código más legible sin cambiar la lógica.

## [1.20.0] - 2024-09-08

-**Agregando funcion es is_valid_diagonal_move**:

-**Descripción**
-Constructor de la clase InvalidMoveBishop ahora guarda la posición del error y un mensaje personalizado que incluye la posición en la que ocurre el error.
-Se sobreescribió el método __str__ en InvalidMoveBishop para proporcionar un mensaje de error más claro cuando se muestra la excepción.
-Se incluyó la función is_valid_diagonal_move dentro de la clase InvalidMoveBishop para verificar si un movimiento diagonal es válido en un tablero de ajedrez:
      -Verifica que el movimiento sea diagonal al comparar las diferencias absolutas entre las filas y columnas.
      -Lanza una excepción InvalidMoveDiagonal si el movimiento no es diagonal.
      -Verifica si la casilla de destino está ocupada, lanzando una excepción si es así.

## [1.19.0] - 2024-09-07

-**Refactorización de la Función move en la Clase Piece**

-**Descripción**: La función move en la clase Piece ha sido refactorizada para ajustar el número de argumentos, cumpliendo así con el límite permitido de cinco argumentos.

-**Problema Original**: La función move original tenía seis argumentos (self, start_row, start_col, to_row, to_col, board), lo que excedía el límite de cinco argumentos permitidos por las reglas de diseño.

-**Solución**: Se ha simplificado la función para utilizar dos objetos Position que encapsulan la información de las posiciones de inicio y destino. Esto permite que la función move acepte sólo cinco argumentos en total, reduciendo la complejidad y cumpliendo con las restricciones.

## [1.18.0] - 2024-09-06

-**Descripción del Cambio**: 
      Se realizó una refactorización en la función is_valid_move para reducir su complejidad cognitiva. La versión anterior tenía una complejidad cognitiva de 20, lo que supera el límite recomendado de 15. La refactorización incluye la simplificación de las verificaciones de movimiento horizontal y vertical, así como la mejora en la legibilidad del código.

-**Cambios Realizados Refactorización de is_valid_move:**
      -Motivo: Reducir la complejidad cognitiva de la función que originalmente supera el límite recomendado.
      -Acción: Simplificación de la lógica de validación de movimientos horizontales y verticales.

## [1.17.0] - 2024-09-05

-**Corrección de Acceso a Atributos Privados**:
      Se reemplazó el acceso directo a los atributos privados __row__ y __col__ de la clase Caballo con métodos getter y setter (get_row(), get_col(), set_row(row), set_col(col)) para seguir las buenas prácticas de encapsulamiento en Python.

-**Actualización de la Función mover_caballo**:
      Modificada la función para utilizar métodos getter y setter en lugar de acceder directamente a los atributos privados.
      Añadido manejo de la excepción InvalidMoveKnight cuando el movimiento no es válido para el caballo.
      La función verifica si la casilla destino está vacía antes de mover el caballo y retorna True si el movimiento es exitoso y False si la casilla está ocupada.

-**Definición de Excepción**:
      Se ha incluido la definición de la excepción InvalidMoveKnight, que ahora es utilizada en la función mover_caballo para indicar movimientos inválidos del caballo con un mensaje de error claro.

## [1.16.0] - 2024-09-04

-**Nueva clase InvalidMoveBishop**: 
    -Se añadió una excepción personalizada que maneja movimientos inválidos del alfil. Incluye:
    -Atributo position para indicar la posición no válida.
    -Mensaje personalizado indicando el error de movimiento.
-**Nueva función mover_alfil**: 
    -Implementada para gestionar el movimiento del alfil en el tablero. Incluye:
    -Verificación de movimientos diagonales válidos.
    -Lógica para mover el alfil solo si la casilla destino está vacía.
    -Manejo de la excepción en caso de movimiento inválido.

## [1.16.0] - 2024-09-03

-**Agregado**:
      -Creación inicial de la clase PieceNotFoundException para manejar errores cuando no se encuentra una pieza en una posición específica.
      -Implementación del método __str__ en PieceNotFoundException para mostrar un mensaje de error básico.
      -Añadida la función get_piece_at para verificar la presencia de una pieza en una posición y lanzar una excepción si no se encuentra ninguna.


## [1.16.0] - 2024-09-2

-**Funcionalidad**: Implementación del método move para verificar si una pieza se mueve fuera de los límites del tablero.

-**Descripción del Cambio**:

  -**Comprobación de límites**: Se añade una verificación para asegurarse de que las coordenadas de destino (to_row, to_col) estén dentro del rango válido del tablero (0 a 7).
  -**Manejo de errores**: Si las coordenadas están fuera de los límites del tablero, se imprime un mensaje de error en lugar de lanzar una excepción.
      Detalles del Código:
  -**Verificación de coordenadas**: Se usa una condición para verificar si to_row o to_col están fuera del rango de 0 a 7.
  -**mensaje de error**: En caso de que las coordenadas estén fuera del tablero, se imprime el mensaje "¡Ouch! Te saliste del tablero!" en lugar de lanzar una excepción.

## [1.15.0] - 2024-09-1

-**Función verificar_si_posicion_ocupada añadida**:
      
      Se implementó una nueva función para verificar si una posición en el tablero está ocupada por una pieza del mismo color.

-**Detalles**:
    La función toma como parámetros el tablero (board), la fila y columna de destino (to_row, to_col), y la pieza que intenta moverse (pieza).
    Utiliza board.get_piece(to_row, to_col) para obtener la pieza en la posición de destino.
    Comprueba si la posición de destino está ocupada por una pieza.
    Si la pieza en la posición de destino es del mismo color que la pieza que intenta moverse, se imprime un mensaje de error y la función devuelve True.
    Si la posición de destino está vacía o está ocupada por una pieza de otro color, la función devuelve False.

-**Manejo básico de errores**:
    Se agregó un mensaje de error que se imprime cuando la posición de destino está ocupada por una pieza del mismo color

## [1.14.0] - 2024-08-31

-**InvalidMoveNoPiece**:
   Añadida una excepción personalizada para indicar que un movimiento no es válido.
-**Constructor (__init__)**: 
   Inicializa el mensaje de error predeterminado "Movimiento no válido".
-**Modificación de la Clase de Movimiento**:
    InvalidMoveRookMove: Actualizada la implementación del método move para verificar la validez del movimiento.
-**Verificación de Movimiento**: Se comprueba si el movimiento es válido usando self.is_valid_move().
-**Manejo de Errores**: Se imprime un mensaje de error si el movimiento no es válido. El código no maneja excepciones pero indica el error mediante un mensaje en la consola.



## [1.13.0] - 2024-08-29

-**Creación del TestKing**:
    Se añadió la clase TestKing para probar los movimientos de la pieza del Rey.
    Implementación de setUp para inicializar un tablero vacío y colocar un Rey blanco en la posición (0, 4).

-**Pruebas de movimientos**:

  -  **Movimiento hacia abajo**: Se agregó la prueba test_mover_una_casilla_hacia_abajo para verificar que el Rey se pueda mover una casilla hacia abajo.
  -  **Movimiento en diagonal**: Se añadió la prueba test_mover_en_diagonal para comprobar el movimiento diagonal del Rey.
  -  **Movimiento a casilla ocupada por misma pieza**: Implementación de la prueba test_colocar_otra_pieza_y_moverla para asegurar que el Rey no se mueva a una casilla ocupada por una pieza del mismo color.
  -  **Movimiento a casilla ocupada por pieza contraria**: Se creó la prueba test_mover_pieza_negra para verificar que el Rey puede capturar una pieza de color contrario.

## [1.12.0] - 2024-08-28

-Creación de la clase King con atributos __row__, __col__ y __color__ para representar la posición y el color del rey en el tablero.
-**Movimiento del Rey**:
    Implementación del método move para permitir al Rey moverse una casilla en cualquier dirección.
-**Condiciones de movimiento**:
    El Rey puede moverse horizontal, vertical o diagonalmente a una casilla adyacente.
    Se permite el movimiento solo si la casilla de destino está vacía o si contiene una pieza de color contrario

## [1.12.0] - 2024-08-27

-Se agregó un método setUp que inicializa un tablero de ajedrez vacío y coloca una Reina blanca en la posición inicial (0, 0).
-**Se implementaron seis pruebas unitarias para verificar el comportamiento de la Reina**:
      -  **Movimiento horizontal**: Verifica que la Reina se pueda mover horizontalmente en la misma fila.
      -  **Movimiento vertical**: Verifica que la Reina se pueda mover verticalmente en la misma columna.
      -  **Movimiento diagonal**: Verifica que la Reina se pueda mover en diagonal.
      -  **Movimiento inválido**: Verifica que la Reina no se mueva a una posición inválida.
      -  **Movimiento a casilla ocupada por la misma pieza**: Verifica que la Reina no se pueda mover a una casilla ocupada por otra pieza del mismo color.
      -  **Movimiento a casilla ocupada por una pieza oponente**: Verifica que la Reina pueda capturar una pieza del oponente moviéndose a su posición.



## [1.12.0] - 2024-08-26

-**Inicialización de la clase Queen**:
        Se agregó el constructor __init__ para definir la posición inicial (row, col) y el color (color) de la Reina en el tablero.

-**Implementación del método move**:
        Se añadió la lógica para permitir que la Reina se mueva horizontalmente, verticalmente y diagonalmente.
        Se añadió una verificación para permitir el movimiento solo si la casilla de destino está vacía o si contiene una pieza del color contrario.
        Se añadió la restricción para devolver False si el movimiento no es válido.

-**Creación del tablero de ajedrez vacío**:
      Se implementó la creación de un tablero de 8x8 con casillas vacías representadas por None.

-**Instanciación y prueba de la Reina**:
      Se creó una instancia de la Reina en la posición inicial (0, 0) con el color blanco.
      Se añadieron pruebas para mover la Reina a diferentes posiciones y verificar la validez de los movimiento

## [1.11.0] - 2024-08-25

-**Pruebas unitarias para la clase Knight**: test_move_L_shape: Verifica movimiento en "L" válido. test_move_not_L_shape: Asegura que no se permite un movimiento inválido. test_move_to_same_color_piece: Impide moverse a una casilla ocupada por una pieza del mismo color. test_move_to_opponent_piece: Permite moverse a una casilla ocupada por una pieza del color opuesto.
## [1.11.0] - 2024-08-26

-**Pruebas unitarias para la clase Knight**:
      test_move_L_shape: Verifica movimiento en "L" válido.
      test_move_not_L_shape: Asegura que no se permite un movimiento inválido.
      test_move_to_same_color_piece: Impide moverse a una casilla ocupada por una pieza del mismo color.
      test_move_to_opponent_piece: Permite moverse a una casilla ocupada por una pieza del color opuesto.

## [1.10.0] - 2024-08-24

-**Clase Knight**: Implementada la clase para representar al caballo en el juego de ajedrez.
      __init__: Inicializa el caballo con una fila (start_row), una columna (start_col), y un color.
      move: Implementado el método para mover el caballo.
      Calcula la diferencia en filas y columnas para verificar movimientos en forma de "L" (2 casillas en una dirección y 1 en la otra).
      Verifica si la casilla destino está vacía o ocupada por una pieza del otro color.
      Mueve el caballo a la nueva posición si el movimiento es válido.

## [1.9.0] - 2024-08-23

-**Método is_valid_move**: Implementado el método para verificar si un movimiento de la torre es válido.
      -**Verificación de línea recta**: La torre solo puede moverse en línea recta, ya sea vertical u horizontal. Si el movimiento no es en línea recta, se devuelve False.
      -**Movimiento vertical**:Si la columna de inicio es igual a la columna de destino, se verifica que no haya piezas en la ruta vertical entre el punto de inicio y el punto de destino. Si se encuentra alguna pieza, se devuelve False.
      -**Movimiento horizontal**:Si la fila de inicio es igual a la fila de destino, se verifica que no haya piezas en la ruta horizontal entre el punto de inicio y el punto de destino. Si se encuentra alguna pieza, se devuelve False.
      -**Movimiento al mismo lugar**: Se verifica que el punto de destino no sea el mismo que el punto de inicio. Si el punto de destino es el mismo, se devuelve False.


## [1.8.0] - 2024-08-22

-**Cambios en la Configuración de Importaciones**
  -**Configuración del Path**: 
    Se ha agregado código para configurar el path de importación en el archivo de pruebas 
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    Esto resuelve problemas con las importaciones relativas, asegurando que los módulos y clases necesarios se importen correctamente desde el directorio padre.


-**Método de Prueba**: test_mover_diagonal_libre
      Verifica que el alfil puede moverse correctamente en diagonal a una posición libre.
      Se asegura de que el alfil se mueva a la posición (3, 3) y que la operación sea exitosa.

-**Método de Prueba**: test_mover_no_diagonal

      Verifica que el alfil no puede moverse a una posición que no está en diagonal.
      Se asegura de que el alfil permanezca en la posición original (1, 1) si el movimiento no es válido.

-**Método de Prueba**:test_mover_posicion_ocupada

      Verifica que el alfil no puede moverse a una posición ocupada por otra pieza.
      Se asegura de que el alfil permanezca en la posición original (1, 1) si la posición destino está ocupada.


## [1.7.0] - 2024-08-21
-**Agregado**: 
  -Método get_piece(row, col) para acceder a la pieza en una posición específica del tablero.
  -Clase de pruebas TestCli utilizando unittest y unittest.mock.patch para simular entradas y verificar el comportamiento de la función play en diferentes escenarios:
        -test_happy_path: Verifica un flujo exitoso donde el usuario introduce valores válidos.
        -test_not_happy_path: Maneja el caso donde la entrada inicial no es válida.
        -test_more_not_happy_path: Maneja el caso donde una entrada inválida ocurre después de algunas entradas válidas.
  -Clase Alfil con métodos para inicializar la posición y color de la pieza, moverla en el tablero si el movimiento es válido, y obtener la posición actual (get_row() y get_col()).
-**Modificado**:
  - Método __str__() para generar una representación visual del tablero en forma de cadena, mostrando las piezas y celdas vacías.
-**Nuevo**: 
  -Implementación de una clase de prueba TestBoard utilizando unittest para verificar que el método __str__() del tablero produce la salida esperada en formato de cadena.

## [1.6.0] - 2024-08-20
### Añadido 
-**Funcionalidad Principal**:
    Implementación de la clase TestPawn para realizar pruebas unitarias sobre los movimientos 
    de la pieza de ajedrez Pawn en un tablero de ajedrez.
-**Nuevas Características**:
  -**Pruebas de Movimiento Adelante**:
    Se agregó la prueba para verificar que un peón blanco y negro pueda moverse hacia adelante en el tablero.
-**Pruebas de Movimiento Hacia Atrás**:
    Se agregó la prueba para asegurar que un peón blanco y negor no pueda moverse hacia atrás en el tablero.
-**Pruebas de Movimiento en la Misma Fila**:
    Se agregó la prueba para confirmar que un peón no pueda moverse lateralmente en la misma fila.
-**Pruebas de Movimiento a una Columna Diferente**:
    Se agregó la prueeba para validar que un peón no pueda moverse diagonalmente a una columna diferente

## [1.5.0] - 2024-08-19

### Añadido
-**Implementada la clase Pawn (Peón) que hereda de Piece**.
  -**Métodos**:
      -**'__init__(self, color)'**: Inicializa un peón con un color específico ("WHITE" o "BLACK"). El símbolo del peón se asigna como "P" para blanco y "p" para negro.
      -**'mover(self, tablero, start_row, start_col, to_row, to_col)'**: Permite mover el peón en el tablero. Las reglas de movimiento aplicadas son:
        El peón no puede moverse en la misma fila (start_row debe ser diferente de to_row).
        El peón solo puede moverse verticalmente en la misma columna (start_col debe ser igual a to_col). 
        El peón blanco solo se mueve hacia adelante (a un número mayor de fila).
        El peón negro solo se mueve hacia adelante (a un número menor de fila).
        El peón es movido en el tablero y la posición original se libera.

## [1.4.0] - 2024-08-18

### Añadido
- **Tests de `Rook`**: Implementación de pruebas unitarias para la clase `Rook` utilizando `unittest`.
  - **`test_rook_initialization()`**: Verifica que el símbolo de la torre sea correcto según su color.
  - **`test_rook_valid_move_horizontal()`**: Verifica que la torre pueda moverse horizontalmente en el tablero.
  - **`test_rook_valid_move_vertical()`**: Verifica que la torre pueda moverse verticalmente en el tablero.
  - **`test_rook_invalid_move()`**: Verifica que la torre no pueda moverse a una posición inválida.

## [1.3.0] - 2024-08-18

### Añadido
- **`Chess`**: Implementación de la clase `Chess` que maneja la lógica del juego de ajedrez, incluyendo el tablero y el turno de los jugadores.
  - **`move()`**: Método que permite mover piezas en el tablero y cambia el turno después de cada movimiento.
  - **`change_turn()`**: Método para alternar el turno entre los jugadores.
  - **`turn`**: Propiedad que retorna el turno actual del jugador.

- **Interfaz de Juego**: Función `main()` y `play()` para interactuar con el juego a través de la consola.
  - **`play()`**: Función que maneja la interacción con el usuario, permitiendo realizar movimientos y mostrar el turno actual.

## [1.2.0] - 2024-08-18

### Añadido
- **`Board`**: Implementación de la clase `Board` que maneja la posición de las piezas en el tablero de ajedrez.
  - **Rook Inicial**: Colocación de las torres (`Rook`) en sus posiciones iniciales en el tablero.
  - **`get_piece()`**: Método que devuelve la pieza en una posición específica del tablero.
  
- **Interfaz Gráfica con Pygame**: Implementación inicial de la interfaz gráfica para visualizar el tablero de ajedrez usando Pygame.
  - **Dibujo del Tabler


