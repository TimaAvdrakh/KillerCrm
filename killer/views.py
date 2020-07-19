from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import xml.etree.ElementTree as ET
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework_xml.parsers import XMLParser
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

# @login_required
class ContractCreate(APIView):
    parser_classes = (XMLParser,)

    def post(self, request):
        xml_data = request.body
        xml = str(xml_data, 'utf-8')
        # tree = ET.parse(xml)
        tree = ET.fromstring(xml)
        print(type(tree))
        for target in tree.findall('targets/target'):
            username = target.find('username').text
            age = int(target.find('age').text)
            priority = int(target.find('priority').text)
            difficulty = int(target.find('difficulty').text)
            link = target.find('link').text
            print([username, age, priority, difficulty,link])
        return Response({'root': tree.attrib})

