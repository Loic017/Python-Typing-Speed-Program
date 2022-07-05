import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear() # Clear Screen
    stdscr.addstr("Speed Typing Test") # Add string to screen
    stdscr.addstr("\nPress any key to START!")
    stdscr.refresh() # Refresh screen, update it to add the string
    stdscr.getkey() # Get the key input from the user

def wpm_test(stdscr):
    target_text = "Hello this is some test text."
    inputted_text = []
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()        
    stdscr.getkey()
    
    while True:
        stdscr.clear()
        stdscr.addstr(target_text)

        for char in inputted_text:
            stdscr.addstr(char, curses.color_pair(1))
            
        stdscr.refresh()
        
        key = stdscr.getkey()   
        
        if ord(key) == 27: # ASCII representation for escape
            break # Break if user presses escape
        
        if key in ("KEY_BACKSPACE", '\b', "\x7f"): # Representation of backspace
            if len(inputted_text) > 0:
                inputted_text.pop()
        else:
            inputted_text.append(key)
    
    
def main(stdscr):
    # Terminal text colours
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)
    
