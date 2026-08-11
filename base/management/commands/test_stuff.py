from django.core.management.base import BaseCommand
from django.db.models import F, Q, Case, ExpressionWrapper, FloatField, Value, When
from django.db.models.aggregates import Count
from base.models import Task
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Day1
        # queryset = User.objects.annotate(total_tasks=Count('task', distinct=True),completed_tasks=Count('task', distinct=True, filter=Q(task__complete=True)),
        #                                  incomplete_tasks=Count('task', distinct=True, filter=Q(task__complete=False)),
        #                                  completion_percentage=Case(
        #                                     When(total_tasks=0, then=Value(0)),
        #                                     default=ExpressionWrapper(
        #                                     F('completed_tasks') / F('total_tasks') * 100,
        #                                     output_field=FloatField())
        #                                     )
        #                                 ).order_by('-total_tasks')
        
        # for user in queryset:
        #     completion_percentage=(float(user.completed_tasks)/float(user.total_tasks))*100
        #     print(f'{user.username} \n tasks:\ntotal: {user.total_tasks}\ncompleted: {user.completed_tasks}\nincomplete: {user.incomplete_tasks}\n{completion_percentage}\n')
            
        # print(queryset.query)
        
        #Day2
        # queryset = Task.objects.filter(Q(title__icontains='test') | Q(description__icontains='test') & Q(complete=False))
        # queryset = User.objects.annotate(total_tasks_count=Count('task'), 
        #                                  test_tasks_count=Count(
        #                                      'task', 
        #                                      filter=(Q(task__title__icontains='test')
        #                                             | Q(task__description__icontains='test')
        #                                             ) & 
        #                                             Q(task__complete=False)
        #                                     )
        #                                 ).filter(test_tasks_count__gt=0
        #                                          ).order_by('-total_tasks_count', '-test_tasks_count')
        # # print(len(queryset))
        # for user in queryset:
        #     print(f'Username: {user.username} \ntotal tasks count: {user.total_tasks_count} \ntest tasks count: {user.test_tasks_count} \n')
        # print(queryset.query)
        
        #Day3