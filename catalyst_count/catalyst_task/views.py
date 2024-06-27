from django.shortcuts import render,redirect
from allauth.account.views import LoginView,SignupView,LogoutView
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MyFileSerializer
import gc
from django.db import transaction
from rest_framework.pagination import PageNumberPagination

# Create your views here.
def create_db(file_path):
    df = pd.read_csv(file_path, delimiter=',', encoding='utf-8')
    list_csv = [list(row) for row in df.values]

    objects_to_create = [
        CSVData(
            Emp_id=i[0],
            name=i[1],
            domain=i[2],
            year=i[3],
            industry=i[4],
            size=i[5],
            area=i[6],
        ) for i in list_csv
    ]

    # Use transaction and bulk_create for faster insertions
    with transaction.atomic():
        CSVData.objects.bulk_create(objects_to_create)
            

        
@login_required
def main(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            file_instance = File.objects.create(file=uploaded_file)
            create_db(file_instance.file.path)
            return redirect('filter')
    else:
        form = UploadFileForm()

    context = {'form': form}
    return render(request, 'upload.html', context)

@login_required
@api_view(['GET'])
def filter_view(request):
    if request.method == 'GET':
        filtered_data = CSVData.objects.all()
        # Get filter parameters from GET request
        filters = {
            'Emp_id': request.GET.get('emp_id'),
            'name': request.GET.get('name'),
            'year': request.GET.get('year'),
            'domain': request.GET.get('domain'),
            'industry': request.GET.get('industry'),
            'size': request.GET.get('size'),
            'area': request.GET.get('area'),
        }

        # Filter out None or empty values
        filters = {k: v for k, v in filters.items() if v}

        # Filter the CSVData based on the cleaned filters
        filtered_data = filtered_data.filter(**filters)

        context = {
            'filtered_data': filtered_data,
        }

        return render(request, 'filter.html', context)

    # Handle other request methods (if any)
    return render(request, 'filter.html')

@login_required
@api_view(['GET'])
def filter_api(request):
    filters = {
        'Emp_id': request.GET.get('emp_id'),
        'name': request.GET.get('name'),
        'year': request.GET.get('year'),
        'domain': request.GET.get('domain'),
        'industry': request.GET.get('industry'),
        'size': request.GET.get('size'),
        'area': request.GET.get('area'),
    }

    filters = {k: v for k, v in filters.items() if v}

    if filters:
        filtered_data = CSVData.objects.filter(**filters)
    else:
        filtered_data = CSVData.objects.all()

    paginator = PageNumberPagination()
    paginated_data = paginator.paginate_queryset(filtered_data, request)

    serializer = MyFileSerializer(paginated_data, many=True)
    return paginator.get_paginated_response(serializer.data)
# Django RestFrameWork

@login_required
@api_view(['GET'])
def filter_api(request):
    filters = {
        'Emp_id': request.GET.get('emp_id'),
        'name': request.GET.get('name'),
        'year': request.GET.get('year'),
        'domain': request.GET.get('domain'),
        'industry': request.GET.get('industry'),
        'size': request.GET.get('size'),
        'area': request.GET.get('area'),
    }

    # Remove empty or None values from filters
    filters = {k: v for k, v in filters.items() if v}

    # Apply filters if there are any
    if filters:
        filtered_data = CSVData.objects.filter(**filters)
    else:
        filtered_data = CSVData.objects.all()

    # Serialize the filtered data
    serializer = MyFileSerializer(filtered_data, many=True)
    return Response(serializer.data)





class CustomLoginView(LoginView):
    template_name = 'login.html'  # Replace with your custom login template
    
class CustomSignupView(SignupView):
        template_name = 'signup.html'
    
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'