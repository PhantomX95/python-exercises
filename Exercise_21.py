# Text File Word Statistics:
# Write a program to read a text file and calculate the number of words, characters, sentences, and paragraphs, 
# calculate the average word length and the reading time based on 200 words per minute using oop.


# Algorithm:
# 01: Import re
# 02: Initialize class Text_Statistics:
#       - Function constructor with instance path.
#               - Assign variable self file path to file path so it can be used in methods.
#               - Assign variable to read the file.
#               - variable number of words, character, sentences, paragraph, average word length and reading time per minute all value 0. 
#       - Function readfile open file and handle error if file not found.
#       - Function calculate all the requirement.
#       - Function display the requirements.
# 03: Assign the file path.
# 04: Call the functions.

import re

class Text_Statistics:
    def __init__(self, file_path):
        self.file_path = file_path # Store the file path as an instance variable
        # Initialize requirements variables as 0
        self.number_words = 0
        self.number_characters = 0
        self.number_sentences = 0
        self.number_paragraphs = 0
        self.average_word_length = 0
        self.reading_time = 0
        self.text = self.read_file() # Read the file contents and store them in self.text
    
    # Reading the file contents
    def read_file(self):
        # Handle error if the file doesn't found
        try:
            # Open the file in read mode and close it after reading
            with open(self.file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File '{self.file_path}' Not Found!")
            return ""
    
    # Count the requirements
    def Calculate_Statistics(self):
        self.number_words = len(re.findall(r'\b[A-Za-z]+\b', self.text)) # Find all alphabetic sequences
        self.number_characters = len(re.findall(r'\w', self.text)) # Find all alphabetic characters
        self.number_sentences = len(re.findall(r'\b[.!?]+', self.text)) # Find the end of sentences by matching .!?
        self.number_paragraphs = len(re.findall(r'\n\s*\n', self.text)) + 1 if self.text.strip() else 0 # Find the Paragraph and if there's no space and not empty it's 1

        # Calculate the requirements
        if self.number_words > 0:
            # Average word length is the number of the characters / the number of words
            self.average_word_length = sum(len(word) for word in re.findall(r'\b[A-Za-z]+\b', self.text)) / self.number_words
        # Average reading time is the number of words / 200(the adult average time 200 to 380)
        self.reading_time = self.number_words / 200

    # Display the requirements results
    def Display_results(self):
        print(f"The Number Of Characters: {self.number_characters}")
        print(f"The Number Of Words: {self.number_words}")
        print(f"The Number Of Senteces: {self.number_sentences}")
        print(f"The Number Of Paragraphs: {self.number_paragraphs}")
        # if integer 1 say character else characters
        print(f"The Average Word Length: {self.average_word_length:.0f} {'Character' if self.average_word_length < 1.5 else 'Characters'}")
        # If 1 say minute else minutes
        print(f"Reading Time: {'Less Than a' if self.reading_time < 1.5 else round(self.reading_time)} {'Minute' if self.reading_time < 1.5 else 'Minutes'}")
    
if __name__ == '__main__':
    # Take the file path from the user
    file_path = input("Please Enter The File Path: ")
    # Create an instance with the file
    stats = Text_Statistics(file_path)
    # Call the method to calculate
    stats.Calculate_Statistics()
    # Show the results
    stats.Display_results()