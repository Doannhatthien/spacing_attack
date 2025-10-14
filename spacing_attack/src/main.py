import pygame
from .settings import WIDTH, HEIGHT, STATE_MENU, STATE_CLASSIC, STATE_CHALLENGE, STATE_LEADERBOARD
from .utils import load_image, load_progress, save_progress
from .game import Game
from .menu import MainMenu
from .leaderboard import Leaderboard
from .challenge import Challenge
from .level_select import LevelSelect
from .name_prompt import NamePrompt

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Typing Game")

    try:
        background = load_image("background.jpg", (WIDTH, HEIGHT))
    except Exception:
        background = None

    lb = Leaderboard()
    state = STATE_MENU

    def goto_classic():
        nonlocal state
        state = STATE_CLASSIC

    def goto_challenge():
        nonlocal state
        state = STATE_CHALLENGE

    def goto_leaderboard():
        nonlocal state
        state = STATE_LEADERBOARD

    menu = MainMenu(goto_classic, goto_challenge, goto_leaderboard, background)

    running = True
    clock = pygame.time.Clock()

    while running:
        if state == STATE_MENU:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                else:
                    menu.handle(e)
            menu.draw(screen)
            pygame.display.flip()
            clock.tick(60)

        elif state == STATE_CLASSIC:
            from .utils import list_background_files
            from .background_select import BackgroundSelect
            from .name_prompt import NamePrompt 

            bg_files = list_background_files()
            chosen_bg = None

            if bg_files:
                selector = BackgroundSelect(bg_files)
                while chosen_bg is None and running:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            running = False
                            chosen_bg = "__CANCEL__"
                            break
                        res = selector.handle(e)
                        if res is not None:
                            chosen_bg = res
                    if not running: break
                    selector.draw(screen)
                    pygame.display.flip()
                    clock.tick(60)
                if not running: break
                if chosen_bg == "__CANCEL__":
                    state = STATE_MENU
                    continue

            game = Game()
            if chosen_bg and chosen_bg != "__CANCEL__":
                try:
                    game.background = load_image(chosen_bg, (WIDTH, HEIGHT))
                except Exception:
                    pass

            game.run()

            # Nếu người chơi bấm X đóng cửa sổ trong khi chơi, tránh prompt tên:
            if getattr(game, "request_quit", False):
                running = False
                break

            # Hiển thị nhập tên và lưu leaderboard Classic
            prompt = NamePrompt("Enter your name (Classic)")
            player_name = prompt.run(screen, background, default_if_empty="Player")
            lb.add_classic(player_name, game.score)

            state = STATE_MENU


        elif state == STATE_CHALLENGE:
            # 1) hiện level select
            progress = load_progress()
            unlocked   = progress.get("unlocked_level", 1)
            stars_arr  = progress.get("stars", [0] * 10)

            selector = LevelSelect(unlocked, stars_arr)
            chosen = None
            while chosen is None:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        running = False
                        chosen = -1
                    lv = selector.handle(e)
                    if lv is not None:
                        chosen = lv
                if not running: break
                selector.draw(screen)
                pygame.display.flip()
                clock.tick(60)

            if not running:
                break
            if chosen == -1:
                state = STATE_MENU
                continue

            # 2) chạy Challenge level đã chọn
            ch = Challenge(screen, background)
            completed, stars, score, lives = ch.run(chosen)

            # 3) nhập tên người chơi & lưu leaderboard (Challenge)
            from .name_prompt import NamePrompt
            prompt = NamePrompt(f"Enter your name (Challenge L{chosen})")
            player_name = prompt.run(screen, background, default_if_empty="Player")

            # Lưu: name, level, lives (đúng yêu cầu Challenge)
            # Cần Leaderboard.add_challenge(name, level, lives)
            lb.add_challenge(player_name, chosen, lives if lives is not None else 0)

            # 4) cập nhật sao đạt được cho level đã chơi
            if stars is None:
                stars = 0
            idx = chosen - 1
            stars_arr[idx] = max(int(stars_arr[idx]), int(stars))

            # 5) mở khóa màn kế tiếp nếu clear
            if completed and chosen >= unlocked and chosen < 10:
                unlocked = chosen + 1

            # 6) lưu progress (unlocked + stars)
            save_progress(unlocked, stars_arr)

            # 7) quay về menu
            state = STATE_MENU

        elif state == STATE_LEADERBOARD:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: running = False
                result = lb.handle(e)
                if result == "__EXIT__":
                    state = STATE_MENU
            lb.draw(screen, background)
            pygame.display.flip()
            clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
