''' Graphics functions for Image Transformations project

    You can create your own versions of these functions and give
    them different names (in your own file), but DO NOT CHANGE THIS FILE.

    Functions include:
    - draw_button: draw and return a button
    - wait_for_button: wait until the user clicks the button, then return
    - normalize: Transform pixel value according to a range given by minimum and maximum value, then return it

    
    See the specific documentation for each function.

    Authors: Suzanne Rivoire and Gurman Gill '''

import statistics
from graphics import *

constY = 15

def draw_button(win, txtCenter, txt):
    '''Draw a button with text, and returns the button.

    Args:
        win (GraphWin): the window to draw the button in
        txtCenter (Point): the coordinates of button center
        txt (str): text to draw in button

    Returns:
        Rectangle object: the button that is drawn
    '''

    button = Rectangle(Point(txtCenter.getX() - len(txt) * 5,
                             txtCenter.getY() - constY),
                       Point(txtCenter.getX() + len(txt) * 5,
                             txtCenter.getY() + constY))

    button.setFill('DarkGray')
    button.draw(win)

    buttontxt = Text(txtCenter, txt)
    buttontxt.setSize(20)
    buttontxt.draw(win)

    return button
    

def wait_for_button(win, button):
    '''Waits for the user to click the button.

    Args:
        win (GraphWin): the window to draw the button in
        button (Rectangle): the button

    Returns:
        None
    '''
    button_ul = button.getP1() # button upper left
    button_lr = button.getP2() # button upper right
    
    # Infinite loop - will break out of it by 
    # returning if the user clicks the button
    while True:
        mousept = win.getMouse()
        if button_ul.getX() < mousept.getX() < button_lr.getX() and \
           button_ul.getY() < mousept.getY() < button_lr.getY():
           return

def convertToGray(rgb):
    '''Converts RGB value to gray value.

        Args:
            rgb (list): three values storing R, G and B values

        Returns:
            Average of R, G and B
        '''

    return statistics.mean(rgb)



def normalize(val, minval, maxval):
    '''Transforms a value so it is within the bounds indicated.

    Args:
        val (int): The value to normalize
        minval (int): Minimum value
        maxval (int): Maximum value

    Returns:
        int: the normalized value, after checking for out of bounds error.
    '''
    norm = int(255*(val - minval)/(maxval-minval))
    if (norm < 0):
        norm = 0
    elif (norm > 255):
        norm = 255
    return norm

