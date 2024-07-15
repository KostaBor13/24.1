from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson
from materials.validators import UrlValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='url')]


class CourseSerializer(ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscriptions = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        """ Возвращает количество уроков в курсе. """
        return instance.lesson_set.count()

    def get_subscriptions(self, obj):
        """ Возвращает статус подписки пользователя на курс. """
        request = self.context.get('request')
        user = request.user
        if obj.subscription_set.filter(user=user, is_subscribed=True):
            return 'подписка оформлена'
        else:
            return 'подписка отсутствует'
  