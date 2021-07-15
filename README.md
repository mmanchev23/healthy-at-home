[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mmanchev23/healthy-at-home2/blob/master/LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/mmanchev23/healthy-at-home2/graphs/commit-activity)

# **Healthy at Home 2**

## Second version of the main project [Healthy at Home](https://github.com/mmanchev23/healthy-at-home).

<br/>

### **How to start the project locally?**
<ol>
    <li>
        Open the project in the console, IDE or text editor.
    </li>
    <li>
        Let's first start the API:
        <br/>
        <code>
            cd backend
        </code>
    </li>
    <li>
        You should install Python in order to run the app. Follow the link bellow to install Python:
        <br/>
        <code>
            https://www.python.org/downloads/
        </code>
    </li>
    <li>
        Install virtual environment (if you haven't already!!!) in the backend folder. My virtual environment of choice is "Pipenv", but feel free to use other as well.
        <br/>
        <code>
            pip install pipenv
        </code>
    </li>
    <li>
        Open the virtual environment.
        <br/>
        <code>
            pipenv shell
        </code>
    </li>
    <li>
        Install the required packages:
        <br/>
        <code>
            pipenv install -r requirements.py
        </code>
    </li>
    <li>
        Run the following commands:
        <br/>
        <code>
            1. python manage.py makemigrations
        </code>
        <br/>
        <code>
            1. python manage.py migrate
        </code>
        <br/>
        <code>
            1. python manage.py runserver
        </code>
    </li>
    <li>
        Open the following link:
        <br/>
        <code>
            http://127.0.0.1:8000/
        </code>
    </li>
    <li>
        Let's now start the frontend app. Go one folder back:
        <br/>
        <code>
            cd ..
        </code>
    </li>
    <li>
        You should install Node.js in order to run the app. Follow the link bellow to install Node.js:
        <br/>
        <code>
            https://nodejs.org/en/download/
        </code>
    </li>
    <li>
        Run the following commands:
        <br/>
        <code>
            1. npm install
        </code>
        <br/>
        <code>
            1. npm start
        </code>
    </li>
    <li>
        Open the following link:
        <br/>
        <code>
            http://localhost:3000/
        </code>
    </li>
    <li>
        If you can see the see the Frontend App as well as the API Home Page, then congratulations, you have successfully started the project locally!
    </li>
</ol>

<br/>

### **What do the files contain?**
<code>.idea</code> - all the files for the python interpreter configurations in PyCharm
<br/>
<code>.vscode</code> - all the files for the python interpreter configurations in Visual Studio Code
<br/>
<code>backend</code> - all the files for the backend side of the project
<br/>
<code>frontend</code> - all the files for the frontend side of the project
<br/>
<code>LICENSE</code> - the license
<br/>
<code>README.md</code> - the file you are reading right now

<br/>

### **What technologies have we used?**
<ul>
    <li>
        Programming Languages - Python, Javascript, HTML5, CSS3
        <br/>
        <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>
        <img alt="JavaScript" src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/>
        <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/>
        <img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/>
    </li>
    <li>
        Frameworks - Django, React.js
        <br/>
        <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/>
        <img alt="React" src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB"/>
    </li>
    <li>
        API - Django Rest Framework
        <br/>
        <img alt="DjangoREST" src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray"/>
    </li>
    <li>
        API Testing - Postman
        <br/>
        <img alt="Postman" src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=red" />
    </li>
    <li>
        Database - SQLite 3
        <br/>
        <img alt="SQLite" src ="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/>
    </li>
    <li>
        Deployment - Heroku and Vercel
        <br/>
        <img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>
        <img alt="Vercel" src="https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white"/>
    </li>
    <li>
        Version Controll Systems - Git and Github
        <br/>
        <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>
        <img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>
    </li>
    <li>
        IDE - Visual Studio Code, PyCharm Community Edition
        <br/>
        <img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
        <img alt="PyCharm" src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green"/>
    </li>
</ul>

<br/>

### **What technologies have we used in the frontend?**
<ul>
    <li>
        Programming Languages - Javascript, HTML5, CSS3
        <br/>
        <img alt="JavaScript" src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/>
        <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/>
        <img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/>
    </li>
    <li>
        Frameworks - React.js
        <br/>
        <img alt="React" src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB"/>
    </li>
    <li>
        Deployment - Vercel
        <br/>
        <img alt="Vercel" src="https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white"/>
    </li>
    <li>
        Version Controll Systems - Git and Github
        <br/>
        <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>
        <img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>
    </li>
    <li>
        IDE - Visual Studio Code
        <br/>
        <img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
    </li>
</ul>

<br/>

### **What technologies have we used in the backend?**
<ul>
    <li>
        Programming Languages - Python
        <br/>
        <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>
    </li>
    <li>
        Frameworks - Django
        <br/>
        <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/>
    </li>
    <li>
        API - Django Rest Framework
        <br/>
        <img alt="DjangoREST" src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray"/>
    </li>
    <li>
        API Testing - Postman
        <br/>
        <img alt="Postman" src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=red" />
    </li>
    <li>
        Database - SQLite 3
        <br/>
        <img alt="SQLite" src ="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/>
    </li>
    <li>
        Deployment - Heroku
        <br/>
        <img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>
    </li>
    <li>
        Version Controll Systems - Git and Github
        <br/>
        <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>
        <img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>
    </li>
    <li>
        IDE - PyCharm Community Edition
        <br/>
        <img alt="PyCharm" src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green"/>
    </li>
</ul>
