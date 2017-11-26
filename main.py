import sys
import os
import curses

board_state = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def draw_game(stdscr):

    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.COLOR_GRAY = 8
    curses.init_color(curses.COLOR_GRAY, 500, 500, 500)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GRAY)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Check screen size
        if height < 15 or width < 22:
            # Print warning
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(0, 0, "WARNING")
            stdscr.attroff(curses.color_pair(2))
            # Refresh the screen
            stdscr.refresh()

        else:
            if k == curses.KEY_DOWN:
                cursor_y = cursor_y + 1
            elif k == curses.KEY_UP:
                cursor_y = cursor_y - 1
            elif k == curses.KEY_RIGHT:
                cursor_x = cursor_x + 1
            elif k == curses.KEY_LEFT:
                cursor_x = cursor_x - 1

            cursor_x = max(0, cursor_x)
            cursor_x = min(width-1, cursor_x)

            cursor_y = max(0, cursor_y)
            cursor_y = min(height-1, cursor_y)

            # Declaration of strings
            title = "Tic Tac Toe"[:width-1]
            subtitle = "Written in Python"[:width-1]
            instr_title = "Instructions"
            instr_move = " Use keypad to move cursor"
            instr_select = " Press enter to select square"
            instr_quit = " Press 'q' to exit"
            if k == 0:
                keystr = "No key press detected..."[:width-1]

            # Centering calculations
            start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
            start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
            start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
            start_x_instr_title = int((width // 2) - (len(instr_title) // 2) - len(instr_title) % 2)
            start_y = 1


            # Render status bar
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(height-4, 0, " " * (start_x_instr_title - 1))
            stdscr.addstr(height-4, start_x_instr_title - 1, instr_title)
            stdscr.addstr(height-4,
                          start_x_instr_title + len(instr_title) - 1,
                          " " * (width - (start_x_instr_title + len(instr_title))))
            stdscr.addstr(height-3, 0, instr_move)
            stdscr.addstr(height-2, 0, instr_select)
            stdscr.addstr(height-1, 0, instr_quit)
            stdscr.addstr(height-3, len(instr_move), " " * (width - len(instr_move) - 1))
            stdscr.addstr(height-2, len(instr_select), " " * (width - len(instr_select) - 1))
            stdscr.addstr(height-1, len(instr_quit), " " * (width - len(instr_quit) - 1))
            stdscr.attroff(curses.color_pair(3))

            # Turning on attributes for title
            stdscr.attron(curses.color_pair(2))
            stdscr.attron(curses.A_BOLD)

            # Rendering title
            stdscr.addstr(start_y, start_x_title, title)

            # Turning off attributes for title
            stdscr.attroff(curses.color_pair(2))
            stdscr.attroff(curses.A_BOLD)

            # Print rest of text
            stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
            stdscr.move(cursor_y, cursor_x)

            # Print board
            stdscr.attron(curses.color_pair(3))
            start_x_board = int((width // 2) - (17 // 2) - 17 % 2)
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(4, start_x_board, " " * 17)
            for x in range(0, 4):
                stdscr.addstr(5, start_x_board + (x * 5), "  ")
            stdscr.addstr(6, start_x_board, " " * 17)
            for x in range(0, 4):
                stdscr.addstr(7, start_x_board + (x * 5), "  ")
            stdscr.addstr(8, start_x_board, " " * 17)
            for x in range(0, 4):
                stdscr.addstr(9, start_x_board + (x * 5), "  ")
            stdscr.addstr(10, start_x_board, " " * 17)

            # Refresh the screen
            stdscr.refresh()

            # Wait for next input
            k = stdscr.getch()


def main():
    curses.wrapper(draw_game)

if __name__ == "__main__":
    main()
