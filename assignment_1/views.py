from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import form_data


# from assignment_1.forms import MyForm

@csrf_exempt
def form_handle(request):
    # print "********************* :", request.POST.get('firstname')
    # print "********************* :", request.POST.get('lastname')
    # print "********************* :", request.POST.get('email')

    # form = MyForm()
    user_obj = None
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')

        user_obj = form_data.objects.create(userfirstname=fname,
                                            userlastname=lname,
                                            useremail=email)

        # import pdb;pdb.set_trace()
        # form = MyForm(request.POST)

        # if form.is_valid():
        #     cd = form.cleaned_data
        #     # first = cd.get('firstname')
        #     # last = cd.get('lastname')
        #     # email = cd.get('email')
        #     # obj=ModelClass(**cd)
        #     # obj.save()
        #

    return render(request, "assignment_1/form_assign.html", {'user': user_obj})
