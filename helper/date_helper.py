import datetime


# returns date in date type object
def convert_to_date(date_text):
    try:
        # if date_text is already a date type do not convert anymore
        if isinstance(date_text, datetime.date):
            return date_text
        else:
            return datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        return None