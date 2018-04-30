import operator, re

def get_questions(questions, page, size, sorts=None):
    """ Return questions based on request parameters"""
    start_element = (page - 1) * size
    end_element = start_element + size

    if sorts:
        sort_field = sorts['0']['field']
        sort_direction = sorts['0']['dir']
        if sort_direction.lower() == 'asc':
            reverse = False
        else:
            reverse = True
        questions = sorted(questions, key=operator.attrgetter(sort_field), reverse=reverse)
    return questions[start_element:end_element]

def get_sorts(args):
    sorts = {}
    pattern = re.compile(r"sorters\[(\d*)\]\[([a-zA-Z]*)\]")
    for arg, value in args.items():
        match = pattern.match(arg)
        if match:
            sort_num = match.group(1)
            sort_type_direction = match.group(2)
            if sort_num not in sorts:
                sorts[sort_num] = {}
            sorts[sort_num][sort_type_direction] = value
    return sorts