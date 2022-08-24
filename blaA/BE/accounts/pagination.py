from rest_framework import pagination


class CustomPageNumberPagination(pagination.PageNumberPagination) :
    
    page_size=10
    page_size_query_param='count'
    max_page_size=20
    page_query_param='page'
    
class CustomPagehundredNumberPagination(pagination.PageNumberPagination) :
    page_size = 100
    page_size_query_param='count'
    max_page_size=200
    page_query_param='page'