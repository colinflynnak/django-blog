from django.http.response import HttpResponse, Http404
from blogging.models import Post
from django.template import loader
from django.shortcuts import render


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs: \n"
        body += "\n".join(["\t%s: %s" % k for k in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


class ListView():
    def as_view(self):
        return self.get

    def get(self, request):
        model_list_name = self.model.__name__.lower() + '_list'
        context = {model_list_name: self.model.objects.all()}
        return render(request, self.template_name, context)


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date') # "-" Reverses order, most recent first
    template = loader.get_template('blogging/list.html')
    context = {'posts': posts}
    body = template.render(context)
    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)

