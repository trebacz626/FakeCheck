from django.core.exceptions import ValidationError


def validate_curse_pl(value):
    if ("dupa" or "chuj" or "kutas" or "jebać" or "twoja stara" or "rucham" or "kurwa" or "jebac") in value.lower():
        raise ValidationError('Niepoprawne słownictwo.')
    return value
