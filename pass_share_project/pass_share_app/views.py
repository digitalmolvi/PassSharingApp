
from .forms import CompoundForm, PassTypeForm, PassRequestForm, PaymentForm, NotificationForm, PropertyOwnerVerificationForm, NationalIDVerificationForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import Compound, PassType, PassRequest, Payment, Notification, PropertyOwnerVerification, NationalIDVerification
from .forms import CompoundForm, PassTypeForm, PassRequestForm, PaymentForm, NotificationForm, PropertyOwnerVerificationForm, NationalIDVerificationForm
from django.http import HttpResponseRedirect

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'property_detail.html', {'property': property})

def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/properties/')  # Redirect to property list
    else:
        form = PropertyForm()
    return render(request, 'property_form.html', {'form': form})

def property_update(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/properties/')  # Redirect to property list
    else:
        form = PropertyForm(instance=property)
    return render(request, 'property_form.html', {'form': form})

def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        property.delete()
        return HttpResponseRedirect('/properties/')  # Redirect to property list
    return render(request, 'property_confirm_delete.html', {'property': property})



def compound_list(request):
    compounds = Compound.objects.all()
    return render(request, 'compound_list.html', {'compounds': compounds})

def compound_detail(request, pk):
    compound = get_object_or_404(Compound, pk=pk)
    return render(request, 'compound_detail.html', {'compound': compound})

def compound_create(request):
    if request.method == 'POST':
        form = CompoundForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/compounds/')  # Redirect to compound list
    else:
        form = CompoundForm()
    return render(request, 'compound_form.html', {'form': form})

def compound_update(request, pk):
    compound = get_object_or_404(Compound, pk=pk)
    if request.method == 'POST':
        form = CompoundForm(request.POST, instance=compound)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/compounds/')  # Redirect to compound list
    else:
        form = CompoundForm(instance=compound)
    return render(request, 'compound_form.html', {'form': form})

def compound_delete(request, pk):
    compound = get_object_or_404(Compound, pk=pk)
    if request.method == 'POST':
        compound.delete()
        return HttpResponseRedirect('/compounds/')  # Redirect to compound list
    return render(request, 'compound_confirm_delete.html', {'compound': compound})


# PassRequest views
def passrequest_create(request):
    if request.method == 'POST':
        # Handle form submission and validation here
        # Create a new PassRequest instance and save it
        return redirect('passrequest_list')  # Redirect to the list view
    return render(request, 'passrequest_create.html')  # Render the creation form

def passrequest_update(request, pk):
    passrequest = get_object_or_404(PassRequest, pk=pk)
    if request.method == 'POST':
        # Handle form submission and validation here
        # Update the existing PassRequest instance and save it
        return redirect('passrequest_list')  # Redirect to the list view
    return render(request, 'passrequest_update.html', {'passrequest': passrequest})  # Render the update form

def passrequest_delete(request, pk):
    passrequest = get_object_or_404(PassRequest, pk=pk)
    if request.method == 'POST':
        # Perform the delete operation
        passrequest.delete()
        return redirect('passrequest_list')  # Redirect to the list view
    return render(request, 'passrequest_delete.html', {'passrequest': passrequest})  # Render the delete confirmation page

# Payment views
def payment_create(request):
    if request.method == 'POST':
        # Handle form submission and validation here
        # Create a new Payment instance and save it
        return redirect('payment_list')  # Redirect to the list view
    return render(request, 'payment_create.html')  # Render the creation form

# Implement payment_update and payment_delete views similarly

# Notification views
def notification_create(request):
    if request.method == 'POST':
        # Handle form submission and validation here
        # Create a new Notification instance and save it
        return redirect('notification_list')  # Redirect to the list view
    return render(request, 'notification_create.html')  # Render the creation form

# Implement notification_update and notification_delete views similarly

# PropertyOwnerVerification views
def propertyownerverification_create(request):
    if request.method == 'POST':
        # Handle form submission and validation here
        # Create a new PropertyOwnerVerification instance and save it
        return redirect('propertyownerverification_list')  # Redirect to the list view
    return render(request, 'propertyownerverification_create.html')  # Render the creation form

# Implement propertyownerverification_update and propertyownerverification_delete views similarly

# NationalIDVerification views
def nationalidverification_create(request):
    if request.method == 'POST':
        # Handle form submission and validation here
        # Create a new NationalIDVerification instance and save it
        return redirect('nationalidverification_list')  # Redirect to the list view
    return render(request, 'nationalidverification_create.html')  # Render the creation form
# NationalIDVerification views
def nationalidverification_list(request):
    nationalidverifications = NationalIDVerification.objects.all()
    return render(request, 'nationalidverification_list.html', {'nationalidverifications': nationalidverifications})

def nationalidverification_detail(request, pk):
    nationalidverification = get_object_or_404(NationalIDVerification, pk=pk)
    return render(request, 'nationalidverification_detail.html', {'nationalidverification': nationalidverification})

def nationalidverification_create(request):
    if request.method == 'POST':
        # Handle form submission and validation here
        # Create a new NationalIDVerification instance and save it
        return redirect('nationalidverification_list')  # Redirect to the list view
    return render(request, 'nationalidverification_create.html')  # Render the creation form

def nationalidverification_update(request, pk):
    nationalidverification = get_object_or_404(NationalIDVerification, pk=pk)
    if request.method == 'POST':
        # Handle form submission and validation here
        # Update the existing NationalIDVerification instance and save it
        return redirect('nationalidverification_list')  # Redirect to the list view
    return render(request, 'nationalidverification_update.html', {'nationalidverification': nationalidverification})  # Render the update form

def nationalidverification_delete(request, pk):
    nationalidverification = get_object_or_404(NationalIDVerification, pk=pk)
    if request.method == 'POST':
        # Perform the delete operation
        nationalidverification.delete()
        return redirect('nationalidverification_list')  # Redirect to the list view
    return render(request, 'nationalidverification_delete.html', {'nationalidverification': nationalidverification})  # Render the delete confirmation page 
# NationalIDVerification views
def nationalidverification_list(request):
    nationalidverifications = NationalIDVerification.objects.all()
    return render(request, 'nationalidverification_list.html', {'nationalidverifications': nationalidverifications})

def nationalidverification_detail(request, pk):
    nationalidverification = get_object_or_404(NationalIDVerification, pk=pk)
    return render(request, 'nationalidverification_detail.html', {'nationalidverification': nationalidverification})

def passtype_detail(request, pk):
    passtype = get_object_or_404(PassType, pk=pk)
    return render(request, 'passtype_detail.html', {'passtype': passtype})

def passtype_create(request):
    if request.method == 'POST':
        form = PassTypeForm(request.POST)
        if form.is_valid():
            passtype = form.save()
            return redirect('passtype_detail', pk=passtype.pk)
    else:
        form = PassTypeForm()
    return render(request, 'passtype_form.html', {'form': form})

def passtype_update(request, pk):
    passtype = get_object_or_404(PassType, pk=pk)
    if request.method == 'POST':
        form = PassTypeForm(request.POST, instance=passtype)
        if form.is_valid():
            passtype = form.save()
            return redirect('passtype_detail', pk=passtype.pk)
    else:
        form = PassTypeForm(instance=passtype)
    return render(request, 'passtype_form.html', {'form': form})

def passtype_delete(request, pk):
    passtype = get_object_or_404(PassType, pk=pk)
    if request.method == 'POST':
        passtype.delete()
        return redirect('passtype_list')
    return render(request, 'passtype_confirm_delete.html', {'passtype': passtype})
# PassRequest views
def passrequest_list(request):
    passrequests = PassRequest.objects.all()
    return render(request, 'passrequest_list.html', {'passrequests': passrequests})

def passrequest_detail(request, pk):
    passrequest = get_object_or_404(PassRequest, pk=pk)
    return render(request, 'passrequest_detail.html', {'passrequest': passrequest})

def passrequest_create(request):
    if request.method == 'POST':
        form = PassRequestForm(request.POST)
        if form.is_valid():
            passrequest = form.save()
            return redirect('passrequest_detail', pk=passrequest.pk)
    else:
        form = PassRequestForm()
    return render(request, 'passrequest_form.html', {'form': form})

def passrequest_update(request, pk):
    passrequest = get_object_or_404(PassRequest, pk=pk)
    if request.method == 'POST':
        form = PassRequestForm(request.POST, instance=passrequest)
        if form.is_valid():
            passrequest = form.save()
            return redirect('passrequest_detail', pk=passrequest.pk)
    else:
        form = PassRequestForm(instance=passrequest)
    return render(request, 'passrequest_form.html', {'form': form})

def passrequest_delete(request, pk):
    passrequest = get_object_or_404(PassRequest, pk=pk)
    if request.method == 'POST':
        passrequest.delete()
        return redirect('passrequest_list')
    return render(request, 'passrequest_confirm_delete.html', {'passrequest': passrequest})
# Payment views
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'payment_detail.html', {'payment': payment})

def payment_create(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            return redirect('payment_detail', pk=payment.pk)
    else:
        form = PaymentForm()
    return render(request, 'payment_form.html', {'form': form})

def payment_update(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            payment = form.save()
            return redirect('payment_detail', pk=payment.pk)
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'payment_form.html', {'form': form})

def payment_delete(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        payment.delete()
        return redirect('payment_list')
    return render(request, 'payment_confirm_delete.html', {'payment': payment})
# Notification views
def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'notification_list.html', {'notifications': notifications})

def notification_update(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    if request.method == 'POST':
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            notification = form.save()
            return redirect('notification_detail', pk=notification.pk)
    else:
        form = NotificationForm(instance=notification)
    return render(request, 'notification_form.html', {'form': form})

def notification_delete(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    if request.method == 'POST':
        notification.delete()
        return redirect('notification_list')
    return render(request, 'notification_confirm_delete.html', {'notification': notification})
# PropertyOwnerVerification views
def propertyownerverification_list(request):
    verifications = PropertyOwnerVerification.objects.all()
    return render(request, 'verification_list.html', {'verifications': verifications})

def propertyownerverification_detail(request, pk):
    verification = get_object_or_404(PropertyOwnerVerification, pk=pk)
    return render(request, 'propertyownerverification_detail.html', {'verification': verification})

def propertyownerverification_create(request):
    if request.method == 'POST':
        form = PropertyOwnerVerificationForm(request.POST)
        if form.is_valid():
            verification = form.save()
            return redirect('propertyownerverification_detail', pk=verification.pk)
    else:
        form = PropertyOwnerVerificationForm()
    return render(request, 'propertyownerverification_form.html', {'form': form})

def propertyownerverification_update(request, pk):
    verification = get_object_or_404(PropertyOwnerVerification, pk=pk)
    if request.method == 'POST':
        form = PropertyOwnerVerificationForm(request.POST, instance=verification)
        if form.is_valid():
            verification = form.save()
            return redirect('propertyownerverification_detail', pk=verification.pk)
    else:
        form = PropertyOwnerVerificationForm(instance=verification)
    return render(request, 'propertyownerverification_form.html', {'form': form})

def propertyownerverification_delete(request, pk):
    verification = get_object_or_404(PropertyOwnerVerification, pk=pk)
    if request.method == 'POST':
        verification.delete()
        return redirect('propertyownerverification_list')
    return render(request, 'propertyownerverification_confirm_delete.html', {'verification': verification})
# NationalIDVerification views
def nationalidverification_list(request):
    verifications = NationalIDVerification.objects.all()
    return render(request, 'verification_list.html', {'verifications': verifications})

def nationalidverification_detail(request, pk):
    verification = get_object_or_404(NationalIDVerification, pk=pk)
    return render(request, 'nationalidverification_detail.html', {'verification': verification})

def nationalidverification_create(request):
    if request.method == 'POST':
        form = NationalIDVerificationForm(request.POST)
        if form.is_valid():
            verification = form.save()
            return redirect('nationalidverification_detail', pk=verification.pk)
    else:
        form = NationalIDVerificationForm()
    return render(request, 'nationalidverification_form.html', {'form': form})

def nationalidverification_update(request, pk):
    verification = get_object_or_404(NationalIDVerification, pk=pk)
    if request.method == 'POST':
        form = NationalIDVerificationForm(request.POST, instance=verification)
        if form.is_valid():
            verification = form.save()
            return redirect('nationalidverification_detail', pk=verification.pk)
    else:
        form = NationalIDVerificationForm(instance=verification)
    return render(request, 'nationalidverification_form.html', {'form': form})

def nationalidverification_delete(request, pk):
    verification = get_object_or_404(NationalIDVerification, pk=pk)
    if request.method == 'POST':
        verification.delete()
        return redirect('nationalidverification_list')
    return render(request, 'nationalidverification_confirm_delete.html', {'verification': verification})

