from django.shortcuts import render
import requests
from django.http import HttpResponse ,JsonResponse
from urllib.parse import urlencode
import time

api_key = "AIzaSyDAgdao9v6RspQpCx0lhUxJGc9bXmFn2-o"
base_url = 'https://maps.googleapis.com/maps/api/directions/json?'


def toCollege(request):
    l_time = int(time.time())
    Arrival_Time =[]
    records = []
    n = 0
    
    while n<15:
        toCollege_Param ={
            'key':api_key,
            'origin':'place_id:ChIJVa52CtS_wjsR8HwnC9a1JVA',
            'destination':'place_id:ChIJC6y1Noe5wjsRMvdwSwp4oIw',
            'mode':'transit',
            'transit_mode':'bus',
            # 'transit_routing_preference':'less_walking',
            'departure_time': l_time,
        }
        encode_param = urlencode(toCollege_Param)
        final_url = base_url + encode_param
        print(final_url)
        resposne = requests.get(final_url)
        result = resposne.json()
        b = result['routes'][0]['legs'][0]['steps'][0]['transit_details']['line']['short_name']
        d = result['routes'][0]['legs'][0]['steps'][0]['transit_details']["departure_time"]["text"]
        a = result['routes'][0]['legs'][0]['steps'][0]['transit_details']["arrival_time"]["text"]
        if a not in Arrival_Time:
            Arrival_Time.append(a)
            res = {
                'arrival_time':a,
                'depature_time':d,
        '       bus':b,}
            records.append(res)
            n += 1
        l_time += 900
    return JsonResponse({'records': records})


def toHome(request):
    l_time = int(time.time())
    Arrival_Time =[]
    records =[]
    n = 0
    while n<15:
        toHome_Param ={
            'key':api_key,
            'origin':'18.605738321879656, 73.7526949201624',
            'destination':'place_id:ChIJMUZV8dO_wjsRIOXcOiFNAY0',
            'mode':'transit',
            'transit_mode':'bus',
            'transit_routing_preference':'less_walking',
            'departure_time': l_time,
        }
        encode_param = urlencode(toHome_Param)
        final_url = base_url + encode_param
        print(final_url)
        resposne = requests.get(final_url)
        result = resposne.json()
        b = result['routes'][0]['legs'][0]['steps'][0]['transit_details']['line']['short_name']
        d = result['routes'][0]['legs'][0]['steps'][0]['transit_details']["departure_time"]["text"]
        a = result['routes'][0]['legs'][0]['steps'][0]['transit_details']["arrival_time"]["text"]
        if a not in Arrival_Time:
            Arrival_Time.append(a)
            res = {
                'arrival_time':a,
                'depature_time':d,
        '       bus':b,}
            records.append(res)
            n += 1
        l_time += 900
    return JsonResponse({'records': records})