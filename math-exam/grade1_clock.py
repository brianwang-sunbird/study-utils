# coding:utf-8

import random
from font_util import useChineseFont

def add():
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    return '%d + %d = ' % (a, b)
    
def sub():
    while True:
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        c = a + b    
        if c < 100:
            break
    return '%d - %d = ' % (c, a)
    
def drawClock(c, x, y, hour, minu):
    from reportlab.lib.colors import black, white
    from reportlab.lib.units import inch
    import math
    c.setStrokeColor(black)
    c.setLineWidth(1)
    c.setLineCap(1)
    c.setDash(1,0)
    u = inch/10.0
    r = 9*u
    c.circle(x, y, r, stroke=1, fill=0)
    c.circle(x, y, r / 18, stroke=1, fill=0)
    d = 360. / 60
    r1 = r - (r / 26)
    r2 = r - (r / 13)
    for i in range(60):
        if i % 5 == 0:
            c.setLineWidth(2)
            n = i / 5
            if n == 0:
                n = 12
            drawNumber(c, x, y, 0.83 * r, d * i, '%d' % n)
        else:
            c.setLineWidth(1)
        drawHand(c, x, y, r1, r2, d * i)    

    # draw long hand
    mdegree = minu / 60. * 360.
    rm = r - (r / 7)
    drawHand(c, x, y, rm, r / 18, mdegree)
    c.setLineWidth(2)
    rm1 = r - (r / 3)
    rm2 = r / 12
    drawHand(c, x, y, rm1, rm2, mdegree)    

    # draw short hand
    c.setLineWidth(2)
    hdegree = ((hour % 12) * 60 + minu) / 720. * 360
    rh = r - (r / 3)
    drawHand(c, x, y, rh, r / 18, hdegree)
    c.setLineWidth(3)
    rh1 = r - (r / 2)
    rh2 = r / 12
    drawHand(c, x, y, rh1, rh2, hdegree)
    c.setStrokeColor(white)
    c.setLineWidth(1)
    rh3 = r - (r / 1.9)
    rh4 = r / 11
    drawHand(c, x, y, rh3, rh4, hdegree)
    c.setStrokeColor(black)

def drawNumber(c, x, y, r, deg, num):
    from reportlab.lib.colors import gray, black
    c.setFont("kaiu", 10)
    c.setFillColor(gray)
    x1 = r * math.sin(deg / 180. * math.pi) + x
    y1 = r * math.cos(deg / 180. * math.pi) + y
    c.drawString(x1 - 3.5, y1 - 3.5, num)
    c.setFillColor(black)
    
def drawHand(c, x, y, r1, r2, deg):
    x1 = r1 * math.sin(deg / 180. * math.pi) + x
    y1 = r1 * math.cos(deg / 180. * math.pi) + y
    x2 = r2 * math.sin(deg / 180. * math.pi) + x
    y2 = r2 * math.cos(deg / 180. * math.pi) + y
    c.line(x1, y1, x2, y2)
    
def generate(c, page):
    sectiony = 3
    gridy = 9 / sectiony
    c.setFont("kaiu", 16)
    from reportlab.lib.units import inch
    from reportlab.lib.colors import black
    # draw basic form
    c.drawString(inch, 10.2 * inch, "姓名:                  座號:                  成績:")
    for i in range(sectiony + 1):
        if i > 0:
            c.setDash(1,2)
        c.line(inch, 10 * inch - i * gridy * inch, 7.5 * inch, 10 * inch - i * gridy * inch)

    c.line((8.5 / 2) * inch, 10 * inch, (8.5 / 2) * inch, 1 * inch)
    
    #textobject.setFont("Helvetica-Oblique", 14)
    for i in range(6):
        th = random.randint(0, 11)
        tm = random.randint(0, 59)
        x = inch * 1.1 + (6.5 / 2) * inch * int(i/sectiony)
        y = 9.7 * inch - (i % sectiony) * inch * gridy
        c.setFont("kaiu", 16)
        c.drawString(x, y, '%d' % (i + 1))
        drawClock(c, x + inch, y - (inch * 0.9), th, tm)

    pagetag = 'P%d' % page
    width = c.stringWidth(pagetag)
    c.drawString( (8.5 / 2) * inch - width / 2, 0.8 * inch, pagetag)
    from datetime import datetime
    dt_obj = datetime.now()
    date_str = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
    c.setFont("kaiu", 12)
    c.drawString((8.5 - 3) * inch, 0.8 * inch, date_str)
    
def main():
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.pdfgen import canvas
    c = canvas.Canvas("clock.pdf", pagesize=letter)
    useChineseFont()
    for i in range(10):
        generate(c, i + 1)
        c.showPage()
    c.save()
    
if __name__ == '__main__':
    import math
    print math.sin(90. / 180. * math.pi)
    main()
