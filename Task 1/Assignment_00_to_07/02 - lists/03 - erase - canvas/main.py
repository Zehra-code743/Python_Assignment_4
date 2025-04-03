import time
import os

Canvas_width = 10
Canvas_Height = 10
Erase_Size = 2

# Initialize canvas with filled characters
canvas = [['█' for _ in range(Canvas_width)] for _ in range(Canvas_Height)]

def print_canvas():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in canvas:
        print(' '.join(row))
    print("\nMove the Eraser using W/A/S/D. Press Q to Quit.")

def erase(x, y):
    for i in range(max(0, y - Erase_Size), min(Canvas_Height, y + Erase_Size + 1)):
        for j in range(max(0, x - Erase_Size), min(Canvas_width, x + Erase_Size + 1)):
            canvas[i][j] = ' '

def main():
    eraser_x, eraser_y = 0, 0
    print_canvas()
    
    while True:
        command = input('Enter move (W/A/S/D) or Q to quit: ').upper()

        if command == 'Q':
            break
        elif command == 'W' and eraser_y > 0:
            eraser_y -= 1
        elif command == 'A' and eraser_x > 0:
            eraser_x -= 1
        elif command == 'S' and eraser_y < Canvas_Height - 1:
            eraser_y += 1
        elif command == 'D' and eraser_x < Canvas_width - 1:
            eraser_x += 1

        erase(eraser_x, eraser_y)
        print_canvas()
        time.sleep(0.1)

if __name__ == "__main__":
    main()
