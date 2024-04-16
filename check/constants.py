import pygame


WIDTH = 800
HEIGHT = 800

SQUARE_SIZE = 100

ROWS = WIDTH//SQUARE_SIZE
COLS = HEIGHT//SQUARE_SIZE

WHITE = (255,255,255)
BLACK = (0,0,0)
BROWN = (165,42,42)
GRAY = (207, 185, 151)


black_queen = pygame.image.load('c:/Users/skace/OneDrive/Dokumenty/Chess/check/assets/black queen.png')
black_queen = pygame.transform.scale(black_queen, (90, 90))
print(4)

black_king = pygame.image.load('c:/Users/skace/OneDrive/Dokumenty/Chess/check/assets/black king.png')
black_king = pygame.transform.scale(black_king, (90, 90))

black_rook = pygame.image.load('c:/Users/skace/OneDrive/Dokumenty/Chess/check/assets/black rook.png')
black_rook = pygame.transform.scale(black_rook, (70, 70))

black_bishop = pygame.image.load('c:/Users/skace/OneDrive/Dokumenty/Chess/check/assets/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))

black_knight = pygame.image.load('c:/Users/skace/OneDrive/Dokumenty/Chess/check/assets/black knight.png')
black_knight = pygame.transform.scale(black_knight, (75, 75))

black_pawn = pygame.image.load('c:/Users/skace/OneDrive/Dokumenty/Chess/check/assets/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))



white_queen = pygame.image.load('c:/Users/skace/OneDrive/Dokumenty/Chess/check/assets/white queen.png')
white_queen = pygame.transform.scale(white_queen, (90, 90))

white_king = pygame.image.load('c:/Users/skace/OneDrive/Dokumenty/Chess/check/assets/white king.png')
white_king = pygame.transform.scale(white_king, (90, 90))

white_rook = pygame.image.load('c:/Users/skace/OneDrive/Dokumenty/Chess/check/assets/white rook.png')
white_rook = pygame.transform.scale(white_rook, (70, 70))

white_bishop = pygame.image.load('c:/Users/skace/OneDrive/Dokumenty/Chess/check/assets/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))

white_knight = pygame.image.load('c:/Users/skace/OneDrive/Dokumenty/Chess/check/assets/white knight.png')
white_knight = pygame.transform.scale(white_knight, (75, 75))

white_pawn = pygame.image.load('c:/Users/skace/OneDrive/Dokumenty/Chess/check/assets/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))