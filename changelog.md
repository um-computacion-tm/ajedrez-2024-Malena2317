# Changelog

Todos los cambios importantes en este proyecto serán documentados en este archivo.
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


