#!/usr/bin/python

from flask import Flask
app=Flask(__name__)
@app.route("/")

def helloworld ():
  return "Happy 2021 !!!"

app.run(host='0.0.0.0')
