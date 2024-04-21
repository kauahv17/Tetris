import pygame

preto = (0, 0, 0)
amarelo = (237, 234, 4)
amarelo = (237, 234, 4)
laranja = (226, 116, 27)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
roxo = (84, 22, 180)
rosa = (228, 0, 224)

class Posicao:
    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

class Blocos:
    def __init__(self, id):
        self.id = id
        self.mover_linha = 0
        self.mover_coluna = 0
        self.sentido = 0
        self.celulas = {}
        self.size_cell = 40
        self.cores = [preto, amarelo, laranja, vermelho, azul, verde, roxo, rosa]

    def mover(self, linhas, colunas):
        self.mover_linha += linhas
        self.mover_coluna += colunas

    def pegar_posicao_cell(self):
        cubos = self.celulas[self.sentido]
        mover_cubos = []
        for pos in cubos:
            pos = Posicao(pos.linha + self.mover_linha, pos.coluna + self.mover_coluna)
            mover_cubos.append(pos)

        return mover_cubos

    def desenhar(self, tela, desvio_x, desvio_y):
        cubos = self.pegar_posicao_cell()
        for cubo in cubos:
            cubo_rect = pygame.Rect(desvio_x + cubo.coluna * self.size_cell, 
                                    desvio_y + cubo.linha * self.size_cell, self.size_cell - 1, self.size_cell - 1)
            pygame.draw.rect(tela, self.cores[self.id], cubo_rect)


    def rotacionar(self):
        self.sentido += 1
        if self.sentido == len(self.celulas):
            self.sentido = 0

    def desfazer_rotacao(self):
        self.sentido += 1
        if self.sentido == 0:
            self.sentido = len(self.celulas) - 1

    

class Bloco_T(Blocos):
    def __init__(self):
        super().__init__(id = 1)
        self.celulas = {
            0: [Posicao(0,1), Posicao(1,0), Posicao(1,1), Posicao(1,2)],
            1: [Posicao(0,1), Posicao(1,1), Posicao(1,2), Posicao(2,1)],
            2: [Posicao(1,0), Posicao(1,1), Posicao(1,2), Posicao(2,1)],
            3: [Posicao(0,1), Posicao(1,0), Posicao(1,1), Posicao(2,1)]
        }
        self.mover(0, 3)


class Bloco_L(Blocos):
    def __init__(self):
        super().__init__(id = 2)
        self.celulas = {
            0: [Posicao(0,2), Posicao(1,0), Posicao(1,1), Posicao(1,2)],
            1: [Posicao(0,1), Posicao(1,1), Posicao(2,1), Posicao(2,2)],
            2: [Posicao(1,0), Posicao(1,1), Posicao(1,2), Posicao(2,0)],
            3: [Posicao(0,0), Posicao(0,1), Posicao(1,1), Posicao(2,1)]
        }
        self.mover(0, 3)

class Bloco_J(Blocos):
    def __init__(self):
        super().__init__(id = 3)
        self.celulas = {
            0: [Posicao(0,0), Posicao(1,0), Posicao(1,1), Posicao(1,2)],
            1: [Posicao(0,1), Posicao(0,2), Posicao(1,1), Posicao(2,1)],
            2: [Posicao(1,0), Posicao(1,1), Posicao(1,2), Posicao(2,2)],
            3: [Posicao(0,1), Posicao(1,1), Posicao(2,0), Posicao(2,1)]
        }
        self.mover(0, 3)

class Bloco_I(Blocos):
    def __init__(self):
        super().__init__(id = 4)
        self.celulas = {
            0: [Posicao(1,0), Posicao(1,1), Posicao(1,2), Posicao(1,3)],
            1: [Posicao(0,2), Posicao(1,2), Posicao(2,2), Posicao(3,2)],
            2: [Posicao(2,0), Posicao(2,1), Posicao(2,2), Posicao(2,3)],
            3: [Posicao(0,1), Posicao(1,1), Posicao(2,1), Posicao(3,1)]
        }
        self.mover(0, 3)

class Bloco_O(Blocos):
    def __init__(self):
        super().__init__(id = 5)
        self.celulas = {
            0: [Posicao(0,0), Posicao(0,1), Posicao(1,0), Posicao(1,1)],
            1: [Posicao(0,0), Posicao(0,1), Posicao(1,0), Posicao(1,1)],
            2: [Posicao(0,0), Posicao(0,1), Posicao(1,0), Posicao(1,1)],
            3: [Posicao(0,0), Posicao(0,1), Posicao(1,0), Posicao(1,1)]
        }
        self.mover(0, 3)

class Bloco_S(Blocos):
    def __init__(self):
        super().__init__(id = 6)
        self.celulas = {
            0: [Posicao(0,1), Posicao(0,2), Posicao(1,0), Posicao(1,1)],
            1: [Posicao(0,1), Posicao(1,1), Posicao(1,2), Posicao(2,2)],
            2: [Posicao(1,1), Posicao(1,2), Posicao(2,0), Posicao(2,1)],
            3: [Posicao(0,0), Posicao(1,0), Posicao(1,1), Posicao(2,1)]
        }
        self.mover(0, 3)


class Bloco_Z(Blocos):
    def __init__(self):
        super().__init__(id = 7)
        self.celulas = {
            0: [Posicao(0,0), Posicao(0,1), Posicao(1,1), Posicao(1,2)],
            1: [Posicao(0,2), Posicao(1,1), Posicao(1,2), Posicao(2,1)],
            2: [Posicao(1,0), Posicao(1,1), Posicao(2,1), Posicao(2,2)],
            3: [Posicao(0,1), Posicao(1,0), Posicao(1,1), Posicao(2,0)]
        }
        self.mover(0, 3)