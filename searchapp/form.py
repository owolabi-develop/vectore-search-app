from django import forms





class PropertySearchForm(forms.Form):
    place = forms.CharField(max_length=255)
    PROPERTY_TYPES = [
        ('rent', 'rent'),
         ('buy', 'buy'),
          ('sold', 'sold'),
        ('apartment', 'Apartment'),
        ('land', 'Land'),
        # Add more property types as needed
    ]
    
    MIN_PRICE_RANGES = [
        (250, '250'),
        (500, '500'),
        (1000, '1,000'),
        (2500, '2,500'),
        (5000, '5,000'),
        (10000, '10,000'),
        (25000, '25,000'),
        (50000, '50,000'),
        (100000, '100,000'),
        (250000, '250,000'),
        (500000, '500,000'),
        (750000, '750,000'),
        (1000000, '1,000,000'),
    ]

    MAX_PRICE_RANGES = [
        (500000, '500,000'),
        (750000, '750,000'),
        (1000000, '1,000,000'),
        (2500000, '2,500,000'),
        (5000000, '5,000,000'),
    ]
    BEDROOM_CHOICES = [
        (1, '1 bedroom'),
        (2, '2 bedroom'),
        (3, '3 bedroom'),
        (4, '4 bedroom'),
        (5, '5 bedroom'),
    ]
    
    bathROOM_CHOICES = [
        (1, '1 '),
        (2, '2'),
        (3, '3'),
    ]
    price_min = forms.ChoiceField(label='MinPrice', choices=MIN_PRICE_RANGES, required=False)
    price_max = forms.ChoiceField(label='MaxPrice', choices=MAX_PRICE_RANGES, required=False)
    property_type = forms.ChoiceField(label='Property Type', choices=PROPERTY_TYPES, widget=forms.CheckboxInput, required=False)
    bedrooms = forms.ChoiceField(label='Bedrooms', choices=BEDROOM_CHOICES, required=False)
    bathrooms = forms.ChoiceField(label='Bathrooms', choices=bathROOM_CHOICES, required=False)
    # Add more fields as needed
    
    