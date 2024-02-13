# KaiznTree Take Home Challenge

## Download the code

```
https://github.com/Nachiket18/kaizn.git
```

## Please set up the virtual environment using the following link

```
https://docs.python.org/3/library/venv.html
```

## Install the required packages

```
pip install -r requirements. txt
```

## Run the Code
Start the Djnago server using the following command. We have tested the API endpoints using httpie (which will be installed using requirements.txt)
```
python manage.py runserver
```
## Testing API's
Now the server has started so open a new terminal window.

1. We have to register the user to use the application- ```http POST http://127.0.0.1:8000/register/ kai_email='kai@gmail.com' kai_password='kaiznoffice' ``` 
2. To test whetehr the user has been created, please login - ``` http POST http://127.0.0.1:8000/login/ username='kai@gmail.com' password='kaiznoffice' ```
3. This command will add a item to the database
   ```http POST http://127.0.0.1:8000/add_item/ kai_SKU='125' kai_Name='Wilson Tennis' kai_Category='Sports Goods' kai_instock=10 kai_available_stock=10 Tags='Equipments' ```
4. To display all the items in the database ``` http GET http://127.0.0.1:8000/dashboard/ ```


