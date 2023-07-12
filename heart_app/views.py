from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as Login_process 
from django.contrib.auth import logout as Logout_process 
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from django.contrib.auth.decorators import login_required
import pickle
from heart_app.mycharts import *
def  login(request):
     if request.method=='POST':
         username=request.POST.get('username')
         pass1=request.POST.get('pswrd')
         remember=request.POST.get('remember')
         user=authenticate(request,username=username,password=pass1)
         if user is not None:
             Login_process(request,user)
             if not remember:
                 request.session.set_expiry(0)
             return redirect('index')
         else:
             return HttpResponse("username or password incorrect")
     
     return render(request,'login.html')

def  signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pswrd1')
        pass2=request.POST.get('pswrd2')

        if pass1!=pass2:
            return HttpResponse("your password and confirm password are not same")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request,'signup.html')

def logout(request):
    Logout_process(request)
    return redirect('login')

def country(request):
    return render(request,'country.html')

@login_required(login_url='login')
def index(request):
     file = open("coviddata.pkl",'rb')
     df = pickle.load(file)
     plt_div=histogram1(df.copy())
     plt_div_sc=scatter(df.copy())
     plt_div1=bargraphtop5(df.copy())
     plt_div2=sunburst1(df.copy())
     plt_div3=sunburst2(df.copy())
     plt_div4=sunburst3(df.copy())
     plt_div5=line1(df.copy())
     plt_div6=line2(df.copy())
     plt_div7=con_line1(df.copy())
     return render(request,'index.html',{'histogram':plt_div,'bar':plt_div1,'sun':plt_div2,'sun1':plt_div3,'sun2':plt_div4,'line':plt_div5,'line1':plt_div6,'scatter':plt_div_sc,'con_line':plt_div7}) 

@login_required(login_url='login')
def country(request):
    
     file = open("coviddata.pkl",'rb')
     df = pickle.load(file)
     plt_div1=con_line1(df.copy())
     plt_div2=con_line2(df.copy())
     plt_div3=con_line3(df.copy())
     plt_div4=con_line4(df.copy())
     plt_div5=sunburst_con(df.copy())
     plt_div6=bargraphtop(df.copy())


     return render(request,'country.html',{'con_line1':plt_div1,'con_line2':plt_div2,'con_line3':plt_div3,'con_line4':plt_div4,'sunburst_con':plt_div5,'bargraphtop':plt_div6})     
      
    #  df=pd.read_csv('owid-covid-data.csv')
    #  scatter=px.bar(df,x="continent",y="total_deaths",color="location",hover_data=['total_cases'],barmode='group')
    #  scatter.update_layout({
    #     'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
    #     'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
    #     },
    #     font_family="Comic Sans MS",
    #     font_color="white",
    #     xaxis=dict(showgrid=False),
    #     yaxis=dict(showgrid=False))

     #geo graph
    #  df=pd.read_csv('owid-covid-data.csv')
    #  geo = px.choropleth(df,       locations='iso_code',        
    #                      color='new_cases',hover_name="location",title="cases worldwide ")
    #  geo.update_layout({
    #     'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
    #     'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
    #     },
    #     font_family="Comic Sans MS",
    #     font_color="white",
    #     margin={'r':0,'t':0,'l':0,'b':0},
       
    #    )

     
    #  plt_div_scatter= plot(scatter, output_type='div')

    #  plt_div_geo = plot(geo, output_type='div')
    
