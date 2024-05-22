import requests

def scan_all_cookies(url):
    try:
        response = requests.get(url, verify=True)
        cookies = response.cookies

        all_cookies = []
        for cookie in cookies:
            all_cookies.append({
                'name': cookie.name,
                'value': cookie.value,
                'secure': cookie.secure
            })

        return all_cookies

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []
