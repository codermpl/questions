import csv, logging
from app.question import Question

log = logging.getLogger(__name__)


def import_csv(filename):
    """ Load the questions from a csv file """
    log.info("Begin loading questions.")
    with open(filename, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter='|')
        questions = list()
        next(reader) # Ignore header row
        for row in reader:
            question = row[0]
            answer = row[1]
            distractors = row[2].split(', ')
            questions.append(Question(question, answer, distractors))
    log.info("Loaded %s questions", len(questions))
    return questions
