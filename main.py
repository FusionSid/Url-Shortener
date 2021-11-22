from flask import Flask, redirect, request, jsonify, Response
from flask.templating import render_template
import json
import pg

HOMEURL = "https://url-shortener.fusionsid.repl.co"
app = Flask("Url-Shortener")

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        url = request.form['url']
        for i in ['http://', 'https://']:
            if i in url:
                http = True
            else:
                http = False

        if http == False:
            url = f"http://{url}"
        with open('urls.json') as f:
            data = json.load(f)
        codes = []
        for i in data:
            codes.append(i["code"])
        while True:
            code = pg.gen_pass()
            if code in codes:
                pass
            else:
                break
        newurl = {"code":code, "url":url}
        data.append(newurl)
        with open('urls.json', 'w') as f:
            json.dump(data, f, indent=4)
        return render_template("index.html", url=f"Url Created!     |     URL: --> {HOMEURL}/{code} <--")
    else:
        return render_template("index.html")


@app.route('/<code>/')
def urlshort(code):
    if len(code) == 4:
        with open('urls.json') as f:
            data = json.load(f)

        for item in data:
            if item['code'] == code:
                rurl = item['url']
            else:
                rurl = False
        
        if rurl == False:
            return "Invalid Code"

        return redirect(rurl)
        
    else:
        return "Invalid Code"


@app.route("/api/", methods=['POST', 'GET'])
def api():
    if request.method == "POST":
      url = request.form['url']
      for i in ['http://', 'https://']:
          if i in url:
              http = True
          else:
              http = False

      if http == False:
          url = f"http://{url}"
      with open('urls.json') as f:
          data = json.load(f)
      codes = []
      for i in data:
          codes.append(i["code"])
      while True:
          code = pg.gen_pass()
          if code in codes:
              pass
          else:
              break
      newurl = {"code":code, "url":url}
      data.append(newurl)
      with open('urls.json', 'w') as f:
          json.dump(data, f, indent=4)
      result = f"{HOMEURL}/{code}"
      print(result)
      return result




# Run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)