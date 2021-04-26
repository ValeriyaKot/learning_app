import pytest
import factory
from apps.courses.models import Course, Module, Material
from apps.users.tests.conftest import ProfileFactory


class CourseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Course

    id = 1
    teacher = factory.SubFactory(ProfileFactory, course=None)
    title = 'Course N1'
    # module = factory.SubFactory('apps.courses.tests.conftest.CourseFactory', course=None)


class ModuleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Module

    id = 1
    title = 'Module N1'
    description = 'Elephant fish sweeper freshwater hatchet fish'
    course = factory.SubFactory(CourseFactory, module=None, factory_related_name='module')
    # material = factory.SubFactory('apps.users.MaterialFactory', module=None)


class MaterialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Material

    id = 1
    text = 'Elephant fish sweeper freshwater hatchet fish trench queen trigger fish molly Chinook salmon.'
    module = factory.SubFactory(ModuleFactory, module=None)
