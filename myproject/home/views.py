from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Farmer
# IMPORT BOTH FORMS
from .forms import FarmerCreateForm, FarmerEditForm 

def farmer_entry(request):
    success = False
    # Use FarmerCreateForm for entry
    if request.method == 'POST':
        form = FarmerCreateForm(request.POST) 
        if form.is_valid():
            form.save()
            success = True
            form = FarmerCreateForm()   # reset form
    else:
        form = FarmerCreateForm()
    return render(request, 'home/farmer_entry.html', {'form': form, 'success': success})


def edit_record(request, id):
    record = get_object_or_404(Farmer, id=id) 

    if request.method == 'POST':
        # Use FarmerEditForm for updating
        form = FarmerEditForm(request.POST, instance=record) 
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Farmer record updated successfully!")
            return redirect('view_records')  
        else:
            messages.error(request, "❌ Error updating record. Please check the highlighted fields.")
    else:
        # Use FarmerEditForm for displaying
        form = FarmerEditForm(instance=record)

    return render(request, 'home/edit_record.html', {
        'form': form,
    })

def view_records(request):
    # Displays all records
    records = Farmer.objects.all()
    return render(request, 'home/view_records.html', {'records': records})



def delete_record(request, id):
    # Deletes the record
    record = get_object_or_404(Farmer, id=id)
    record.delete()
    messages.success(request, f"Farmer record for {record.name} deleted.")
    return redirect('view_records')

# app/views.py 
import csv
from django.http import HttpResponse
from .models import Farmer 

# Define a function to convert boolean to Yes/No
def boolean_to_yes_no(value):
    if value is True:
        return 'Yes'
    return 'No' # Handles False and None cases

def download_records_excel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="farmer_records.csv"'

    field_names = [
        'Employee ID', 'Name', 'Village', 'Phone', 'Date', 'Crop', 'Area', # <-- 'Date' ADDED
        'Seed', 'Pesticide', 'Fertilizer', 'Drip', 'Machinery',
        'Nursery', 'Sprayer', 'Next Visit Date', 'Others', 'Location'
    ]
    
    writer = csv.writer(response)
    writer.writerow(field_names)

    # Note: The checkbox fields (Seed to Sprayer) are now indices 7 through 13.
    
    # Use values_list to get raw data
    records_query = Farmer.objects.all().values_list(
        'employee',     # 0
        'name',         # 1
        'village',      # 2
        'phone',        # 3
        'today_date',   # 4 (NEW FIELD)
        'crop',         # 5
        'area',         # 6
        'seed',         # 7 (Boolean)
        'pesticide',    # 8 (Boolean)
        'fertilizer',   # 9 (Boolean)
        'drip',         # 10 (Boolean)
        'machinery',    # 11 (Boolean)
        'nursery',      # 12 (Boolean)
        'sprayer',      # 13 (Boolean)
        'next_visit',   # 14 (Date)
        'others',       # 15
        'location'      # 16
    )
    
    for record_tuple in records_query:
        # Convert the tuple to a mutable list for easy processing
        row = list(record_tuple)
        
        # Process Boolean fields (Indices 7 through 13) - The indices shifted due to the new field
        for i in range(7, 14):
            row[i] = boolean_to_yes_no(row[i])
            
        # Process all fields, ensuring None, Dates, and other objects are properly converted to strings
        final_row = [str(item) if item is not None else '' for item in row]
        writer.writerow(final_row)

    return response
