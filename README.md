# Order Details CRUD API
## A live link to the application (json file)
<a href="https://iftynibir.pythonanywhere.com/orders.json">https://iftynibir.pythonanywhere.com/orders.json<a/>
## Ways to set up and run projects.
1. First, you need to install Python and pip on your local machine
2. Create a folder and open the terminal in that folder
3. Create a virtual environment using the terminal. For example, the environment name is "env"
```bash
python -m venv env 
```
4. Activate the environment
```bash
env\Scripts\activate
```
5. Now you need to clone the repository.
```bash
git clone https://github.com/IftakhirNibir/Order_CRUD_API.git 
```
6. Open the project folder
```bash
cd Order_CRUD_API
```
7. Install the required prerequisites using
```bash
pip install -r requirement.txt
```
8. Open "OrdersAPI" folder
```bash
cd OrdersAPI
```
9. Now run the server
```bash
py manage.py runserver
```
10. Open the browser and go 
```bash
http://127.0.0.1:8000/orders.json
```
This link shows us all order details in a JSON file
11. If we want to get a piece of specific order information we need to open the browser and write product_id
```bash
http://127.0.0.1:8000/order_detail/{product_id}.json
```
12. To see the API Documentation then go to this link 
```bash
http://127.0.0.1:8000/swagger/
```
## To test API endpoints
1. Go to the main project folder and open another terminal then activate the virtual environment and write for install jupyter notebook
```bash
pip install notebook
```
2. Open the project folder
```bash
cd Order_CRUD_API
```
3. Open Jupyter Notebook by writing
```bash
jupyter notebook
```
4. Select Testing_API.ipynb file and run all 

