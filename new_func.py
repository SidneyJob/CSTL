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

def print_c(text, color):
	eval(f'print(Fore.{color} + """{text}""" + Style.RESET_ALL)')



@app.route('/', methods=["GET", "POST"])
def reset_password():
    check_result(request)
    return "123"

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

    for header_name, header_value in dict(request.headers).items():
        print_c(f"    [+] {header_name}: {header_value}","MAGENTA")    
    
    print_c(f"""{(100//2 - len("END")) * "+"}END{(100//2)  * "+"}""", "RED")
    if authorized:
        return True
    else:
        return False

app.run(host=app.host, port=app.port)