from dotenv import load_dotenv
from flask import Flask, redirect, request, session, url_for, render_template
import msal
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TENANT_ID = os.getenv("TENANT_ID")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
REDIRECT_PATH = "/getAToken"
SCOPE = ["User.Read"]


def build_msal_app():
    return msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )


@app.route("/")
def index():
    user = session.get("user")

    if user:
        return render_template("home.html", user=user)

    return render_template("login.html")


@app.route("/login")
def login():
    auth_url = build_msal_app().get_authorization_request_url(
        scopes=SCOPE,
        redirect_uri="http://localhost:5000/getAToken"
    )
    return redirect(auth_url)


@app.route(REDIRECT_PATH)
def authorized():
    result = build_msal_app().acquire_token_by_authorization_code(
        request.args["code"],
        scopes=SCOPE,
        redirect_uri="http://localhost:5000/getAToken"
    )

    if "id_token_claims" in result:
        session["user"] = result["id_token_claims"]
        return redirect("/")

    return f"Login failed: {result}"


@app.route("/logout")
def logout():
    session.clear()
    return render_template(
        "logout.html",
        logout_url=f"{AUTHORITY}/oauth2/v2.0/logout?post_logout_redirect_uri=http://localhost:5000/"
    )


if __name__ == "__main__":
    app.run(debug=True)