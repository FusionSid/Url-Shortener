# Url Shortener

### This is a url shortener website I made.
### You can check it out [here](https://url-shortener.fusionsid.repl.co/)

## How it works:
On the homepage you add a url and then the script generates a unique code for you.
Now when you add the code to the url: `https://url-shortener.fusionsid.repl.co/<code>`
The script checks the json file(I tried sql but thought json would be easier) for that code and if the code is in the json file. It will get the url to redirect to and redirect you to it - No ads, no ip grabbing, No wait 5 sec .

Im using this as the backend of my url shortening app that im making using flutter(dart). You can check it out [here](https://github.com/FusionSid/Url-Shortner-App)

## Post Requests
You can also send post requests to the app and it will send back a url.

**This is how to do that in Python**
```
import requests

def post_data(short : str):
  data = {'url':short}
  url = "https://url-shortener.fusionsid.repl.co/api/"
  response = requests.post(url, data=data)
  url = response.content.decode()
  print(url)
 
post_data("fusionsid.xyz)
```



**This is how to do the same thing in dart**
```
import 'package:http/http.dart';

Future postData(String short) async {
  const url = "https://url-shortener.fusionsid.repl.co/api/";
  final response = await post(Uri.parse(url), body: {"url": short});
  String responseurl = response.body;
  print(responseurl);
}

postData("fusionsid.xyz");
```
