from flask import render_template, make_response
# from colorama import Fore, Style
from logger import setup_logger
import random
import jwt
import os

logger = setup_logger()


def gen_random_string(lenght):
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    string = ''

    for i in range(lenght):
        string += random.choice(chars)
    return string


def print_c(text, color):
    eval(f'print(Fore.{color} + """{text}""" + Style.RESET_ALL)')


def print_cookies(cookies):
    return "[+] " + "\n[+] ".join(cookies)


def generate_jwt():
    secret_key = os.environ.get('SECRET_KEY')

    tasks = {'login': True, 'api_key': gen_random_string(16)}
    token = jwt.encode(tasks, secret_key, algorithm="HS256")

    return token


def return_cookie(request):
    if not request.cookies.get('None'):
        res = make_response(render_template('index.html'))
        res.set_cookie('None', generate_jwt(), samesite="None", secure=True)
        res.set_cookie('Lax', generate_jwt(), samesite="Lax")
        res.set_cookie('Strict', generate_jwt(), samesite="Strict")
        res.set_cookie('None_SameSite', generate_jwt())

        logger.info('Set cookie!')
        return res
    else:
        res = make_response(render_template(
            'index.html', cook=dict(request.cookies))
            )
        return res


def check_result(request):
    # authorized = 0

    if request.method == "GET":
        data = dict(request.args)

    elif request.method == "POST":
        data = dict(request.form)

    else:
        data = {"None": "None"}

    # СООБЩЕНИЯ ОТ TOKIAKASU
    # Логируется строка вида "GET https://localhost:8081/reset_password"
    logger.info(f"{request.method} {request.url}")

    # Предыдущая реализация вывода кук при запросе
    # logger.info("Cookies:")
    # for cookie_name, cookie_value in dict(request.cookies).items():
    #     logger.info(f"    [+] {cookie_name}: {cookie_value}")
    #     if cookie_name:
    #         authorized = 1
    
    # Куки соединяются в единую строку, включая символы переносы строки
    cookies_info = "\n".join([f"[+] {cookie_name}: {cookie_value}"
                              for cookie_name, cookie_value
                              in dict(request.cookies).items()
                              if cookie_name is not None])

    # после полученная строка вставляется в лог
    logger.info(f"Cookies:\n{cookies_info}")

    # код не трогал, ибо не видел данных с ними
    logger.info("Data:")
    for data_name, data_value in data.items():
        logger.info(f"[+] {data_name}: {data_value}")

    logger.info("\nHeaders:")

    if cookies_info:
        return True
    else:
        return False

