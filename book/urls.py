from django.urls import path
from . import views
urlpatterns = [
	path('',views.get_all_books,name='get_all_books'),
	path('new_book',views.new_book,name="new_book"),
	path('<int:id>',views.get_book,name="get_book"),
	path('delete_book/<int:id>',views.delete_book,name="delete_book"),
	path('edit_book/<int:id>',views.edit_book,name="edit_book")
]