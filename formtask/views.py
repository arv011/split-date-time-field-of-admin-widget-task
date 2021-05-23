from django.shortcuts import render,redirect,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Incidentmodelform,CustomUserCreationform
# Create your views here.
class Signupview(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationform

    def get_success_url(self):
        return reverse("login")

class homeview(generic.TemplateView):
    template_name = 'home.html'

# class createformview(LoginRequiredMixin,generic.CreateView):
#     template_name = 'form.html'
#     form_class = Incidentmodelform

#     def get_context_data(self,**kwargs):
#         context = super(createformview, self).get_context_data(**kwargs)
#         name = self.request.user.username
#         context.update({
#             'name':name
#         })
#         return context
#     def get_success_url(self):
#         return redirect("Home")
#     def form_valid(self, form):
#         inc = form.save(commit=False)
#         inc.reported_by = self.request.user.username
#         form.save()
        
#         return super(createformview, self).form_valid(form)

def createform(request):

    if request.user.is_authenticated:
        name = request.user.username
        form = Incidentmodelform()
        

        rem = {'form':form,'name':name}
        if request.method == 'POST':
            form = Incidentmodelform(request.POST)
            
            if form.is_valid():
                inc = form.save(commit=False)
                inc.reported_by = name
                form.save()
                return redirect("Home")

        return render(request, 'form.html', rem)
    
    