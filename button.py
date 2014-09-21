#  button.py
#  a class from the Zelle text on button creation
# basically a weak widget

import graphics


class Button:

    """ A button is rectangle in a wind activated() or deactived() w/ methodes
    theclicked methode returns true if click was in the rectable"""

    def __init__(self, win, center, width, height, label):
        """ creates a rectangluar button eg:
        qb = Button(myWin, centerpoint, width, height, 'QUIT') """

        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = graphics.Point(self.xmin, self.ymin)
        p2 = graphics.Point(self.xmax, self.ymax)
        self.rect = graphics.Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = graphics.Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """returns true if the button is active and p is inside the button"""
        statement_a = self.ymin <= p.getY() <= self.ymax
        statement_b = self.xmin <= p.getX() <= self.xmax
        return self.active and statement_b and statement_a

    def getLabel(self):
        """Returns the label string of the button"""
        return self.label.getText()

    def activate(self):
        """Sets the button to active"""
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """Sets the button to inactive"""
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False