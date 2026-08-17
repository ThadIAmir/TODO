from django.core.management.base import BaseCommand
from django.db.models import F, Q, Case, Exists, ExpressionWrapper, FloatField, OuterRef, Subquery, Value, When
from django.db.models.lookups import GreaterThanOrEqual
from django.db.models.aggregates import Avg, Count
from base.models import Task
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Day1 - annotate/Count/Case-When/ExpressionWrapper/F/
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
        #     print(f'{user.username} \n tasks:\ntotal: {user.total_tasks}\ncompleted: {user.completed_tasks}\nincomplete: {user.incomplete_tasks}\n{completion_percentage}\n')
            
        # print(queryset.query)
        
        # ------------------------------------------------------------------------------------------
        
        #Day2 - Q
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
        
        # queryset = Room.objects.annotate(
        #     message_count=Count('messages'), 
        #     active_message_count=Count('messages', filter=
        #                                Q(messages__content__icontains='django') 
        #                                | Q(messages__content__icontains='python')
        #                                ),
        #     reaction_count=Count('messages__reactions', distinct=True)
        #     ).filter(Q(active_message_count__gt=0) | Q(reaction_count__gt=5)
        #              ).order_by('-message_count', '-reaction_count')
        
        # ------------------------------------------------------------------------------------------
        
        #Day3 - Subquery/OuterRef
        # latest_message_time = (
        #     Message.objects
        #     .filter(sender=OuterRef('pk'))
        #     .order_by('-created_at')
        #     .values('created_time')[:1]
        # )

        # users = User.objects.annotate(
        #     last_message_time=Subquery(latest_message_time)
        # )
        
        # last_message = Message.objects.filter(sender=OuterRef('pk')
        #                                       ).order_by('-created_at')[:1]        
        
        # users = User.objects.annotate(
        #     message_count = Count('messages'),
        #     last_message_time = Subquery(last_message.values('created_at')),
        #     last_message_content = Subquery(last_message.values('content')),
        #     last_message_room_name = Subquery(last_message.values('room__name')),
        # ).filter(message_count__gte=3
        #     ).order_by('-last_message_time')
        
        # ------------------------------------------------------------------------------------------
        
        # Day4 - Exists/~Exists
        # Tasks1 = Task.objects.filter((Q(title__icontains='django') | Q(description__icontains='django')) & Q(complete=False), user=OuterRef('pk'))
        # Tasks2 = Task.objects.filter((Q(title__icontains='python') | Q(description__icontains='python')) & Q(complete=True), user=OuterRef('pk'))
        # users = User.objects.filter(Q(Exists(Tasks1)) & Q(~Exists(Tasks2)))
        
        # incomplete_tasks = Task.objects.filter(complete=False, user=OuterRef('pk'))
        # users = User.objects.annotate(has_incomplete_tasks=Exists(incomplete_tasks))
        # # print(users.query)
        # for user in users:
        #     print(f'{user.username} : has_incomplete_tasks? {user.has_incomplete_tasks}')
        
        # last_message = Message.objects.filter(room=OuterRef('id')).order_by('-created_at')[:1]        
        # python_messages = Messaage.objects.filter(content__icontains='python', room=OuterRef('id'))
        # Rooms = Room.objects.annotate(
        #     message_count = Count('messages'),
        #     last_message_content = Subquery(last_message.values('content')),
        #     has_python_message = Exists(python_messages)
        # ).filter(message_count__gte=10
        #     ).order_by('-message_count')
        
        # ------------------------------------------------------------------------------------------
        
        # Day5 - F/Avg
        # Task.objects.filter(GreaterThanOrEqual( F('actual_minutes'), F('estimated_minutes') * 2 ) )
        # also we could do it like this too: 
        # Task.objects.filter(actual_minutes__gte=F('estimated_minutes') * 2 )
        
        # Task.objects.annotate(time_difference=F('actual_minutes') - F('estimated_minutes'))
        
        # avg_minutes = Task.objects.filter(user=OuterRef('pk')
        #                             ).values('user'
        #                                 ).annotate(diff=F('actual_minutes') - F('estimated_minutes')
        #                                     ).annotate(avg_mins=Avg('diff')
        #                                             ).values('avg_mins')
        # avg_minutes = (
        #     Task.objects
        #     .filter(user=OuterRef('pk'))
        #     .values('user')
        #     .annotate(
        #         avg_mins=Avg(
        #             F('actual_minutes') - F('estimated_minutes')
        #         )
        #     )
        #     .values('avg_mins')
        # )
        # users= User.objects.annotate(avg_minutes=Subquery(avg_minutes))
        
        
        
        