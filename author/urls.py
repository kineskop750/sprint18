from django.urls import path
from . import views

urlpatterns = [
	# Домашняя страница
	path('',views.get_all_authors,name="get_all_authors"),
	path('new_author',views.new_author,name="new_author"),
	path('<int:id>',views.get_author,name="get_author"),
	path('delete_author/<int:id>',views.delete_author,name="delete_author"),
	path('edit_author/<int:id>',views.edit_author,name="edit_author")
]