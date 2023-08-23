from django.contrib import admin
from django.urls import path
from .views import (
    property_list,
    property_detail,
    property_create,
    property_update,
    property_delete,
    compound_list,
    compound_detail,
    compound_create,
    compound_update,
    compound_delete,
    passrequest_create,
    passrequest_update,
    passrequest_delete,
    payment_create,
    notification_create,
    propertyownerverification_create,
    nationalidverification_create,
    nationalidverification_list,
    nationalidverification_detail,
    nationalidverification_update,
    nationalidverification_delete,
    passtype_detail,
    passtype_create,
    passtype_update,
    passtype_delete,
    passrequest_list,
    passrequest_detail,
    payment_list,
    payment_detail,
    payment_update,
    payment_delete,
    notification_list,
    notification_update,
    notification_delete,
    propertyownerverification_list,
    propertyownerverification_detail,
    propertyownerverification_update,
    propertyownerverification_delete,
    # ... other views you want to import ...
)

urlpatterns = [
    path('properties/', property_list, name='property_list'),
    path('property/<int:pk>/', property_detail, name='property_detail'),
    path('property/create/', property_create, name='property_create'),
    path('property/<int:pk>/update/', property_update, name='property_update'),
    path('property/<int:pk>/delete/', property_delete, name='property_delete'),

    path('compounds/', compound_list, name='compound_list'),
    path('compound/<int:pk>/', compound_detail, name='compound_detail'),
    path('compound/create/', compound_create, name='compound_create'),
    path('compound/<int:pk>/update/', compound_update, name='compound_update'),
    path('compound/<int:pk>/delete/', compound_delete, name='compound_delete'),

    path('passrequest/create/', passrequest_create, name='passrequest_create'),
    path('passrequest/<int:pk>/update/', passrequest_update, name='passrequest_update'),
    path('passrequest/<int:pk>/delete/', passrequest_delete, name='passrequest_delete'),

    path('payment/create/', payment_create, name='payment_create'),

    path('notification/create/', notification_create, name='notification_create'),

    path('propertyownerverification/create/', propertyownerverification_create, name='propertyownerverification_create'),

    path('nationalidverification/create/', nationalidverification_create, name='nationalidverification_create'),
    path('nationalidverification/list/', nationalidverification_list, name='nationalidverification_list'),
    path('nationalidverification/<int:pk>/', nationalidverification_detail, name='nationalidverification_detail'),
    path('nationalidverification/<int:pk>/update/', nationalidverification_update, name='nationalidverification_update'),
    path('nationalidverification/<int:pk>/delete/', nationalidverification_delete, name='nationalidverification_delete'),

    path('passtype/<int:pk>/', passtype_detail, name='passtype_detail'),
    path('passtype/create/', passtype_create, name='passtype_create'),
    path('passtype/<int:pk>/update/', passtype_update, name='passtype_update'),
    path('passtype/<int:pk>/delete/', passtype_delete, name='passtype_delete'),

    path('passrequest/list/', passrequest_list, name='passrequest_list'),
    path('passrequest/<int:pk>/', passrequest_detail, name='passrequest_detail'),
    path('passrequest/create/', passrequest_create, name='passrequest_create'),
    path('passrequest/<int:pk>/update/', passrequest_update, name='passrequest_update'),
    path('passrequest/<int:pk>/delete/', passrequest_delete, name='passrequest_delete'),

    path('payment/list/', payment_list, name='payment_list'),
    path('payment/<int:pk>/', payment_detail, name='payment_detail'),
    path('payment/create/', payment_create, name='payment_create'),
    path('payment/<int:pk>/update/', payment_update, name='payment_update'),
    path('payment/<int:pk>/delete/', payment_delete, name='payment_delete'),

    path('notification/list/', notification_list, name='notification_list'),
    path('notification/<int:pk>/update/', notification_update, name='notification_update'),
    path('notification/<int:pk>/delete/', notification_delete, name='notification_delete'),

    path('propertyownerverification/list/', propertyownerverification_list, name='propertyownerverification_list'),
    path('propertyownerverification/<int:pk>/', propertyownerverification_detail, name='propertyownerverification_detail'),
    path('propertyownerverification/create/', propertyownerverification_create, name='propertyownerverification_create'),
    path('propertyownerverification/<int:pk>/update/', propertyownerverification_update, name='propertyownerverification_update'),
    path('propertyownerverification/<int:pk>/delete/', propertyownerverification_delete, name='propertyownerverification_delete'),

    path('nationalidverification/list/', nationalidverification_list, name='nationalidverification_list'),
    path('nationalidverification/<int:pk>/', nationalidverification_detail, name='nationalidverification_detail'),
    path('nationalidverification/create/', nationalidverification_create, name='nationalidverification_create'),
    path('nationalidverification/<int:pk>/update/', nationalidverification_update, name='nationalidverification_update'),
    path('nationalidverification/<int:pk>/delete/', nationalidverification_delete, name='nationalidverification_delete'),
]
