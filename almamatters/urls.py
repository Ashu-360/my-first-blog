from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# from almamatters.apiviews import CategoryList, CourseList
from almamatters.views import CollegeListing, CollegePage, HomePage, UserLogin
from django.conf import settings

urlpatterns = [
    url('^home/$', HomePage.as_view(), name='home_page'),

    url(r'^colleges/$', CollegeListing.as_view(), name='college_listing'),
    url(r'^college/(?P<slug>[\w-]+)/$', CollegePage.as_view(), name='college_page'),

    url(r'register/$', UserLogin.as_view(), name='user_login'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    # url("catlist/", CategoryList.as_view(), name="category_list"),
    # url("coulist/", CourseList.as_view(), name="course_list"),
]
