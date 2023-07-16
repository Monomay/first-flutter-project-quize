from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Exam
from .serializers import ExamSerializer
from rest_framework import status


@api_view(['GET'])
def ExamList(request):

    if request.method == 'GET':
        exam = Exam.objects.all()
        serializer = ExamSerializer(exam, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = ExamSerializer(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)





        
    
