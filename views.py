from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def student_api(request, id=None):
    if request.method == 'GET':
        if id is not None:
            student = get_object_or_404(Student, id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        if isinstance(data, list):
            serializer = StudentSerializer(data=data, many=True)
        else:
            serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'PATCH':
        result = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})

    elif request.method == 'DELETE':
        result = get_object_or_404(Student, id=id)
        result.delete()
        return Response({"status": "success", "data": "Record deleted"})

