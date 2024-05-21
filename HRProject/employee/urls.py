from django.urls import path


from employee.views import EmployeeListCreate, EmployeeModifyRetrieveDelete, DepartmentListCreate, \
    DepartmentModifyRetrieveDelete

urlpatterns = [
    path('employee/', EmployeeListCreate.as_view(), name='all_employee'),
    path('employee/<int:pk>/', EmployeeModifyRetrieveDelete.as_view(), name='one_employee_modification'),
    path('department/', DepartmentListCreate.as_view(), name='department'),
    path('department/<int:pk>/', DepartmentModifyRetrieveDelete.as_view(), name='department'),

]
