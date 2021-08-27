from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.list import BaseListView

from api.views_utill import obj_to_post
from blog.models import Post


class ApiPostLV(BaseListView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        qs = context["object_list"]
        post_list = [obj_to_post(obj) for obj in qs]
        return JsonResponse(data=post_list, safe=False, status=200)
