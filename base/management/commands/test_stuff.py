from django.core.management.base import BaseCommand
from django.db.models import F, Q, Case, ExpressionWrapper, FloatField, Value, When
from django.db.models.aggregates import Count
from base.models import Task
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        queryset = User.objects.annotate(total_tasks=Count('task', distinct=True),completed_tasks=Count('task', distinct=True, filter=Q(task__complete=True)),
                                         incomplete_tasks=Count('task', distinct=True, filter=Q(task__complete=False)),
                                         completion_percentage=Case(
                                            When(total_tasks=0, then=Value(0)),
                                            default=ExpressionWrapper(
                                            F('completed_tasks') / F('total_tasks') * 100,
                                            output_field=FloatField())
                                            )
                                        ).order_by('-total_tasks')
        
        for user in queryset:
            completion_percentage=(float(user.completed_tasks)/float(user.total_tasks))*100
            print(f'{user.username} \n tasks:\ntotal: {user.total_tasks}\ncompleted: {user.completed_tasks}\nincomplete: {user.incomplete_tasks}\n{completion_percentage}\n')
            
        print(queryset.query)