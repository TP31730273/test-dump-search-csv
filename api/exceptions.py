from rest_framework.exceptions import APIException

class QueryParmNotValidException(APIException):
    status_code = 400
    default_detail = 'Query Param Not valid, try again later.'
    default_code = 'service_unavailable'