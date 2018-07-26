# from django import forms
#
# from almamatters.models import COURSE_CATEGORY, INTERESTD_COURSE
#
#
# class UserRegistrationForm(forms.Form):
#     username = forms.CharField(
#         required=True,
#         max_length=32,
#         label="Username"
#     )
#     email = forms.EmailField(
#         required=True,
#         label="Email",
#         max_length=40
#     )
#     mobile = forms.CharField(
#         required=True,
#         label="Mobile No"
#     )
#     category = forms.ChoiceField(
#         choices=COURSE_CATEGORY,
#         label="Course Category"
#     )
#     course = forms.ChoiceField(
#
#         choices=INTERESTD_COURSE,
#         label="Interested Course"
#     )
#
#
