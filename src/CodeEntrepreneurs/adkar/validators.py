from django.core.exceptions import ValidationError
# i think this is cald exceptions because it got to do with that 404 database exeption the one where you type try: query then
#                                                                                                                        exeption:


ma_yaseer = ['حمار']


def validate_title(value):
    if value in ma_yaseer:
        raise ValidationError(f"{value}: عيب")


def validate_body(value):
    if "زق" in value:
        raise ValidationError("not a good word")
