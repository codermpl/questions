import csv

from app.question import Question

def import_csv(filename):
    with open(filename, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter='|')
        questions = list()
        next(reader) # Ignore header row
        for row in reader:
            question = row[0]
            answer = row[1]
            distractors = row[2].split(', ')
            questions.append(Question(question, answer, distractors))
    return questions