from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import get_all_authors, get_author, author_form, delete_author, AuthorView


router = SimpleRouter()

router.register('api/authors', AuthorView)

urlpatterns = [
	path('', get_all_authors, name="get_all_authors"),
	path('new_author', author_form, name="new_author"),
	path('<int:id>', get_author, name="get_author"),
	path('delete_author/<int:id>', delete_author, name="delete_author"),
	path('edit_author/<int:id>', author_form, name="edit_author"),
]

urlpatterns += router.urls
