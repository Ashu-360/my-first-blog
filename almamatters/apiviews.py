# import json
#
# from rest_framework.serializers import Serializer
#
# from .models import INTERESTD_COURSE, COURSE_CATEGORY
# from rest_framework.views import APIView
# from rest_framework.response import Response
#
#
# class CategoryList(APIView):
#     def get(self, request):
#         category = COURSE_CATEGORY
#         categorydata = json.dumps(category)
#         # print "***********", categorydata
#         return Response(categorydata)
#
#
# class CourseList(APIView):
#     def get(self, request):
#         course = INTERESTD_COURSE
#         coursedata = json.dumps(course)
#         # print "***********", coursedata
#         return Response(coursedata)
#
#
#
#
