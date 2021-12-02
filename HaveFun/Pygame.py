import pygame
import sys
import random
from time import sleep

BLACK = (0, 0, 0)
padWidth = 400  # 게임화면 가로크기
padHeight = 640  # 게임화면 세로크기

# 추가
src_path = 'src/'

rockImage = ['rock01.png', 'rock02.png', 'rock03.png', 'rock04.png', 'rock05.png',
             'rock06.png', 'rock07.png', 'rock08.png', 'rock09.png', 'rock10.png',
             'rock11.png', 'rock12.png', 'rock13.png', 'rock14.png', 'rock15.png',
             'rock16.png', 'rock17.png', 'rock18.png', 'rock19.png', 'rock20.png',
             'rock21.png', 'rock22.png', 'rock23.png', 'rock24.png', 'rock25.png',
             'rock26.png', 'rock27.png', 'rock28.png', 'rock29.png', 'rock30.png']
# 추가
for i in range(len(rockImage)):
    rockImage[i] = src_path + rockImage[i]

explosionSound = ['explosion01.wav', 'explosion02.wav', 'explosion03.wav', 'explosion04.wav']

# 추가
for i in range(len(explosionSound)):
    explosionSound[i] = src_path + explosionSound[i]


# 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font(src_path + 'NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수:' + str(count), True, (255, 255, 255))
    gamePad.blit(text, (10, 0))


# 운석이 화면 아래로 통과한 개수
def writePassed(count):
    global gamePad
    font = pygame.font.Font(src_path + 'NanumGothic.ttf', 20)
    text = font.render('놓친 운석:' + str(count), True, (255, 0, 0))
    gamePad.blit(text, (290, 0))


# 게임 메시지 출력
def writeMessage(text):
    global gamePad, gameOverSound
    textfont = pygame.font.Font(src_path + 'NanumGothic.ttf', 80)
    text = textfont.render(text, True, (255, 0, 0))
    textpos = text.get_rect()
    textpos.center = (padWidth / 2, padHeight / 2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()  # 배경음악 정지
    gameOverSound.play()  # 게임 오버 사운드 재생
    sleep(2)
    pygame.mixer.music.play(-1)  # 배경음악 재생
    runGame()


# 운석충돌시 메시지 출력
def crash():
    global gamePad
    writeMessage('전투기 파괴')


# 게임 오버 메시지 보이기
def gameover():
    global gamePad
    writeMessage('게임 오버')


def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))


def initGame():
    global gamePad, clock, background, fighter, missile, explosion, missileSound, gameOverSound
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight)) # 창 크기 설정
    pygame.display.set_caption('pyShooting')  # 게임 이름
    background = pygame.image.load(src_path + 'background.png')  # 배경 그림
    fighter = pygame.image.load(src_path + 'fighter.png')  # 전투기 그림
    missile = pygame.image.load(src_path + 'missile.png')  # 미사일 그림
    explosion = pygame.image.load(src_path + 'explosion.png')  # 폭발 그림
    pygame.mixer.music.load(src_path + 'music.wav')  # 배경음악
    pygame.mixer.music.play(-1)  # 배경음악 재생
    missileSound = pygame.mixer.Sound(src_path + 'missile.wav')  # 미사일 음악
    gameOverSound = pygame.mixer.Sound(src_path + 'gameover.wav')  # 게임오버 음
    clock = pygame.time.Clock()


def runGame():
    global gamepad, clock, background, fighter, missile, explosion, missileSound
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]  # 전투기 크기

    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0  # 전투기 초기위치

    missileXY = []  # 무기 좌표 리스트

    # 운석 랜덤 생성
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size  # 운석 크기
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    destroySound = pygame.mixer.Sound(random.choice(explosionSound))

    rockX = random.randrange(0, padWidth - rockWidth)  # 운석위치 초기 설정
    rockY = 0
    rockSpeed = 2

    isShot = False
    shotCount = 0
    rockPassed = 0

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:  # 게임 프로그램 종료
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:  # 전투기 왼쪽 이동
                    fighterX -= 5

                elif event.key == pygame.K_RIGHT:  # 전투기 오른쪽 이동
                    fighterX += 5

                elif event.key == pygame.K_SPACE:  # 미사일 발사
                    missileSound.play()  # 미사일 사운드 재생
                    missileX = x + fighterWidth / 2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])

            if event.type in [pygame.KEYUP]:  # 방향키를 떼면 전투기 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0

        drawObject(background, 0, 0)  # 배경화면 그리기

        x += fighterX  # 전투기 위치 재조정
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth  # x좌표를 전투기 좌표로 만들기 그리고 좌우 끝으로 가면 더이상 늘어나지 않게 하기 위해 고정

        # 전투기가 운석과 충돌했는지 체크
        if y < rockY + rockHeight:
            if (rockX > x and rockX < x + fighterWidth) or (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth) or (x > rockX and x + fighterWidth < rockX + rockWidth):
                crash()

        drawObject(fighter, x, y)  # 비행기를 게임 화면의 (x, y) 좌표에 그리기

        # 미사일 발사 화면에 그리기
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):  # 미사일 요소에 대해 반복
                bxy[1] -= 10  # 총알의 y좌표 -10(위로 이동), 총알의 속도값만큼 y좌표를 빼줌
                missileXY[i][1] = bxy[1]

                if bxy[1] < rockY:  # 미사일이 운석의 y좌표에 도달했을 때
                    if rockX < bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1

                if bxy[1] <= 0:  # 미사일이 화면 밖을 벗어나면
                    try:
                        missileXY.remove(bxy)  # 미사일 제거
                    except:
                        pass

        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        writeScore(shotCount)  # 운석 맞춘 점수 표시

        rockY += rockSpeed  # 운석 아래로 움직임

        # 운석이 지구로 떨어진경우
        if rockY > padHeight:
            rock = pygame.image.load(random.choice(rockImage))  # 새로운 운석 랜덤 생성
            rockSize = rock.get_rect().size  # 운석 크기
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)  # 운석위치 초기 설정
            rockY = 0
            rockPassed += 1

        # 운석 5개 놓치면 게임오버
        if rockPassed == 5:
            gameover()

        writePassed(rockPassed)  # 놓친 운석 수 표시

        # 운석을 맞춘 경우
        if isShot:
            drawObject(explosion, rockX, rockY)  # 운석 폭발
            destroySound.play()

            # 새로운 운석위치 랜덤 생성
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            destroySound = pygame.mixer.Sound(random.choice(explosionSound))
            isShot = False

            rockSpeed += 0.02
            if rockSpeed >= 10:
                rockSpeed = 10

        drawObject(rock, rockX, rockY)  # 운석 그리기

        pygame.display.update()  # 게임화면을 다시 그림

        clock.tick(60)  # 게임화면의 초당 프레임 60 고정

    pygame.quit()  # 파이게임 종료


initGame()
runGame()
