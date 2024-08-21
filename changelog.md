# Changelog

Todos los cambios importantes en este proyecto serán documentados en este archivo.


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


