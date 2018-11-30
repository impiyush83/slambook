# import datetime
# from decimal import Decimal
#
# date_format = '%Y-%m-%d %H:%M:%S UTC'
#
#
# def parse_date(date_str, _format=date_format):
#     try:
#         if date_str is None:
#             return None
#         date_time = datetime.strptime(date_str, _format)
#     except ValueError:
#         return None
#     else:
#         return date_time
#
#
# def date_to_str(date):
#     return date and date.strftime(date_format)
#
#
# def parse_int(int_str):
#     try:
#         return int(int_str)
#     except ValueError:
#         return None
#     except TypeError:
#         return None
#
#
# def parse_float(float_str):
#     try:
#         return float(float_str)
#     except ValueError:
#         return None
#     except TypeError:
#         return None
#     except:
#         return None
#
#
# def parse_decimal(decimal_str):
#     try:
#         return Decimal(decimal_str)
#     except ValueError:
#         return None
#     except TypeError:
#         return None
#     except:
#         return None
