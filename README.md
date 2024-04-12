Here is the showcase of the frontend:
<https://samchenghowing.github.io/COMP3334/#/>

Used technologies:

Frontend: Vue.js

Backend: Python flask, Azure web service with azure cosmos db

### Update Apr 2024: 
## This app have intergrated the idea from:<https://github.com/miguelgrinberg/Flask-SocketIO-Chat>
please visit his page and supports him!

### If you want to test the backend locally, you need to install and login to the Azure cli
Please check out the method below for azure cli guide
<https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt>


## Project setup to run the backend application locally

### Create a virtual environment for the app

```
python3 -m venv .venv
source .venv/bin/activate
```

### Install the dependencies

```
pip3 install -r requirements.txt
```

### run the app

```
flask run
```

When new code is pushed to the master branch, it will be deploy automatically to the Azure App Service hosting on <https://icy-ocean-55c1ab97056148c38929dee989edc826.azurewebsites.net/>

You may check the current deployment status under the GitHub Actions.
