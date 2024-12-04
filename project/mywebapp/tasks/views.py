from rest_framework import viewsets
from tasks.models import PlannedTask
from tasks.serializers import PlannedTaskSerializer


class PlannedTaskViewSet(viewsets.ModelViewSet):
    queryset = PlannedTask.objects.all()
    serializer_class = PlannedTaskSerializer

    def get_queryset(self):
        status = self.request.GET.get('status')
        if status == 'completed': 
            return super().get_queryset().filter(completed=True)
        elif status == 'incomplete':
            return super().get_queryset().filter(completed=False)
        return super().get_queryset()