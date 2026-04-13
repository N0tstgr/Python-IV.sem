from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("/mnt/data/assignment_handwritten.pdf")
styles = getSampleStyleSheet()

content = """Assignment – 2

Vikash Kasaudhan
2400970310212

1. Program: Dictionary of Student Details

student = {
"name" : "Vikash",
"roll_no" : "2400970310212",
"branch" : "CS",
"marks" : 85
}

student["email"] = "vikash@gmail.com"
student["marks"] = 90
del student["email"]

2. Compare List, Tuple and Dictionary

List → Ordered, mutable
Tuple → Ordered, immutable
Dictionary → Key-value pairs

3. Use of Functions

def greet(name):
    print("Hello", name)

greet("Vikash")

4. String Methods

s = "hello world"
print(s.upper())

s = "I love Java"
print(s.replace("Java","Python"))

5. Built-in Functions

len("Python") = 6
type(10) = int
sum([1,2,3,4,5]) = 15
"""

story = []

for line in content.split("\n"):
    story.append(Paragraph(line, styles["Normal"]))
    story.append(Spacer(1, 10))

doc.build(story)
