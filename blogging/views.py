from django.http.response import HttpResponse, Http404
from blogging.models import Post
from django.template import loader
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.syndication.views import Feed
from django.urls import reverse


class BlogListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    context_object_name = "posts"
    template_name = "blogging/list.html"


class BlogDetailView(DetailView):
    # queryset = Post.objects.exclude(published_date__exact=None)
    context_object_name = "post"
    template_name = "blogging/detail.html"

    def get_queryset(self):
        self.post = get_object_or_404(
            Post, pk=self.kwargs["pk"]
        )  # self.post is a model object, based on the subsequent query (pk = xxx)
        return Post.objects.exclude(published_date__exact=None).filter(pk=self.post.pk)


class LatestEntriesFeed(Feed):
    title = "My Cool Blog"
    link = "/feed/"
    description = "Updates on changes and additions to My Cool Blog."

    def items(self):
        return Post.objects.exclude(published_date__exact=None).order_by(
            "published_date"
        )[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse("blog_detail", args=[item.pk])
