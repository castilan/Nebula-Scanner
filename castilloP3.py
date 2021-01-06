"""
Program: CS115 Project 3
Author: Angelina Castillo
Description: Calls an inputted directory and can produce a noise-free image,
cycle through images, convert image to gray scale, and revert image to its original form.
"""
import sys
import time
from helper_graphics import *
from os.path import join


def draw_menu(win, w, h):
    """Creates and draws a menu of buttons. Buttons are hard coded to Cycle Through Images, Convert to GrayScale,
    Average the images, and Quit.

    Args:
        win (GraphWin): The window where buttons will be drawn.
        w (int): Width of the graphical window
        h (int): Height of the graphical window

    Returns:
        list: a list buttons, where buttons[i] is the i-th button (Rectangle object).

    """
    # list of the titles given to each button
    menu_titles = ["a. Cycle Through Images", "b. Convert to GrayScale", "c. Average the Images", "d. Quit", "e. Revert Images"]
    buttons = []  # list of button objects

    middle_x = w / 2  # x value for middle of the image
    middle_y = h / 2  # y value for middle of the image
    button_amount = len(menu_titles)  # number of buttons to be made

    # draw each button centered, starting halfway down the image
    for i in range(len(menu_titles)):
        button = draw_button(win, Point(middle_x, middle_y + i * (h / (button_amount*2))), menu_titles[i])
        # height calculations represent the spacing in between buttons
        # spacing is measured by the amount of elements in the list menu_titles

        buttons.append(button)

    return buttons


def cycleThrough(win, dirname, file_list, color):
    """ Cycles through images
    Args:
        win (GraphWin): The window where the image will be displayed.
        dirname (directory) : File where images are stored.
        file_list (list): Contains all the names of the images in dirname
        color (Boolean): Tells if image is gray or colorful
    return:
        None
    """
    if color is True:

        for i in range(0, 10):
            inputImageFilename = file_list[i]
            fullname = join(dirname, inputImageFilename)

            img = Image(Point(0, 0), fullname)

            w = img.getWidth()
            h = img.getHeight()

            img.setAnchor(Point(w // 2, h // 2))

            win.setTitle("showing " + inputImageFilename)
            img.draw(win)

            win.getMouse()

    elif color is False:
        for i in range(0, 10):
            inputImageFilename = file_list[i]
            fullname = join(dirname, inputImageFilename)

            img = Image(Point(0, 0), fullname)

            w = img.getWidth()
            h = img.getHeight()

            img.setAnchor(Point(w // 2, h // 2))

            win.setTitle("showing " + inputImageFilename)
            img = grayImage(img)
            img.draw(win)

            win.getMouse()


def grayImage(img):
    """ Converts an image to gray scale.
    args:
        image(img): image
    return:
        image
    """

    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            rgb = img.getPixel(x, y)
            avg = convertToGray(rgb)
            img.setPixel(x, y, color_rgb(int(avg), int(avg), int(avg)))

    return img


def averageImages(dirname, win, img):
    """ Computes and saves average pixel color into image.
    args:
        dirname(directory): Where images are stored.
        win(GraphWin): Window where images are drawn.
        image(img): Menu image.

    """
    file_list = os.listdir(dirname)
    img_list = []

    for i in range(len(file_list)):
        fullname = join(dirname, file_list[i])
        pic = Image(Point(0, 0), fullname)
        w = pic.getWidth()
        h = pic.getHeight()
        pic.setAnchor(Point(w // 2, h // 2))
        img_list.append(pic)

    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            r = 0
            g = 0
            b = 0

            for j in range(len(img_list)):  # for loop runs through each image in dirname
                rgb = img_list[j].getPixel(x, y)
                r = rgb[0] + r
                g = rgb[1] + g
                b = rgb[2] + b
            img.setPixel(x, y, color_rgb(int(r//len(img_list)), int(g//len(img_list)), int(b//len(img_list))))

    img.undraw()  # removes menu image
    img.draw(win)  # image drawn without menu
    win.getMouse()


def revertImages(w, h, name):
    """ reassigns an image to its original form
    args:
        w(int): width of the image
        h(int): height of the image
        name: fullname or the path to the file holding original image
    return:
        img(Image): The first image from the original file

    """
    # Create an Image object using fullname. Store it in variable img
    img = Image(Point(0, 0), name)

    # Set anchor of image to its center point
    img.setAnchor(Point(w // 2, h // 2))
    return img




def wait_for_menu(win, buttons):
    """Waits for a click, detects the clicked button and returns its index.

    Args:
        win (GraphWin): The window where the user would click.
        buttons (list): A list, where buttons[i] is the i-th button (Rectangle object).

    Returns:
        int: a value between 0 and len(buttons)-1, indicating the
             index of the button that was clicked.
    """
    # Upper left points of the button are in variables ending with "ul"
    # Lower Right points of the button are in variables ending with "lr"

    button_ul = buttons[0].getP1()
    button_lr = buttons[0].getP2()

    button_ul_1 = buttons[1].getP1()
    button_lr_1 = buttons[1].getP2()

    button_ul_2 = buttons[2].getP1()
    button_lr_2 = buttons[2].getP2()

    button_ul_3 = buttons[3].getP1()
    button_lr_3 = buttons[3].getP2()

    button_ul_4 = buttons[4].getP1()
    button_lr_4 = buttons[4].getP2()

    # wait for user to click screen
    mousept = win.getMouse() # store user click in mousept

    # if mousept point is within range of a button, return the button index

    if button_ul.getX() < mousept.getX() < button_lr.getX() and \
            button_ul.getY() < mousept.getY() < button_lr.getY():
        return 0  # 0 is Cycle Through Images

    elif button_ul_1.getX() < mousept.getX() < button_lr_1.getX() and \
            button_ul_1.getY() < mousept.getY() < button_lr_1.getY():
        return 1  # 1 is Convert to GrayScale

    elif button_ul_2.getX() < mousept.getX() < button_lr_2.getX() and \
            button_ul_2.getY() < mousept.getY() < button_lr_2.getY():
        return 2  # 2 is Average the images

    elif button_ul_3.getX() < mousept.getX() < button_lr_3.getX() and \
            button_ul_3.getY() < mousept.getY() < button_lr_3.getY():
        return 3  # 3 is Quit
    elif button_ul_4.getX() < mousept.getX() < button_lr_4.getX() and \
            button_ul_4.getY() < mousept.getY() < button_lr_4.getY():
        return 4  # 4 is Revert Images
    else:
        return None


def main():
    dirname = input("Name of directory you want to open: ")

    file_list = os.listdir(dirname)
    print("List of images:", file_list)

    # Get first noisy image
    inputImageFilename = file_list[0]
    fullname = join(dirname, inputImageFilename)
    print('Full path of first file:', fullname)

    # Create an Image object using fullname. Store it in variable img
    img = Image(Point(0, 0), fullname)

    # Get width and height of image
    w = img.getWidth()
    h = img.getHeight()

    # Set anchor of image to its center point
    img.setAnchor(Point(w // 2, h // 2))

    try:
        # Create a window the same size of the image

        win = GraphWin("Click to continue...", w, h)
        img.draw(win)

        # Draw menu after image is displayed and user clicks on image
        win.getMouse()
        button = draw_menu(win, w, h)
        button_index = wait_for_menu(win, button)

        color = True  # color determines if the image has color or is gray scale

        while button_index != 3:
            # User clicked convert image to black and white
            if button_index == 1:
                grayImage(img)
                color = False  # color indicates that all the images are in gray scale

            # user clicked Average the images
            elif button_index == 2:
                averageImages(dirname, win, img)
                button = draw_menu(win, w, h)

            # user clicked Cycle Through Images
            elif button_index == 0:
                cycleThrough(win, dirname, file_list, color)
                win.close()
                win = GraphWin("Click to continue...", w, h)
                img.draw(win)
                button = draw_menu(win, w, h)

            # user clicked Revert Images
            elif button_index == 4:
                img = revertImages(w, h, fullname)  # revert img
                img.draw(win)                       # draw the reverted image
                color = True                        # reset the color to true so cycleThrough displays color images
                button = draw_menu(win, w, h)

            # wait for user click at menu once again
            button_index = wait_for_menu(win, button)

        # user clicked quit
        if button_index == 3:
            win.close()

    # user clicked the "x" button for the window instead of the Quit button
    except GraphicsError:
        print("Please close the window properly next time")


main()
