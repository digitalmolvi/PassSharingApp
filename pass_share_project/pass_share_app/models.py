from django.db import models
from django.utils import timezone # Import the timezone module
from datetime import datetime  # Import the datetime module



# Abstract Base Class for Common Fields
class CommonFields(models.Model):
    address = models.TextField(default='')  # Provide a default value
    city = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    postal_code = models.CharField(max_length=20, default='')
    # ... Other common fields

    class Meta:
        abstract = True

# Status Choices
STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('cancelled', 'Cancelled'),
    # ... Add more as needed
)

# Payment Status Choices
PAYMENT_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('success', 'Success'),
    ('failed', 'Failed'),
    # ... Add more as needed
)

# Verification Status Choices
VERIFICATION_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    # ... Add more as needed
)

class User(CommonFields):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=15)
    language_preference = models.CharField(max_length=10)
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    social_media_links = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    # ... Other fields

    def __str__(self):
        return self.email

class Property(CommonFields):
    property_name = models.CharField(max_length=255)
    property_image = models.ImageField(upload_to='property_images/')

    property_type = models.CharField(max_length=50)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    amenities = models.TextField()

    # ... Other fields

    def __str__(self):
        return self.property_name

class Compound(CommonFields):
    compound_name = models.CharField(max_length=255)
    compound_image = models.ImageField(upload_to='compound_images/')
    compound_location = models.CharField(max_length=255)
    
    description = models.TextField(default='')
    facilities = models.TextField(default='')
    security_level = models.CharField(max_length=50, default='')
    contact_email = models.EmailField(default='')  # Provide a default value
    contact_phone = models.CharField(max_length=20, default='')  # Provide a default value
    website = models.URLField(null=True, blank=True)
    social_media_links = models.TextField(null=True, blank=True)
    
    # ... Other fields

    def __str__(self):
        return self.compound_name

class PassType(models.Model):
    compound = models.ForeignKey(Compound, on_delete=models.CASCADE)
    passtype_name = models.CharField(max_length=255)
    passtype_price = models.DecimalField(max_digits=10, decimal_places=2)
    geo_restricted = models.BooleanField(default=False)
    
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    duration = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()
    special_conditions = models.TextField()
    is_active = models.BooleanField(default=True)

    # ... Other fields

    def __str__(self):
        return self.passtype_name

class PassRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    compound = models.ForeignKey(Compound, on_delete=models.CASCADE)
    passtypes_selected = models.ManyToManyField(PassType)
    arrival_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    request_date = models.DateTimeField(auto_now_add=True, blank=True)
    approval_date = models.DateTimeField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    cancellation_reason = models.TextField(null=True, blank=True)
    is_expired = models.BooleanField(default=False)

    # ... Other fields

    def __str__(self):
        return f"PassRequest by {self.user} for {self.compound}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    passrequest = models.ForeignKey(PassRequest, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=50)
    receipt_url = models.URLField(null=True, blank=True)
    is_refunded = models.BooleanField(default=False)
    refund_date = models.DateTimeField(null=True, blank=True)

    # ... Other fields

    def __str__(self):
        return f"Payment of {self.amount} by {self.user} for PassRequest {self.passrequest}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    notification_type = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    action_link = models.URLField(null=True, blank=True)

    # ... Other fields

    def __str__(self):
        return f"Notification for {self.user}: {self.message}"

# Define other models (PropertyOwnerVerification, NationalIDVerification) similarly

class PropertyOwnerVerification(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    verification_document = models.FileField(upload_to='verification_documents/')
    verification_status = models.CharField(max_length=20, choices=VERIFICATION_STATUS_CHOICES, default='pending')
    
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    review_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    # ... Other fields

    def __str__(self):
        return f"Verification for Property: {self.property}"

class NationalIDVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='national_id_verifications')
    verification_result = models.BooleanField()
    
    verification_date = models.DateTimeField(auto_now_add=True, blank=True)
    verifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_national_ids')
    notes = models.TextField(null=True, blank=True)
    
    # Set the default value to the current timestamp using timezone.now()
    timestamp = models.DateTimeField(default=timezone.now)
    
    # ... Other fields

    def __str__(self):
        return f"Verification for User: {self.user}"