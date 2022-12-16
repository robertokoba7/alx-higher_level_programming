# Python - Network #1

Project done during **Full Stack Software Engineering studies** at **ALX SE Programme** and **Holberton School**. It aims to learn how to fetch internet resources using urllib package,Quickstart with Requests package,Requests package.   

## Technologies
* Python Scripts are written with Python (version 3.8.5)
* Tested on Ubuntu 20.04 LTS

## Files
**Filename**    	|**Description**
------------------------|----------------------
`0-hbtn_status.py`  |script that fetches `https://alx-intranet.hbtn.io/status` using the package `urllib`
`1-hbtn_header.py`    |  script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.
`2-post_email.py` | script that takes in a URL and an email, sends a **POST**request to the passed URL with the email as a parameter, and displays the body of the response `(decoded in utf-8)`
`3-error_code.py`  | script that takes in a URL, sends a request to the URL and displays the body of the response `(decoded in utf-8)` while managing `urllib.error`.HTTPError exceptions and print: `Error code:` followed by the HTTP status code 
`4-hbtn_status.py` | script that fetches `https://alx-intranet.hbtn.io/status`
`5-hbtn_header.py` | script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header
`6-post_email.py`  | script that takes in a URL and an email address, sends a **POST** request to the passed URL with the email as a parameter, and finally displays the body of the response.
`7-error_code.py` | script that takes in a URL, sends a request to the URL and displays the body of the response. If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
`8-json_api.py` | Write a Python script that takes in a letter and sends a **POST** request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
`10-my_github.py` |  script that takes your GitHub credentials (username and password) and uses the **GitHub API** to display your `id`.  use **Basic Authentication** with a **personal access token as password** to access to your information (only `read:user` permission is needed)
`100-github_commits.py` | script that takes 2 arguments in order to solve this challenge.
