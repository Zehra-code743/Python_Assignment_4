import random

Done_Likes = 0.3

def done():
    return random.random() < Done_Likes

def like():
    for i in range(0 , 10):
        cur = i + 1
        if done():
            return
        print(cur)

def main():
    like()
    print('Like Done')


if __name__ == "__main__":
    main()