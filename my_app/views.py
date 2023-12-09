from django.shortcuts import render
from rest_framework import generics
import traceback
from django.http import HttpResponse
import json
from .models import *
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from datetime import date,datetime

# Create your views here.
class FriendsDetailsView(generics.ListAPIView):
    def post(self,request):
        try:
            data = request.data
            first_name = data["first_name"]
            last_name = data["last_name"]
            contact = data["contact"]
            alternative_contact = data["alternative_contact"]
            email = data["email"]
            date_of_birth = data["date_of_birth"]
            address = data["address"]
            maritial_status = data["maritial_status"]
            favorite_sports = data["favorite_sports"]
            hobbies = data["hobbies"]
    
            bestfriends_obj = friend_info(
                first_name = first_name,
                last_name = last_name,
                contact = contact,
                alternative_contact = alternative_contact,
                email = email,
                date_of_birth = date_of_birth,
                address = address,
                maritial_status = maritial_status,
                favorite_sports = favorite_sports,
                hobbies = hobbies
            )

            bestfriends_obj.save()
            return HttpResponse(
                json.dumps({"status":"success","message":"Friend details added successfully"}),
                status=200,
                content_type="application/json",
            )
        
        except Exception as ex:
            traceback.print_exc()
            return HttpResponse(
                json.dumps({"status":"failed","message":"There is backed issue, please contact administrator"}),
                status=200,
                content_type="application/json",
            )
        
    def get(self,request):
        try:
            response_data = []
            friends_data = friend_info.objects.all()

            for i in friends_data:
                full_name = str(f"{i.first_name} {i.last_name}")
                date_of_birth = datetime(i.date_of_birth.year, i.date_of_birth.month, i.date_of_birth.day)
                difference = datetime.now() - date_of_birth
                years = difference.days // 365
                response_data.append({
                    "id":i.pk,
                    "name":full_name,
                    "contact_number":i.contact,
                    "alternative_contact":i.alternative_contact,
                    "email":i.email,
                    "date_of_birth":str(i.date_of_birth),
                    "age":f"{years} years",
                    "address":i.address,
                    "maritial_status":i.maritial_status,
                    "hobbies":i.hobbies
                })

            return HttpResponse(
                json.dumps({"status":"success","message":"Friends details retrived successfully","data":response_data}),
                status=200,
                content_type="application/json",
            )
        
        except Exception as ex:
            traceback.print_exc()
            return HttpResponse(
                json.dumps({"status":"failed","message":"There is backed issue, please contact administrator"}),
                status=200,
                content_type="application/json",
            )

class LocationDetailsView(generics.ListAPIView):
    def post(self,request):
        try:
            data = request.data
            location_name = data["location_name"]

            location_obj = location(
                name = location_name
            )

            location_obj.save()
            return HttpResponse(
                json.dumps({"status":"success","message":"Location added successfully"}),
                status=200,
                content_type="application/json",
            )
        
        except Exception as ex:
            traceback.print_exc()
            return HttpResponse(
                json.dumps({"status":"failed","message":"There is backed issue, please contact administrator"}),
                status=200,
                content_type="application/json",
            )
        
    def get(self,request):
        try:
            response_data = []
            location_data = location.objects.all()

            for i in location_data:
                response_data.append({
                    "id":i.pk,
                    "location":i.name
                })

            return HttpResponse(
                json.dumps({"status":"success","message":"Location details retrived successfully","data":response_data}),
                status=200,
                content_type="application/json",
            )
        
        except Exception as ex:
            traceback.print_exc()
            return HttpResponse(
                json.dumps({"status":"failed","message":"There is backed issue, please contact administrator"}),
                status=200,
                content_type="application/json",
            )

# class CompanyDetailsView(generics.ListAPIView):
#     def post(self,request):
#         try:
#             data = request.data
#             friend_id = data["friend_id"]
#             current_company = data["current_company"]
#             location_id = data["location_id"]
#             position = data["position"]
#             date_of_joining = data["date_of_joining"]

#             bestfriends_obj = company_details(
#                 friend_id = friend_id,
#                 current_company = current_company,
#                 location_id = location_id,
#                 position = position,
#                 date_of_joining = date_of_joining
#             )

#             bestfriends_obj.save()
#             return HttpResponse(
#                 json.dumps({"status":"success","message":"Company details added successfully"}),
#                 status=200,
#                 content_type="application/json",
#             )
        
#         except Exception as ex:
#             traceback.print_exc()
#             return HttpResponse(
#                 json.dumps({"status":"failed","message":"There is backed issue, please contact administrator"}),
#                 status=200,
#                 content_type="application/json",
#             )
        
#     def get(self,request):
#         try:
#             response_data = []
#             friends_data = company_details.objects.all()

#             for i in friends_data:
#                 full_name = str(f"{i.friend.first_name} {i.friend.last_name}")
#                 date_of_joining = datetime(i.date_of_joining.year, i.date_of_joining.month, i.date_of_joining.day)
#                 difference = datetime.now() - date_of_joining
#                 years = difference.days // 365
#                 months = (difference.days % 365) // 30
#                 days = (difference.days % 365) % 30
#                 response_data.append({
#                     "id":i.pk,
#                     "name":full_name,
#                     "current_company":i.current_company,
#                     "location":i.location.name,
#                     "position":i.position,
#                     "date_of_joining":str(date_of_joining.date()),
#                     "Total Experiance":f"{years} years, {months} months, {days} days"

#                 })

#             return HttpResponse(
#                 json.dumps({"status":"success","message":"Company details retrived successfully","data":response_data}),
#                 status=200,
#                 content_type="application/json",
#             )
        
#         except Exception as ex:
#             traceback.print_exc()
#             return HttpResponse(
#                 json.dumps({"status":"failed","message":"There is backed issue, please contact administrator"}),
#                 status=200,
#                 content_type="application/json",
#             )

# class DeleteFriendDetailsView(generics.ListAPIView):
#     def post(self,request):
#         try:
#             data = request.data
#             friend_id = data.get("id")

#             # Check if the ID exists in the table
#             try:
#                 friend = friends.objects.get(id=friend_id)
#             except ObjectDoesNotExist:
#                 return HttpResponse(
#                     json.dumps({"status": "failed", "message": "Friend ID does not exist"}),
#                     status=404,
#                     content_type="application/json",
#                 )

#             # If the ID exists, proceed with deletion
#             with connection.cursor() as cursor:
#                 cursor.execute(f"DELETE FROM my_app_bestfriends WHERE id = {friend_id}")

#             return HttpResponse(
#                 json.dumps({"status":"success","message":"Friend details deleted successfully"}),
#                 status=200,
#                 content_type="application/json",
#             )
        
#         except Exception as ex:
#             traceback.print_exc()
#             return HttpResponse(
#                 json.dumps({"status":"failed","message":"There is backed issue, please contact administrator"}),
#                 status=200,
#                 content_type="application/json",
#             )
