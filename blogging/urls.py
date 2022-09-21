from django.urls import path
from blogging.views import BlogListView, BlogDetailView, LatestEntriesFeed


urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("feed/", LatestEntriesFeed()),
]
