# voice_maze.py
import pygame, speech_recognition as sr, threading, queue, time

WIDTH, HEIGHT = 400, 400
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(50, 50, 20, 20)
speed = 20

commands = queue.Queue()

def listen_thread(q):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            try:
                audio = r.listen(source, timeout=3)
                text = r.recognize_google(audio).lower()
                q.put(text)
            except Exception:
                pass

t = threading.Thread(target=listen_thread, args=(commands,), daemon=True)
t.start()

maze = [pygame.Rect(100,100,200,20), pygame.Rect(100,200,20,200)]

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    # process voice commands
    try:
        cmd = commands.get_nowait()
        print("Heard:",cmd)
        if "left" in cmd: player.x -= speed
        if "right" in cmd: player.x += speed
        if "up" in cmd: player.y -= speed
        if "down" in cmd: player.y += speed
    except:
        pass

    win.fill((30,30,30))
    pygame.draw.rect(win, (0,0,255), player)
    for m in maze: pygame.draw.rect(win, (200,0,0), m)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
