from  tablero.board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"# Empieza el turno con el jugador blanco
        self.game_over = False  # Indica si el juego ha terminado

    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        # validate coords
        piece = self.__board__.get_piece(from_row, from_col)
        self.change_turn()
    @property
    def play_turn(self):
        
    if self.game_over:  # Si el juego ha terminado, no se puede jugar
                return False
            self.board.print_board()  # Muestra el tablero
            print("Es el turno de " + self.current_turn)  # Indica de quién es el turno

            origin = input("Ingrese la posición de origen (Ej: D2) o 'q' para rendirse: ")
            if origin.lower() == 'q':
                print("El jugador " + self.current_turn + " se ha rendido.")
                self.game_over = True
                return False

            destination = input("Ingrese la posición de destino (Ej: D3): ")


    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK" # Cambia a negro
        else:
            self.__turn__ = "WHITE"  # Cambia a blanco