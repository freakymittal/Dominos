var request = new XMLHttpRequest();
request.open("GET", "https://pizzaonline.dominos.co.in/", true);
request.withCredentials = true;
request.send();
request.onreadystatechange = function() {
  if(this.readyState == this.HEADERS_RECEIVED) {
    console.log(request.getAllResponseHeaders());
    console.log(request.responseHeaders);
  }
}