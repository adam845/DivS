from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contactus
from .serializers import ContactUsSerializer

@api_view(['GET'])
def contact_list(request):
    contacts = Contactus.objects.all()
    serializer = ContactUsSerializer(contacts, many=True)
    return Response(serializer.data)
