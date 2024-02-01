"""views for myapp."""

from rest_framework.response import Response
from myapp.serializers import *
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import *
from rest_framework import status




class StudentClass():

    @api_view(['POST'])
    def add_student(request):
        student_serializer = StudentCreateSerializer(data=request.data)

        if student_serializer.is_valid():
            instance = student_serializer.save()

            profile_data  = request.data.get('profile')
            
            if profile_data:
                print('in profile data')
                profile_data['student'] = instance.id
                profile_serializer = StudentProfileSerializer(data=profile_data)
                if profile_serializer.is_valid():
                    profile_serializer.save()
                else:
                    # Handle the case where profile creation fails
                    print('in delete')
                    instance.delete()
                    return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            return Response(student_serializer.data)
        return Response(student_serializer.errors)


    @api_view(['GET'])
    def list_students(request):
        queryset = Student.objects.all()
        serializer = StudentRetrieveSerializer(queryset, many=True)

        return Response(serializer.data)
    


    @api_view(['PATCH'])
    def update_student(request, id):
        queryset = Student.objects.get(id=id)
        serializer = StudentUpdateSerializer(queryset, data=request.data, partial=True)

        if serializer.is_valid():
            instance = serializer.save()

            # profile_data = request.data.get('profile')

            # if profile_data:
            #     # Check if the profile already exists
            #     try:
            #         print('profile_data = ', profile_data)
            #         profile = instance.profile
            #     except StudentProfile.DoesNotExist:
            #         profile_data['student'] = instance
            #         profile_serializer = StudentProfileSerializer(data=profile_data)
            #     else:
            #         profile_serializer = StudentProfileSerializer(profile, data=profile_data, partial=True)


            #     if profile_serializer.is_valid():
            #         profile_serializer.save()
            #     else:
            #         return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data)
        return Response(serializer.errors)



# class StudentViews(viewsets.ModelViewSet):
#     queryset = Student.objects.all()

#     def get_serializer_class(self):
#         if self.action in ['create', 'update', 'partial_update']:
#             return StudentCreateSerializer
#         else:
#             return StudentRetrieveSerializer
        

#     def perform_create(self, serializer):
#         # Override perform_create to create associated StudentProfile
#         instance = serializer.save()

#         # Assuming your StudentCreateSerializer has a nested profile field
#         profile_data = self.request.data.get('profile')
#         print("profile", profile_data)
#         if profile_data:
#             profile_data['student'] = instance.id
#             print('aaa', profile_data)
#             profile_serializer = StudentProfileSerializer(data=profile_data)
#             if profile_serializer.is_valid():
#                 profile_serializer.save()
#             else:
#                 # Handle the case where profile creation fails
#                 instance.delete()
#                 return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         return instance
    
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         # Update associated profile
#         profile_data = request.data.get('profile')
#         if profile_data:
#             profile_serializer = StudentProfileSerializer(instance.profile, data=profile_data, partial=partial)
#             if profile_serializer.is_valid():
#                 profile_serializer.save()
#             else:
#                 return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         return Response(serializer.data)




class StudentProfileViews(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

class TeacherViews(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SubjectViews(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer








