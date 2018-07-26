from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from almamatters import forms
from almamatters.models import College, Footer, Student, Category, Course


class FooterLinksView(TemplateView):
    template_name = 'almamatters/footer.html'
    links = Footer.objects.all()

    def get_context_data(self, **kwargs):
        context = super(FooterLinksView, self).get_context_data(**kwargs)
        context.update({'links': self.links})
        return context


class CollegeListing(TemplateView):
    template_name = 'almamatters/listing.html'

    def get_context_data(self, **kwargs):
        context = super(CollegeListing, self).get_context_data(**kwargs)
        context.update({'colleges': College.objects.all()})
        return context


class CollegePage(CollegeListing):
    template_name = 'almamatters/collegepage.html'

    def get_context_data(self, **kwargs):
        context = super(CollegePage, self).get_context_data(**kwargs)
        college = College.objects.get(slug=kwargs.get('slug'))
        context.update({'college': college})
        return context

    # def clg_search(self, context):
    #     pass
    #     search = context.objects.filter(name  = )


class HomePage(TemplateView):
    pass


@method_decorator(csrf_exempt, name='dispatch')
class UserLogin(TemplateView):
    template_name = 'registration/login.html'

    def post(self, request, *args, **kwargs):
        userobj = None
        if request.method == "POST":
            uname = request.POST.get('username')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            course_name = request.POST.get('course')
            print request.POST

            course = Course.objects.filter(name=course_name)[0]

            userobj = Student.objects.create(name=uname,
                                             email=email,
                                             mobile=mobile,
                                             course=course)

        return render(request, "registration/login.html", {'user': userobj,
                                                           'category': Category.objects.all(),
                                                           'course': Course.objects.all()})

    def get(self, request, *args, **kwargs):
        return render(request, "registration/login.html", {'category': Category.objects.all(),
                                                           'course': Course.objects.all()})









