import operator, re, logging

log = logging.getLogger(__name__)


def get_questions(questions, page, size, sorts=None):
    """ Return questions based on request parameters"""
    log.info("Getting questions. Page %s, Number of questions: %s", page, size)
    start_element = (page - 1) * size
    end_element = start_element + size

    if sorts:
        log.debug("Received sorting")
        sort_field = sorts['0']['field']
        sort_direction = sorts['0']['dir']
        if sort_direction.lower() == 'asc':
            reverse = False
        else:
            reverse = True
        questions = sorted(questions, key=operator.attrgetter(sort_field), reverse=reverse)
    return questions[start_element:end_element]

def get_sorts(args):
    """ Get the parameters to sort the questions """
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

def get_pagination_params(args):
    """ Get the size and page number from the parameters """
    try:
        page = int(args.get('page', 1))
    except ValueError:
        log.warning("Page parameter not valid, defaulting to 1")
        page = 1

    try:
        size = int(args.get('size', 20))
    except ValueError:
        log.warning("Size parameter not valid, defaulting to 20")
        size = 20

    return page, size