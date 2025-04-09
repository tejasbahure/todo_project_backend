from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ToDo
from .serializers import ToDoSerializer

@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.method == 'GET':
        todos = ToDo.objects.all().order_by('-created_at')
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, pk):
    try:
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def todo_clear_all(request):
    ToDo.objects.all().delete()
    return Response({"message": "All tasks deleted."}, status=status.HTTP_204_NO_CONTENT)
