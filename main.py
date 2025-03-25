import os

from flask import Flask

app = Flask(__name__)
counter = 0

@app.get("/counter")
def getCounter():
  return {"counter": counter}

@app.get("/counter/next")
def nextCounter():
  global counter
  counter += 1
  return {"counter": counter}

if __name__ == "__main__":
  app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))