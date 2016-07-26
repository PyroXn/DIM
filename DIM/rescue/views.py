from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .models import Patient, Address

class IndexView(generic.ListView):
    template_name = 'rescue/index.html'
    context_object_name = 'latest_patient_list'

    def get_queryset(self):
        """Return the last five patient."""
        return Patient.objects.order_by('-adm_date')[:5]


class PatientView(generic.DetailView):
    model = Patient
    template_name = 'rescue/patient.html'


class AddressView(generic.DetailView):
    model = Address
    template_name = 'result/address.html'



class PatientList(generic.ListView):
    model = Patient


class PatientDetail(generic.DetailView):
    model = Patient


class PatientCreate(generic.CreateView):
    model = Patient
    fields = ['name', 'adm_date', 'address']

class PatientUpdate(generic.UpdateView):
    model = Patient
    fields = ['name', 'adm_date', 'address']


class PatientDelete(generic.DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_list')