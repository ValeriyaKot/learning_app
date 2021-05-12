import factory
from apps.courses.models import Course, Module, Material
from apps.users.tests.conftest import ProfileFactory


class CourseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Course

    id = 1
    teacher = factory.SubFactory(ProfileFactory, course=None)
    title = 'Course N1'


class ModuleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Module

    id = 1
    title = 'Module N1'
    course = factory.SubFactory(CourseFactory, module=None, factory_related_name='module')


class MaterialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Material

    id = 1
    text = 'Elephant fish sweeper freshwater hatchet fish trench queen trigger fish molly Chinook salmon.'
    module = factory.SubFactory(ModuleFactory, module=None)
