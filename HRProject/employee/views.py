from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from employee.models import Employee, Department
from employee.serializer import EmployeeSerializer, DepartmentSerializer
from user.models import Notification
from user.permissions import IsHR
from employee.permission import IsHRorIsOwner

class EmployeeListCreate(ListCreateAPIView):
    queryset = Employee.objects.filter(is_deleted=False)
    serializer_class = EmployeeSerializer
    permission_classes = [IsHRorIsOwner]

    def list(self, request, *args, **kwargs):

        if request.user.role.role != 'hr':
            queryset = Employee.objects.filter(is_deleted=False, user=request.user)

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Employee.objects.filter(is_deleted=False)

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)


class EmployeeModifyRetrieveDelete(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.filter(is_deleted=False)
    serializer_class = EmployeeSerializer
    permission_classes = [IsHRorIsOwner]

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class DepartmentListCreate(ListCreateAPIView):
    queryset = Department.objects.filter(is_deleted=False)
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

class DepartmentModifyRetrieveDelete(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.filter(is_deleted=False)
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
