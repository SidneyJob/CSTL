from flask import Flask, render_template_string, render_template, request, make_response, Response, send_file
from colorama import Fore, Style
import random
import json
import jwt
import os

app = Flask(__name__)
app.host = "0.0.0.0"
app.port = 8081
app.debug = True
app.key = "SidneyJob"

# <----------------------------------------->
# !DISABLE LOGGING REQUESTS!
import logging

app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True
# <----------------------------------------->

def gen_random_string(lenght):
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    string = ''
    
    for i in range(lenght):
        string += random.choice(chars)
    return string


def print_c(text, color):
	eval(f'print(Fore.{color} + """{text}""" + Style.RESET_ALL)')

def generate_jwt():
    tasks = { 'login': True, 'api_key': gen_random_string(16) }
    token = jwt.encode(tasks, app.key, algorithm="HS256")

    return token

def return_cookie(request):
    if not request.cookies.get('None'):
        res = make_response(render_template("index.html"))
        res.set_cookie('None', generate_jwt(), samesite="None", secure=True)
        res.set_cookie('Lax', generate_jwt(), samesite="Lax")
        res.set_cookie('Strict', generate_jwt(), samesite="Strict")
        res.set_cookie('None_SameSite', generate_jwt())
   
        print(Fore.GREEN + '[+] Set cookie!'  + Style.RESET_ALL)
        return res
    else:
        res = make_response(render_template("index.html", cook=dict(request.cookies)))
        return res

def check_result(request):
    authorized = 0

    if request.method == "GET":
        data = dict(request.args)

    elif request.method == "POST":
        data = dict(request.form)

    else:
        data = {"None": "None"}



    ############ PRINT DATA
    print_c(f"""{(100//2 - len("REQUEST INFO")) * "+"}REQUEST INFO{(100//2)  * "+"}""", "RED")
    print_c(f"""[+] URL: {request.url}\n[+] Method: {request.method}\n""", "RED")

    print_c(f"[++] Cookies:", "GREEN")
    for cookie_name, cookie_value in dict(request.cookies).items():
        print_c(f"    [+] {cookie_name}: {cookie_value}", "MAGENTA")
        if cookie_name:
            authorized = 1

    print_c(f"\n[++] Data:", "BLUE")
    for data_name, data_value in data.items():
        print_c(f"    [+] {data_name}: {data_value}","MAGENTA")    

    print_c(f"\n[++] Headers:", "YELLOW")

    # ARTEM ARTEMARTEMARTEMARTEMARTEMARTEMARTEMARTEMARTEMARTEMARTEMARTEM 
    
    print_c(f"""{(100//2 - len("END")) * "+"}END{(100//2)  * "+"}""", "RED")
    if authorized:
        return True
    else:
        return False

