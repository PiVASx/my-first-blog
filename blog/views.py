from django.shortcuts import render


# Create your views here.
def post_list(request):
    post_li = render(request, 'blog/post_list.html', {})
    return post_li