from django.urls import path
from .views import first_view,second_view,three_view,four_view,five_view

urlpatterns =  [
    path('', first_view, name = 'first-view'),
    path('second_view', second_view, name = 'second-view'),
    path('three_view', three_view, name='three-view'),
    path('four_view', four_view, name='three-view'),
    path('five_view', five_view, name='five-view'),
]
