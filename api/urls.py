from django.urls import include,path
from . import views 

urlpatterns=[
	path('welcome',views.welcome),
	path('addbooks',views.add_book),
	path('updatebook/<int:book_id>',views.update_book),
	path('deletebook/<int:book_id>',views.delete_book)
    
]