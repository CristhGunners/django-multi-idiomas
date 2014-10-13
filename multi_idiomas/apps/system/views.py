from django.shortcuts import render

from django.views.generic.base import TemplateView

from django.utils.translation import ugettext_lazy as _

class Home(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['title_es'] = _("Welcome to Github")
		return context