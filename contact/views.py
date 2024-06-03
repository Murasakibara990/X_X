from rest_framework import generics
from .models import Contact, ContactInfo
from .serializer import ContactSerializer, ContactInfoSerializer


class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactInfoApiView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
