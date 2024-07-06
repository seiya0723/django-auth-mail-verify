from django.shortcuts import render
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "bbs/index.html")
    def post(self, request, *args, **kwargs):
        return redirect("bbs:index")

index   = IndexView.as_view()
