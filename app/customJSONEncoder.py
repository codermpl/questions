from flask.json import JSONEncoder

from app.question import Question


class CustomJSONEncoder(JSONEncoder):
    """ Class to turn Question object to JSON """
    def default(self, obj):
        if isinstance(obj, Question):
            return {
                'question': obj.question,
                'answer': obj.answer,
                'distractors': obj.distractors,
            }
        return super().default(obj)
