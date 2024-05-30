# Order Details CRUD API
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
cd OrderAPI
```
7. Install the required prerequisites using
```bash
pip install -r requirement.txt
```
8. Now run the server
```bash
py manage.py runserver
```
9. Open the browser and go 
```bash
http://127.0.0.1:8000/orders.json
```
This link shows us all order details in a JSON file
10. If we want to get a piece of specific order information we need to open the browser and 
```bash
http://127.0.0.1:8000/order_details/{product_id}.json
```
