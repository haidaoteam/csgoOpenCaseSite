import json
import logging

from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView, RedirectView

from box.models import Case, AssetItem

_logger = logging.getLogger(__name__)


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


home_page = HomePageView.as_view()
