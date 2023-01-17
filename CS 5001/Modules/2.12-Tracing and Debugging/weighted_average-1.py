"""
Module: Variables & Arithmetic Operators
Lesson 2-6: Tracing and Debugging
Author: Maria Jump

This is the code that we are writing in this module.  It is NOT COMPLETE and
still contains an error.  Can you find it using the provided test cases?  
If not, watch the video for this lesson all the way to the end.
"""


def main():
    reading = int(input("Enter grade for readings: "))
    labs = int(input("Enter grade for labs: "))
    hw = int(input("Enter grade for hw: "))
    exams = int(input("Enter grade for exams: "))

    # calculations
    read_part = reading * 5
    lab_part = labs * 15
    hw_part = hw * 50
    exam_part = exams * 30
    average = read_part + lab_part + hw_part + exam_part / 100


main()
