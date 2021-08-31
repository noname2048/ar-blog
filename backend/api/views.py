from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from taggit.models import Tag

from api.views_utill import obj_to_post, prev_next_post, make_tag_cloud
from blog.models import Post


class ApiPostLV(BaseListView):
    # model = Post

    def get_queryset(self):
        tagname = self.request.GET.get("tagname")
        if tagname:
            qs = Post.objects.filter(tags__name=tagname)
        else:
            qs = Post.objects.all()
        return qs

    def render_to_response(self, context, **response_kwargs):
        qs = context["object_list"]
        post_list = [obj_to_post(obj) for obj in qs]
        return JsonResponse(data=post_list, safe=False, status=200)


class ApiPostDV(BaseDetailView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        obj = context["object"]
        post = obj_to_post(obj)
        post["prev"], post["next"] = prev_next_post(obj)
        return JsonResponse(data=post, safe=True, status=200)


class ApiTagCloudLV(BaseListView):
    queryset = Tag.objects.annotate(count=Count("post"))

    def render_to_response(self, context, **response_kwargs):
        qs = context["object_list"]
        tag_list = make_tag_cloud(qs)
        return JsonResponse(data=tag_list, safe=False, status=200)
