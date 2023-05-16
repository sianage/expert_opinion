from django.urls import path
from . import views
from .views import Econ_Blog, AddEntryView, ArticleDetailView, EditPostView, DeletePostView, CategoryView, Polisci_Blog, \
    Philosophy_Blog, Medicine_Blog, index, DebatesView

urlpatterns = [
    #path("", views.index, name="index"),
    path("", index.as_view(), name="index"),
    path("econ_blog/", Econ_Blog.as_view(), name="econ_blog"),
    path("polisci_blog/", Polisci_Blog.as_view(), name="polisci_blog"),
    path("econ_blog/<int:id_author>", Econ_Blog.as_view(), name="econ_blog"),
    path("polisci_blog/<int:id_author>", Polisci_Blog.as_view(), name="polisci_blog"),
    path("philosophy_blog/", Philosophy_Blog.as_view(), name="philosophy_blog"),
    path("philosophy_blog/<int:id_author>", Philosophy_Blog.as_view(), name="philosophy_blog"),
    path("medicine_blog/", Medicine_Blog.as_view(), name="medicine_blog"),
    path("medicine_blog/<int:id_author>", Medicine_Blog.as_view(), name="medicine_blog"),
    path('article_details/<int:pk>', ArticleDetailView.as_view(), name="article_details"),
    path("add_entry/", AddEntryView.as_view(), name="add_entry"),
    path('article/edit/<int:pk>', EditPostView.as_view(), name="edit_post"),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cat>/', CategoryView, name='category'),
    path('debates/', DebatesView.as_view(), name="debates"),
]