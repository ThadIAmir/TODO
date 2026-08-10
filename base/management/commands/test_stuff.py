from django.core.management.base import BaseCommand
from base.models import Task
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        queryset = User.objects.all().prefetch_related('task_set')
        for user in queryset:
            print(f'{user.username} \n tasks:{user.task_set.all()}')
            
        print(queryset.query)