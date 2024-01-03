from imports import *


# <----------------------------------------------------------------->

def print_cookies(cookies):
    return "\t[+] "+ "\n\t[+] ".join(cookies)

## Page to test CSRF
@app.route('/reset_password', methods=["GET", "POST"])
def reset_password():
    cookies = []

    if check_result(request):
        return "Successfull reset!"

    return "None"


# <----------------------------------------------------------------->




try:
    @app.route('/api_gen', methods=['POST', 'GET'])
    def api_gen():
        res = Response(json.dumps(
            {"key":None}
        ))

        try:
            Origin = request.headers['Origin']
        except:
            Origin = "https://discovery-lab.su"
            
        res.headers['Content-Type'] = "application/json"
        res.headers['Access-Control-Allow-Origin'] = Origin   
        res.headers['Access-Control-Allow-Credentials'] = 'true' 

        cookies = []
        if request.cookies.get('None'):
            cookies.append(f'None: {request.cookies.get("None")}')

        if request.cookies.get('Lax'):
            cookies.append(f'Lax: {request.cookies.get("Lax")}')

        if request.cookies.get('Strict'):
            cookies.append(f'Strict: {request.cookies.get("Strict")}')

        if cookies:
            print_c(f"""
 <----------------------------------------->
            !!!!!! WARNING !!!!!!
[+] Authentification passed!
[+] URL: {request.url}
[*] Recived cookies: [
{print_cookies(cookies)}
]
 <----------------------------------------->
            """,
            'RED'
        )
            
            res.data = json.dumps(
                {"key":f"SidneyJob{{{gen_random_string(16)}_gen_page}}"}
            )

            return res
        return res





    @app.route('/api_without_creds', methods=['POST', 'GET'])
    def api_creds():
        res = Response(json.dumps(
            {"key":None}
        ))
        
        res.headers['Content-Type'] = "application/json"
        res.headers['Access-Control-Allow-Origin'] = "*"    

        if check_result(request):
            res.data = json.dumps(
                {"key":f"SidneyJob{{{gen_random_string(16)}_creds_page}}"}
            )

            return res
        return res


    @app.route('/api_null', methods=['POST', 'GET'])
    def api_null():
        res = Response(json.dumps(
            {"key":None}
        ))

        res.headers['Content-Type'] = "application/json"
        res.headers['Access-Control-Allow-Origin'] = 'null'
        res.headers['Access-Control-Allow-Credentials'] = 'true'

        if check_result(request):
            res.data = json.dumps(
                {"key":f"SidneyJob{{{gen_random_string(16)}_null_page}}"}
            )

            return res
        return res
       





    @app.route('/api_correct', methods=['POST', 'GET'])
    def api_correct():
        res = Response(json.dumps(
            {"key":None}
        ))
        
        res.headers['Content-Type'] = "application/json"
        res.headers['Access-Control-Allow-Origin'] = "https://discovery.sidneyjob.ru"
        res.headers['Access-Control-Allow-Credentials'] = 'true'  

        if check_result(request):
            res.data = json.dumps(
                {"key":f"SidneyJob{{{gen_random_string(16)}_creds_page}}"}
            )

            return res
        return res
except:
    pass



