from PIL import ImageGrab, ImageOps  # for taking screen
import pyautogui  # for mouse operations
import time
pyautogui.PAUSE = 0.01
pyautogui.MINIMUM_DURATION = 0.01


def locate_tiles():
    first = True    # is it the first tile?
    score = 0
    game_cord = [8, 40, 383, 700]  # cord of game [x1,y1,x2,y2]
    try:
        while 1:
            run = True
            color = 0  # color of normal block tile
            stime = time.time()  # start time of program
            image = ImageGrab.grab(game_cord)
            grayimage = ImageOps.grayscale(image)  # scaling image to gray
            width, height = grayimage.size
            screen_y = range(height - 1, 45, -1)  # y points to compare
            column_sep = int(width/4)  # separation lines
            columns_x_position = [column_sep - 40, 2*column_sep - 40, 3*column_sep - 40, width - 40]  # all four columns
            if first:
                color = 132  # color of start tile
                screen_y = range(height - 200, 1, -1)
            pix = grayimage.load()  # saving pixel of image
            for act_y in screen_y:
                if not run:
                    break
                for act_x in columns_x_position:  # 4 columns positions
                    if not run:
                        break
                    if pix[act_x, act_y] == color or pix[act_x, act_y] == 1:  # check if color == start,normal,long tile
                        if score > 1000:
                            act_y += 10
                        if score > 1300:
                            act_y += 20
                        if score > 1700:
                            act_y += 20
                        pyautogui.moveTo(act_x, act_y)
                        pyautogui.click()
                        run = False
                        first = False
                        score += 1  # current score
                        print(f"It took {time.time() - stime} s to click | score = {score}")  # time of execution
    except pyautogui.FAILSAFE:
        print("Emergency stop")
        exit()
    except Exception as e:
        print(e)
        exit()


locate_tiles()
