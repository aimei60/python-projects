import curses
from curses import wrapper
import time
import random

def sentence_choice():
    sentence_one = "The swift breeze carried the scent of fresh flowers as children played in the park, laughing and chasing each other"
    sentence_two = "A mysterious figure appeared at the edge of the forest, watching silently as the sun set behind the mountains"
    sentence_three = "The old library was filled with ancient books, their pages yellowed and worn, telling stories of times long past"
    sentence_four = "As the thunderstorm approached, the sky darkened, and lightning illuminated the clouds, creating a spectacular show of nature's power"
    sentence_five = "The bustling city streets were alive with activity, as people hurried to and fro, each with their own destination"
    return random.choice([sentence_one, sentence_two, sentence_three, sentence_four, sentence_five])
            
def main(stdscr):
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    MAGENTA = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    RED = curses.color_pair(3)
    
    sentence = sentence_choice()
    stdscr.clear()
    curses.echo()
    
    stdscr.addstr("Welcome to the WPM Test! Press enter to get your WPM", MAGENTA | curses.A_UNDERLINE)
    stdscr.addstr(1,0, sentence)
    stdscr.refresh()
    
    user_input = []
    correct_words = ""
    
    start_time = time.time()
    countdown_time = 60
    
    while time.time() - start_time < countdown_time:
        try:
            char = stdscr.getch()
            if char == ord("\n"):
                break
            user_input += chr(char)
        
            for i in range(len(user_input)):
                if i < len(sentence) and user_input[i] == sentence[i]:
                    stdscr.addstr(4, i , user_input[i], GREEN)
                    correct_words += user_input[i]
                else:
                    stdscr.addstr(4, i , user_input[i], RED)
                    stdscr.refresh()
        except curses.error:
            pass
        
        elapsed_time = int(time.time() - start_time)
        remaining_time = countdown_time - elapsed_time
        mins, secs = divmod(remaining_time, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        stdscr.addstr(5, 0, f"Time left: {timer}")
        stdscr.refresh()            
              
    correct_words = correct_words.split()
    wpm = round(len(correct_words) * 30 / countdown_time)
    stdscr.addstr(6,0, f"WPM: {wpm}", MAGENTA)

    stdscr.refresh()

    stdscr.getch()
        

curses.wrapper(main)