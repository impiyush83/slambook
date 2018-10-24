from functools import wraps

from flask import request, jsonify

from utils.custom_exceptions import RequestValidationException


class Validator(cerberus_validator):

    def __init__(self, *args, **kwargs):
        if 'additional_context' in kwargs:
            self.additional_context = kwargs['additional_context']
        super(Validator, self).__init__(*args, **kwargs)

    def _validate_type_unicode(self, value):
        return True if type(value) is str else False

    def _validate_type_utc_date(self, value):
        date_value = parse_date(value)
        return True if date_value else False

    def _validate_type_gps_coordinates(self, value):
        gps_coordinates_value = parse_coordinates(value)
        return True if gps_coordinates_value else False

    def _validate_type_integer_string(self, value):
        integer_value = parse_int(value)
        return True if integer_value is not None else False

    def _validate_type_decimal_string(self, value):
        decimal_value = parse_decimal(value)
        return True if decimal_value is not None else False


def data_validator_restful(schema):
    def decorator(func):
        @wraps(func)
        def validate(*args, **kwargs):
            validator = Validator(schema)
            if validator.validate(request.safe_json):
                return func(*args, **kwargs)
            else:
                raise RequestValidationException(jsonify(validator.errors))

        return validate

    return decorator
