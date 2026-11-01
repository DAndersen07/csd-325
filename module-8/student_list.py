"""Dustin Andersen - Assignment 8.
Load, display, update, and save a JSON student roster.
The added ID and email are fictional.
"""

import json
from pathlib import Path


def print_students(class_list):
    """Print every student's name, ID, and email."""
    for student in class_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , Email = {student['Email']}")


def main():
    """Read the roster, append a student, and save the updated list."""
    filename = Path(__file__).with_name('Student.json')
    with filename.open('r', encoding='utf-8') as student_file:
        class_list = json.load(student_file)

    print('Original Student list:')
    print_students(class_list)

    class_list.append({
        'F_Name': 'Dustin',
        'L_Name': 'Andersen',
        'Student_ID': 45606,
        'Email': 'dustin.andersen@example.com'
    })

    print('\nUpdated Student list:')
    print_students(class_list)

    # Save the complete updated array. Appending JSON text would be invalid.
    with filename.open('w', encoding='utf-8') as student_file:
        json.dump(class_list, student_file, indent=4)
        student_file.write('\n')

    print('\nStudent.json was updated.')


if __name__ == '__main__':
    main()
