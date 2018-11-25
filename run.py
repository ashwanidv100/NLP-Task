from app import app
import os

myPort = int(os.environ.get("PORT", 5432))
app.run(host='ec2-50-19-249-121.compute-1.amazonaws.com',debug=True, port=myPort)
