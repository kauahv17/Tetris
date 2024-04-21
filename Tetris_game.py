import random
from Tetris import *
from Grade import GRADE
from pygame.locals import *
import pygame,sys


pygame.display.set_caption("Tetris")
tela = pygame.display.set_mode((580, 940))

class JOGO:
    def __init__(self):
        self.Grade = GRADE()
        self.blocos = [Bloco_T(), Bloco_L(), Bloco_J(), Bloco_I(), Bloco_O(), Bloco_S(), Bloco_Z()]
        self.bloco_atual = self.escolher_bloco()
        self.proximo_bloco = self.escolher_bloco()
        self.derrota = False
        self.pontuacao = 0


    def atualizar_score(self, linhas_limpadas, pontos_movimento):
        self.pontuacao += linhas_limpadas * 100
        self.pontuacao += pontos_movimento



    def mover_direita(self):
        self.bloco_atual.mover(0, 1)
        if self.bloco_dentro() == False or self.encaixar_blocos() == False:
            self.bloco_atual.mover(0, -1)

    def mover_esquerda(self):
        self.bloco_atual.mover(0, -1)
        if self.bloco_dentro() == False or self.encaixar_blocos() == False:
            self.bloco_atual.mover(0, 1)

    def mover_baixo(self):
        self.bloco_atual.mover(1, 0)
        if self.bloco_dentro() == False or self.encaixar_blocos() == False:
            self.bloco_atual.mover(-1, 0)
            self.travar_bloco()


    def encaixar_blocos(self):
        cubos = self.bloco_atual.pegar_posicao_cell()

        for cubo in cubos:
            if self.Grade.esta_vazio(cubo.linha,cubo.coluna) == False:
                return False

        return True


    def travar_bloco(self):
        cubos = self.bloco_atual.pegar_posicao_cell()

        for pos in cubos:
            self.Grade.grade[pos.linha][pos.coluna] = self.bloco_atual.id
                
        self.bloco_atual = self.proximo_bloco
        self.proximo_bloco = self.escolher_bloco()
        linhas_limpadas = self.Grade.limpar_todas_linhas()
        self.atualizar_score(linhas_limpadas, 0)
        if self.encaixar_blocos() == False:
            self.derrota = True



    def rotacionar(self):
        self.bloco_atual.rotacionar()
        if self.bloco_dentro() == False:
            self.bloco_atual.desfazer_rotacao()


    def bloco_dentro(self):
        cubos = self.bloco_atual.pegar_posicao_cell()

        for cubo in cubos:
            if self.Grade.dentro_da_grade(cubo.linha, cubo.coluna) == False:
                return False
        
        return True

    def escolher_bloco(self):
        if len(self.blocos) == 0:
            self.blocos = [Bloco_T(), Bloco_L(), Bloco_J(), Bloco_I(), Bloco_O(), Bloco_S(), Bloco_Z()]

        bloco = random.choice(self.blocos)
        self.blocos.remove(bloco)

        return bloco
    
    def desenhar(self, tela):
        self.Grade.desenhar(tela)
        self.bloco_atual.desenhar(tela, 31, 111)
        self.proximo_bloco.desenhar(tela, 325, 220)


    def reiniciar(self):
        self.Grade.reiniciar()
        self.blocos = [Bloco_T(), Bloco_L(), Bloco_J(), Bloco_I(), Bloco_O(), Bloco_S(), Bloco_Z()]
        self.bloco_atual = self.escolher_bloco()
        self.proximo_bloco = self.escolher_bloco()
        self.pontuacao = 0






Jogo = JOGO()
velocidade = 220

JOGO_UPDATE = pygame.USEREVENT
pygame.time.set_timer(JOGO_UPDATE, velocidade)

pygame.init()


def main():
    
    azul_escuro_borda = (33, 95, 194)
    azul_escuro_interface = (14, 29, 48)

    fonte_score = pygame.font.SysFont("Arial", 35)
    score = fonte_score.render("Score", 1, (255,255,255))


    fonte = pygame.font.SysFont("Arial", 30)
    texto_prox_bloco = fonte.render("PROXIMO", 1, (255,255,255))
    texto_derrota = fonte.render("SE FUDEU", 1, (255,0,0))

    score_rect = pygame.Rect(265, 8, 185, 100)
    prox_bloco_rect = pygame.Rect(435, 150, 140, 200)
    derrota_rect = pygame.Rect(435, 445, 142, 60)
    
    #prox_bloco = font_prox_bloco.render(f"{Jogo.proximo_bloco}", 1, (255,255,255))

    
    
    relogio = pygame.time.Clock()

    while True:
        relogio.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE and Jogo.derrota == True:
                    Jogo.derrota = False
                    Jogo.reiniciar()

                if event.key == K_s or event.key == K_DOWN and Jogo.derrota == False:
                    Jogo.mover_baixo()
                    Jogo.atualizar_score(0, 10)
                    
                if event.key == K_d or event.key == K_RIGHT and Jogo.derrota == False:
                    Jogo.mover_direita()
                if event.key == K_a or event.key == K_LEFT and Jogo.derrota == False:
                    Jogo.mover_esquerda()

                if event.key == K_r or event.key == K_UP and Jogo.derrota == False:
                    Jogo.rotacionar()

            if event.type == JOGO_UPDATE and Jogo.derrota == False:
                Jogo.mover_baixo()
                Jogo.atualizar_score(0, 1)
        
        
        if Jogo.pontuacao % 500 == 0:
            velocidade -= 5
            pygame.time.set_timer(JOGO_UPDATE, velocidade)

        

        tela.fill((14, 29, 60))
        
        pygame.draw.rect(tela, azul_escuro_borda, score_rect, 0, 10)
        tela.blit(score, (270, 10))
        
        fonte_pontos = pygame.font.SysFont("Arial", 60)
        pontos = fonte_pontos.render(f"{Jogo.pontuacao}", 1, (255,255,255))
        tela.blit(pontos, pontos.get_rect(centerx = score_rect.centerx, centery = 70))#(320, 40)

        pygame.draw.rect(tela, azul_escuro_borda, prox_bloco_rect, 0, 10)
        tela.blit(texto_prox_bloco, (445, 150))
        #tela.blit(prox_bloco,(375, 100, 50, 50))

        if Jogo.derrota:
            pygame.draw.rect(tela, (70,0,0), derrota_rect, 0, 10)
            tela.blit(texto_derrota, (445, 455))

        
        Jogo.desenhar(tela)
        
        pygame.display.update()
        

if __name__ == '__main__':
    main()