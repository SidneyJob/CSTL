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
    cookies = []
    

    if request.method == "GET":
        data = dict(request.args)

    elif request.method == "POST":
        data = dict(request.form)

    else:
        data = {"None": "None"}



    ############ PRINT DATA
    print_c(f"""{"+"*100}\n{(100//2 - len("REQUEST INFO")) * "+"}REQUEST INFO{(100//2)  * "+"}\n{"+"*100}""", "RED")
    print_c(f"""
[+] URL: {request.url}
[+] METHOD: {request.method}
""", "RED")

    print_c(f"[++] Cookies: \n{'+' * 100 }", "GREEN")
    for cookie_name, cookie_value in dict(request.cookies).items():
        print_c(f"[+] {cookie_name}: {cookie_value}", "MAGENTA")

    print_c(f"{'+' * 100}\n", "GREEN")



    print_c(f"[++] Data: \n{'+'*100}", "BLUE")
    for data_name, data_value in data.items():
        print_c(f"[+] {data_name}: {data_value}","MAGENTA")    
    print_c(f"{'+' * 100}", "BLUE")

    print_c(f"""{"+"*100}\n{(100//2 - len("END")) * "+"}END{(100//2)  * "+"}\n{"+"*100}""", "RED")
app.run(host=app.host, port=app.port)