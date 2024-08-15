from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'limit'
    max_page_size = 10

class OffsetPagination(LimitOffsetPagination):
    default_limit=1
    limit_query_param='limit'
    offset_query_param = 'offset'