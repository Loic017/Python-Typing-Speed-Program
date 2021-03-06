import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear() # Clear Screen
    stdscr.addstr("Speed Typing Test") # Add string to screen
    stdscr.addstr("\nPress any key to start! >>")
    stdscr.refresh() # Refresh screen, update it to add the string
    stdscr.getkey() # Get the key input from the user

def display_text(stdscr, target, current, wpm=0): # wpm is an optional parameter
        stdscr.addstr(target)
        stdscr.addstr(1, 0, f"WPM: {wpm}")

        for i,char in enumerate(current): # Enumerate passes element AND index
            correct_char = target[i]
            color = curses.color_pair(1)
            if char != correct_char:
                color = curses.color_pair(2)
            stdscr.addstr(0, i, char, color)

def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()
        
    
def wpm_test(stdscr):
    target_text = load_text()
    inputted_text = []
    #stdscr.clear()
    #stdscr.addstr(target_text)
    #stdscr.refresh()        
    #stdscr.getkey()
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(inputted_text)/ (time_elapsed/60))/5)
        
        stdscr.clear()
        display_text(stdscr, target_text, inputted_text, wpm)
        stdscr.refresh()
        
        if target_text == "".join(inputted_text):
            stdscr.nodelay(False)
            break
            
        try:
            key = stdscr.getkey()
        except:
            continue
        
        if ord(key) == 27: # ASCII representation for escape
            break # Break if user presses escape
        
        if key in ("KEY_BACKSPACE", '\b', "\x7f"): # Representation of backspace
            if len(inputted_text) > 0:
                inputted_text.pop()
        elif len(inputted_text) < len(target_text):
            inputted_text.append(key)
    
def main(stdscr):
    # Terminal text colours
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        
        stdscr.addstr(2, 0, "Text Completed. \n\nPress any ESC to exit. \nPress anything else to continue. \n>>")
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break
        

wrapper(main)
    
