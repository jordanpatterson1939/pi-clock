import time


def blink(text,duration):
    clearline = ' '*len(text)
    for i in range(duration):
        print('\t\t'+text,end='\r')
        time.sleep(.5)
        print('\t\t'+clearline,end='\r')
        time.sleep(.5)

def main():
    text="Hello World"
    blink(text,20)

if __name__=='__main__':
    main()
