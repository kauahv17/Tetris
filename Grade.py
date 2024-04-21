import pygame

class GRADE:
    def __init__(self):
        self.N_linhas = 20
        self.N_colunas = 10
        self.size_cell = 40
        self.grade = [[0 for i in range(self.N_colunas) ]for j in range(self.N_linhas)]
        self.cores = self.lista_cores()

    def exibir(self):
        for i in range(self.N_linhas):
            for j in range(self.N_colunas):
                print(self.grade[i][j], end=" ")
            print("")


    def dentro_da_grade(self, linha, coluna):
        if linha >= 0 and linha < self.N_linhas and coluna >= 0 and coluna < self.N_colunas:
            return True
        
        return False
    
    def esta_vazio(self, linha, coluna):
        if self.grade[linha][coluna] == 0:
            return True
        
        return False
    
    def linha_cheia(self, linha):
        for coluna in range(self.N_colunas):
            if self.grade[linha][coluna] == 0:
                return False
        return True
    
    def limpar_linha(self, linha):
        for coluna in range(self.N_colunas):
            self.grade[linha][coluna] = 0

    def descer_linhas(self, linha, num_linhas):
        for coluna in range(self.N_colunas):
            self.grade[linha+num_linhas][coluna] = self.grade[linha][coluna]
            self.grade[linha][coluna] = 0

    def limpar_todas_linhas(self):
        completa = 0
        for linha in range(self.N_linhas-1, 0, -1):
            if self.linha_cheia(linha):
                self.limpar_linha(linha)
                completa += 1

            elif completa > 0:
                self.descer_linhas(linha, completa)

        return completa


    def lista_cores(self):
        preto = (0, 0, 0)
        amarelo = (237, 234, 4)
        laranja = (226, 116, 27)
        vermelho = (255, 0, 0)
        azul = (0, 0, 255)
        verde = (0, 255, 0)
        roxo = (84, 22, 180)
        rosa = (228, 0, 224)


        return [preto, amarelo, laranja, vermelho, azul, verde, roxo, rosa]
    
    def desenhar(self, tela):
        for i in range(self.N_linhas):
            for j in range(self.N_colunas):
                valor_cell = self.grade[i][j]
                cell_rect = pygame.Rect(j * self.size_cell + 31, i * self.size_cell + 111, self.size_cell - 1, self.size_cell - 1)
                pygame.draw.rect(tela, self.cores[valor_cell], cell_rect)

    def reiniciar(self):
        for linha in range(self.N_linhas):
            for coluna in range(self.N_colunas):
                self.grade[linha][coluna] = 0