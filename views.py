from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from kleiner_specht.models import Releases, Members
from kleiner_specht.forms import ReleaseInput
from django.views import View


class IndexPage(TemplateView):
    template_name = 'index.html'

class ContactsPage(TemplateView):
    template_name = 'contacts.html'

class ReleasesView(ListView):
    template_name = 'releases.html'
    model = Releases
    context_object_name = 'releases_view'
    queryset = Releases.objects.all()

class MembersView(ListView):
    template_name = 'about.html'
    model = Members
    context_object_name = 'models_view'
    queryset = Members.objects.all()

class InputRelease(View):
    template_name = 'add-release.html'
    def get(self, request):
        form = ReleaseInput
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = ReleaseInput(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/releases.html')