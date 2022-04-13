# import canvas
from reportlab.pdfgen.canvas import Canvas
canvas = Canvas("20ce006_3rdResult.pdf")
canvas.drawString(50, 830, "---------------------------------------------Sem 3-20CE006-------------------------------------")
canvas.drawString(50, 800, "CE244 SOFTWARE GROUP PROJECT-1   PRACTICAL : AA")
canvas.drawString(50, 780, "CE251 JAVA PROGRAMMING PRACTICAL :AA THEORY: AA")
canvas.drawString(50, 760, "CE252 DIGITAL ELECTRONICS PRACTICAL :BC THEORY: BC")
canvas.drawString(50, 740, "CE257 DATA COMMUNICATION & NETWORKING PRACTICAL :AA THEORY: AB")
canvas.drawString(50, 720, "EE284 PYTHON PROGRAMMING PRACTICAL :AA ")
canvas.drawString(50, 700, "HS123.02 A CREATIVITY, PROBLEM SOLVING AND INNOVATION PRACTICAL : AA")
canvas.drawString(50, 680, "MA253 DISTINCT MATHEMATICS AND ALGEBRA THEORY: AA")
canvas.drawString(50, 660, "CGPA : 9.68")
canvas.drawString(50, 640, "SGPA : 9.78")
canvas.save()

# Setting the Page Size

from reportlab.lib.units import inch, cm  # noqa

print(cm)
print(inch)

canvas = Canvas("Result_Sem_3_20CE006.pdf", pagesize=(8.5 * inch, 11 * inch))

from reportlab.lib.pagesizes import LETTER  

canvas = Canvas("Result_Sem_3_20CE006.pdf", pagesize=LETTER)
print(LETTER)
