from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MedicineSerializer
from .models import Medicine


# from django.http import JsonResponse

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/home_medicine_server/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of medicine'
        },
        {
            'Endpoint': '/home_medicine_server/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single medicine object'
        }
    ]
    return Response(routes)


@api_view(['GET'])
def getMedicines(request):
    medicines = Medicine.objects.all()
    serializer = MedicineSerializer(medicines, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMedicine(request, pk):
    medicine = Medicine.objects.get(id=pk)
    serializer = MedicineSerializer(medicine, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createMedicine(request):
    data = request.data

    medicine = Medicine.objects.create(
        body=data['body']
    )
    serializer = MedicineSerializer(medicine, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateMedicine(request, pk):
    data = request.data

    medicine = Medicine.objects.get(id=pk)
    serializer = MedicineSerializer(medicine, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteMedicine(request, pk):
    medicine = Medicine.objects.get(id=pk)
    medicine.delete()
    return Response('Medicine was deleted')
