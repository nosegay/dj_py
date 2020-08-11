from django import template
from datetime import datetime


register = template.Library()


@register.filter
def format_date(value):
    time_diff = datetime.now() - datetime.utcfromtimestamp(value)
    if time_diff.days > 1:
        return datetime.strptime(time_diff, "&Y-%m-%d")

    if time_diff.seconds / 60 < 10:
        return "только что"

    return f'{int(time_diff.seconds / 3600)} часов назад'


@register.filter
def parse_score(value, default_value=None):
    if default_value is not None:
        value = default_value
    score = int(value)
    if score < -5:
        return "всё плохо"

    if -5 <= score < 5:
        return "нейтрально"

    return "хорошо"


@register.filter
def format_num_comments(value):
    if value == 0:
        return "Оставьте комментарий"

    if 0 < value <= 50:
        return value

    return "50+"

@register.filter
def format_selftext(value, count):
    parsed_str = value.split()

    if len(parsed_str) <= count * 2:
        return value

    result_str = " ".join(parsed_str[:count]) + ' ... ' + " ".join(parsed_str[-count:])
    return result_str




