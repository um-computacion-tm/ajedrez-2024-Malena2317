# Changelog

Todos los cambios importantes en este proyecto serán documentados en este archivo.



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


