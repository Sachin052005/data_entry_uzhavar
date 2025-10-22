from django import forms
from .models import Farmer

# Define the common widgets dictionary for all fields except 'employee'
COMMON_WIDGETS = {
    'name': forms.TextInput(attrs={'placeholder': 'Enter farmer name'}),
    'village': forms.TextInput(attrs={'placeholder': 'Enter village name'}),
    'phone': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
    'crop': forms.TextInput(attrs={'placeholder': 'Enter crop name'}),
    
    # Area field is set to TextInput as requested
    'area': forms.TextInput(attrs={'placeholder': 'Area in acres'}), 
    
    'location': forms.TextInput(attrs={'placeholder': 'Click fetch location button', 'id': 'id_location'}),
    
    # Checkbox fields (Farmer Needs)
    'seed': forms.CheckboxInput(), 
    'pesticide': forms.CheckboxInput(), 
    'fertilizer': forms.CheckboxInput(), 
    'drip': forms.CheckboxInput(),
    'machinery': forms.CheckboxInput(), 
    'nursery': forms.CheckboxInput(), 
    'sprayer': forms.CheckboxInput(),
    
    # Widget for the new today_date field
    'today_date': forms.DateInput(attrs={'type': 'date', 'id': 'id_today_date'}, format='%Y-%m-%d'),

    # Date and Textarea fields
    'next_visit': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    'others': forms.Textarea(attrs={'placeholder': 'Enter additional details (optional)', 'rows': 3}),
}


# 1. Form for Record CREATION (used by farmer_entry view)
# This form MUST include all fields, including 'employee' and 'today_date'.
class FarmerCreateForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = [
            'employee', # Must be the first field in creation
            'name', 
            'village', 
            'phone',
            'today_date', # <-- ADDED for creation
            'crop', 
            'area',
            'seed', 'pesticide', 'fertilizer', 'drip', 'machinery',
            'nursery', 'sprayer', 
            'location', 
            'next_visit', 
            'others',
        ]
        
        # Start with common widgets and add the employee widget
        widgets = COMMON_WIDGETS.copy()
        widgets['employee'] = forms.Select(attrs={'placeholder': 'Select Employee'})


# 2. Form for Record EDITING (used by edit_record view)
# This form EXCLUDES the 'employee' and 'today_date' fields.
class FarmerEditForm(forms.ModelForm):
    class Meta:
        model = Farmer
        # Use exclude to omit the employee and today_date fields, keeping all others
        exclude = ['employee', 'today_date'] # <-- 'today_date' ADDED to exclusion list
        
        # All other widgets are defined in COMMON_WIDGETS
        widgets = COMMON_WIDGETS
