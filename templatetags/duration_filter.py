from django import template

register = template.Library()

@register.filter
def duration(value, arg:str):
    try:
        total_seconds = int(value.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if arg:
            return (
                arg
                .replace('h', str(hours))
                .replace('i', str(minutes))
                .replace('s', str(seconds))
            )
        else:
            return f"{hours}시 {minutes}분 {seconds}초"
    except Exception:
        return value