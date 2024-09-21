# Student Grading System: Create a system that allows teachers to input student names and grades,and then calculate the average,
# highest, and lowest grades for the class, Add the ability to generate a report card for each student, saved as a text file.


# Algorithm:
# 01: Initialize a class and it's construct and Initialize Students (dictionary) and Subjects (set).
#       - Prepare variables for tracking highest, lowest, total grades, and counts.
# 02: Collect Data:
#       - Get subjects from the teacher and store them in Subjects.
#       - For each student, get their grades for all subjects and store them in Students.
# 03: Calculate Statistics:
#       - For each subject, find the highest, lowest, and average grade.
#       - Track which student(s) got the highest and lowest grades.
# 04: Generate Report:
#       - Ask the teacher if they want a report.
#       - If yes, write overall class stats and individual student reports to a text file.




class Students_Grades():
    def __init__(self):
        # Initialize data structures for students and grades
        self.Students = {}
        self.Subjects = set()
        self.highest_grade = 0
        self.lowest_grade = 0
        self.total_grades = 0
        self.count_grades = 0

    def teacher_gets_grades(self):
        # Prompt teacher to enter subjects for the class
        print("Please Enter The Subjects Of The Class.")
        while True:
            subject = input("Enter a Subject Name ('D' Or 'Done' To Finish): ").title()
            if subject in ['D', 'Done']:
                break
            self.Subjects.add(subject)
            
        # Collect each student's name and their grades for each subject
        while True:
            student_name = input("Enter The Student's Name ('D' Or 'Done' To Finish): ").title()
            if student_name in ['D', 'Done']:
                break
            grades = {subject: '' for subject in self.Subjects}
            for subject in self.Subjects:
                while True:
                    try:
                        grade = int(input(f"Enter The {subject} Grade: "))
                        if not (0 <= grade <= 100):
                            print("Wrong Grade! Please Enter a Grade Between 0 and 100 (Only Numbers)")
                        else:
                            grades[subject] = grade
                            break
                    except ValueError:
                        print("Wrong Input! Please Enter Only The Grade Number.")
            self.Students[student_name] = grades
    
    def calculate_stats(self):
        # Initialize statistics for grades
        self.highest_grade = {subject: (0, []) for subject in self.Subjects}
        self.lowest_grade = {subject: (100, []) for subject in self.Subjects}
        self.total_grades = {subject: 0 for subject in self.Subjects}
        self.count_grades = {subject: 0 for subject in self.Subjects}

        # Calculate statistics for each student's grades
        for students, subjects in self.Students.items():
            for subject, grade in subjects.items():
                # Update highest and lowest grades
                if grade > self.highest_grade[subject][0]:
                    self.highest_grade[subject] = (grade, [students])
                elif grade == self.highest_grade[subject][0]:
                    self.highest_grade[subject][1].append(students)

                if grade < self.lowest_grade[subject][0]:
                    self.lowest_grade[subject] = (grade, [students])
                elif grade == self.lowest_grade[subject][0]:
                    self.lowest_grade[subject][1].append(students)
                
                # Sum grades and count occurrences
                self.total_grades[subject] += grade
                self.count_grades[subject] += 1

        # Print calculated statistics
        print("=================")
        print("Class Statistics:")
        print("=================\n")
        for subject in self.Subjects:
            if self.count_grades[subject] > 0:
                average = self.total_grades[subject] / self.count_grades[subject]
                print(f"\nSubject {subject}:")
                print(f"--------------------\n")
                print(f"Average Grade: {average:.2f}%")
                print(f"Highest Grade: {self.highest_grade[subject][0]}% by {' and '.join(self.highest_grade[subject][1])}")
                print(f"Lowest Grade: {self.lowest_grade[subject][0]}% by {' and '.join(self.lowest_grade[subject][1])}")

    def generate_report(self):
        # Check if there are students to generate reports for
        if not self.Students:
            print("No students to generate reports for.")
            return

        while True:
            user_choice = input("Do You Want To Generate a Report For Card For Each Student? Y/N: ").lower()
            if user_choice not in ('yes', 'no', 'y', 'n'):
                print("Wrong Input! Please Enter Y/Yes Or N/No.")
            elif user_choice in ('no', 'n'):
                print("No Report Generated.")
                break
            elif user_choice in ('yes', 'y'):
                # Create a report file and write overall statistics
                with open('Report.txt', 'w') as file:
                    file.write("===============================\n")
                    file.write("==== Overall Class Report =====\n")
                    file.write("===============================\n\n")
                    for subject in self.Subjects:
                        if self.count_grades[subject] > 0:
                            average = self.total_grades[subject] / self.count_grades[subject]
                            file.write(f"\nSubject {subject}:\n")
                            file.write(f"--------------------\n\n")
                            file.write(f"Average Grade: {average:.2f}%\n")
                            file.write(f"Highest Grade: {self.highest_grade[subject][0]}% by {' and '.join(self.highest_grade[subject][1])}\n")
                            file.write(f"Lowest Grade: {self.lowest_grade[subject][0]}% by {' and '.join(self.lowest_grade[subject][1])}\n")
                        else:
                            file.write("No Grades Available For This Subject")
                    
                    # Generate individual student reports
                    for student, subjects in self.Students.items():
                        if not subjects:
                            file.write(f"{student} has no grades recorded.\n")
                            continue
                        total_grades_student = 0
                        count_grade_student = 0
                        highest_grade_student = -1
                        highest_subject_student = ''
                        lowest_grade_student = 101
                        lowest_subject_student = ''

                        for subject, grade in subjects.items():
                            if grade is not None:
                                total_grades_student += grade
                                count_grade_student += 1
                                if grade > highest_grade_student:
                                    highest_grade_student = grade
                                    highest_subject_student = subject
                                if grade < lowest_grade_student:
                                    lowest_grade_student = grade
                                    lowest_subject_student = subject
                        
                        average_grade_student = total_grades_student / count_grade_student if count_grade_student > 0 else 0

                        # Write individual student report card
                        file.write("\n\n===============================\n")
                        file.write(f"Student {student}' Report Card:\n")
                        file.write("===============================\n\n")

                        for subject, grade in subjects.items():
                            file.write(f"{subject} => {grade if grade is not None else 'No Grade Recorded'}\n")
                        file.write("\n")

                        file.write(f"{student}' Statistics\n")
                        file.write("---------------------\n")
                        
                        file.write(f"Average Grade: {average_grade_student:.2f}%\n")
                        file.write(f"Highest Grade: {highest_grade_student}% In {highest_subject_student}\n")
                        file.write(f"Lowest Grade: {lowest_grade_student}% In {lowest_subject_student}\n")

                    file.write("\n")

                print("The Report Has Been Generated.")
                break

if __name__ == '__main__':
    # Execute the program
    grades = Students_Grades()
    grades.teacher_gets_grades()  # Collect grades from teacher
    grades.calculate_stats()       # Calculate and display statistics
    grades.generate_report()       # Generate a report file