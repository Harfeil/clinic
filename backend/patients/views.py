from rest_framework.views import APIView
from .serializers import PatientSerializer
from django.http.response import JsonResponse
from .models import Patient
from django.http.response import Http404
from rest_framework.response import Response
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(r"E:\SCC notes\clinic\backend\clinic.json.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

class PatientView(APIView):

    def get_student(self, pk):
        try:
            patient = Patient.objects.get(studentId=pk)
            return student
        except:
            return JsonResponse("Student Does Not Exist", safe=False)

    def get(self, request, pk=None):
        if pk:
            data = self.get_student(pk)
            serializer = PatientSerializer(data)
           
        else:
            data = Patient.objects.all()
            serializer = PatientSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PatientSerializer(data=data)
        
        doc_ref = db.collection('patients').document()
        doc_ref.set(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Created Successfully", safe=False)
        return JsonResponse("Failed to Add Student", safe=False)

    def put(self, request, pk=None):
        student_to_update = Patient.objects.get(studentId=pk)
        data = request.data
        serializer = PatientSerializer(instance=student_to_update, data=request.data, partial=True)
        
        doc_ref = db.collection("patients").document("JYcZE3Ds6YeccmWMHPdk")
        doc_ref.update(data)
        # print(serializer)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Student")
   

    def delete(self, request, pk=None):
        student_to_delete = Patient.objects.get(studentId=pk)
        student_to_delete.delete()
        return JsonResponse("Student Deleted Successfully", safe=False)





