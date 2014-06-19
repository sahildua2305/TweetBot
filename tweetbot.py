import time


def main():
    f = open('tweetbot.txt', 'rU')
    for line in f:
        print line,
        time.sleep(3)


if __name__ == '__main__':
    main()
