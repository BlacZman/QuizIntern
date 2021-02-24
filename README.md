# The Internship 2021

This repository is created for theinternship.io program.

# Table of contents
* [Sorting Acronyms](#1-sorting-acronyms)
* [Floating Prime](#2-floating-prime)
* [Digit Hangman](#3-digit-hangman)
* [Basic Web Crawler](#4-basic-web-crawler)
* * [Extract Data from Source HTML](#41-extract-data-from-source-html)
* * [API](#42-api-extract-data-from-source-html)

# 1. Sorting Acronyms
To run the code. type this in '1' folder.
```
$ py 1st.py
```

# 2. Floating Prime
To run the code. type this in '2' folder.
```
$ py 2nd.py
```

# 3. Digit Hangman
To run the code. type this in '3' folder.
```
$ py 3rd.py
```

# 4. Basic Web Crawler
CI/CD version that automatically deployed on Cloud Run can be found [here](https://gitlab.com/BlacZman/api_getlogo)
## 4.1. Extract Data from Source HTML
To run the code. type this in '4' folder.
```
$ py 4th-1.py
```

## 4.2. [API] Extract Data from Source HTML
### Directly access to API
* https://logocompanies-dm4dse37vq-as.a.run.app/companies to access this api without running the code.
### Open the API by Docker
If you have [Docker](https://www.docker.com/) you can use either
#### Default docker
* Run this code.
```
$ docker build -t [name of your choice] .
$ docker run -p 8000:8000 [name of your choice]
```
* If there is nothing wrong, you should be able to access the api by http://127.0.0.1:8000/companies.
#### Docker compose
* Simply run this code inside '4' folder.
```
$ docker-compose up
```
* Then access the api by http://127.0.0.1:8000/companies
### Python runtime
* You need to have at least Python 3.x or newer.
* You need to have the required module by typing this command in terminal (WARNING! this will mess with your python environment. Create virtual environment(venv) before installing is recommended.)
```
$ pip install -r requirements.txt
```
* and you need to uncomment these 2 lines in the file `4th-2.py`.
```
.. |
28 | 
29 | # if __name__ == "__main__":
30 | #     app.run(port=8000)
```
* to
```
.. |
28 | 
29 | if __name__ == "__main__":
30 |     app.run(port=8000)
```
* Then run this code in your terminal.
```
$ py 4th-2.py
```
* Then access the api by http://127.0.0.1:8000/companies
