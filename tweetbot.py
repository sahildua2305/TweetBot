import time
import tweepy


def main():
    f = open('twitterbot.txt', 'rU')
    for line in f:
        print line,
        time.sleep(3)


if __name__ == '__main__':
    main()
