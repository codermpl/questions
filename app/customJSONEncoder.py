from flask.json import JSONEncoder

from app.question import Question


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Question):
            return {
                'question': obj.question,
                'answer': obj.answer,
                'distractors': obj.distractors,
            }
        return super(CustomJSONEncoder, self).default(obj)
