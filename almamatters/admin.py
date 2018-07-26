from django.contrib import admin

from almamatters.models import College, Footer, Student, Category, Course


class CollegeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'slug', 'website')


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'slug')


class CourseAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'slug', 'category')


class StudentAdmin(admin.ModelAdmin):
    search_fields = ('email',)
    list_display = ('name', 'email', 'mobile', 'student_category', 'course')

    def student_category(self, obj):
        return obj.course.category


admin.site.register(College, CollegeAdmin)
admin.site.register(Footer)
admin.site.register(Student, StudentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
