from collections import deque

class Jogovelha:
    def __init__(self):

        # Inicializa o tabuleiro vazio
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

        # Define o jogador atual como 'X'
        self.jogador = 'X'

    # Função para imprimir o tabuleiro
    def print_tabuleiro(self):

        for row in self.tabuleiro:
            print('|'.join(row))
            print('-' * 5)

    # Verifica se o jogador passado como parâmetro venceu o jogo
    def ganhador(self, jogador):
      
    # Verifica todas as linhas
        for row in self.tabuleiro:
            if all(cell == jogador for cell in row):
                return True
            
    # Verifica todas as colunas
        for col in range(3):
            if all(self.tabuleiro[row][col] == jogador for row in range(3)):
                return True
            
    # Verifica diagonais
        if all(self.tabuleiro[i][i] == jogador for i in range(3)) or all(
            self.tabuleiro[i][2 - i] == jogador for i in range(3)
        ):
            return True
        return False
    
    # Verifica se o jogo terminou em empate
    def empate(self):
        print("Deu Velha")
        return all(cell != ' ' for row in self.tabuleiro for cell in row)
        
    # Verifica se o jogo acabou
    def fim_jogo(self):
        return self.ganhador('X') or self.ganhador('O') or self.empate()

    # Retorna todos os movimentos válidos disponíveis no tabuleiro
    def movimentos_validos(self):
        moves = []
        for row in range(3):
            for col in range(3):
                if self.tabuleiro[row][col] == ' ':
                    moves.append((row, col))
        return moves
    
    # Realiza um movimento na posição especificada pelo jogador atual
    def jogadas(self, row, col):
        
        if self.tabuleiro[row][col] == ' ':
            self.tabuleiro[row][col] = self.jogador
            
            # Alterna o jogador atual
            self.jogador = 'O' if self.jogador == 'X' else 'X'
            return True
        return False
    
    # Implementação da busca em largura
    def bfs(self):
       
        # Inicializa uma fila com o estado inicial do jogo (tabuleiro vazio e jogador 'X')
        queue = deque([(self.tabuleiro, self.jogador)])
        while queue:

            # Retira o primeiro estado da fila
            tabuleiro, jogador = queue.popleft()

            # Cria uma instância do jogo com o estado retirado da fila
            game = Jogovelha()
            game.tabuleiro = tabuleiro
            game.jogador = jogador

            # Verifica se o jogo acabou
            if game.fim_jogo():

                # Se o jogo terminou, imprime o tabuleiro e o jogador vencedor
                game.print_tabuleiro()
                print("BFS - Ganhou:", jogador)
                return
            
            # Se o jogo não terminou, gera todos os possíveis movimentos a partir do estado atual
            for move in game.movimentos_validos():

                # Cria uma cópia do tabuleiro atual
                new_tabuleiro = [row[:] for row in game.tabuleiro]

                # Realiza o movimento no novo tabuleiro
                new_tabuleiro[move[0]][move[1]] = jogador

                # Alterna o jogador para o próximo movimento
                new_jogador = 'O' if jogador == 'X' else 'X'

                # Adiciona o novo estado na fila para ser explorado posteriormente
                queue.append((new_tabuleiro, new_jogador))

    # Implementação da busca em profundidade
    def dfs(self, tabuleiro=None, jogador=None):
        
        if tabuleiro is None:
            # Se não foi especificado um tabuleiro inicial, usa o tabuleiro atual do jogo
            tabuleiro = self.tabuleiro
            jogador = self.jogador

        # Cria uma instância do jogo com o estado atual
        game = Jogovelha()
        game.tabuleiro = tabuleiro
        game.jogador = jogador

        # Verifica se o jogo acabou
        if game.fim_jogo():
            # Se o jogo terminou, imprime o tabuleiro e o jogador vencedor
            game.print_tabuleiro()
            print("DFS - Ganhou:", jogador)
            return

        # Se o jogo não terminou, gera todos os possíveis movimentos a partir do estado atual
        for move in game.movimentos_validos():
            # Cria uma cópia do tabuleiro atual
            new_tabuleiro = [row[:] for row in game.tabuleiro]

            # Realiza o movimento no novo tabuleiro
            new_tabuleiro[move[0]][move[1]] = jogador

            # Alterna o jogador para o próximo movimento
            new_jogador = 'O' if jogador == 'X' else 'X'

            # Chama recursivamente a função DFS com o novo estado
            game.dfs(new_tabuleiro, new_jogador)

# Instancia um jogo da velha
game = Jogovelha()

# Imprime o tabuleiro inicial
game.print_tabuleiro()

# Executa a busca em largura
game.bfs()

# Executa a busca em profundidade
game.dfs()

    # Edson Fernando Araujo Silva - 202308674099