from flask import Flask
from views import views
import os

app=Flask(__name__)
app.register_blueprint(views,url_prefix="/")

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000) #heroku sets the PORT environ variable
    app.run(debug=True, host="0.0.0.0", port=port)