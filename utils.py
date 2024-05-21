import requests

def scan_secure_cookies(url):
    try:
        response = requests.get(url, verify=True)
        cookies = response.cookies

        secure_cookies = []
        for cookie in cookies:
            if cookie.secure:
                secure_cookies.append({'name': cookie.name, 'value': cookie.value})

        return secure_cookies

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []
