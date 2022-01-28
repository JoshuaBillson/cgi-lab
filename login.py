#!/usr/bin/env python3

import os
import cgi
import cgitb
import secret
from http.cookies import SimpleCookie

from templates import login_page, after_login_incorrect, secret_page


def main():
    cgitb.enable()

    # Extract Cookies
    cookie = SimpleCookie(os.environ.get("HTTP_COOKIE"))
    cookie_username = cookie.get("username").value if "username" in cookie else None
    cookie_password = cookie.get("password").value if "password" in cookie else None

    # Check That Cookie Is Okay
    cookie_ok = cookie_username == secret.username and cookie_password == secret.password

    # Extract Form Data
    s = cgi.FieldStorage()
    username = cookie_username if cookie_ok else s.getfirst("username")
    password = cookie_password if cookie_ok else s.getfirst("password")

    # Check That Login Is Okay
    login_ok = username == secret.username and password == secret.password

    # If Login Correct And Cookie Is Not Set, Set The Cookie
    print("Content-Type: text/html")
    if login_ok and not cookie_ok:
        print(f"Set-Cookie: username={username}")
        print(f"Set-Cookie: password={password}")

    print()
    if not username or not password:
        print(login_page())
    elif login_ok:
        print(secret_page(username, password))
    else:
        print(after_login_incorrect())


if __name__ == "__main__":
    main()
