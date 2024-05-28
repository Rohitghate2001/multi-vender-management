Multi vender Management system

<b>Introduction:</b>

The multi Vendor Management System, developed using Django,django_rest_framework is a web application.</br>

It encompasses functionalities for managing vendor profiles, tracking purchase orders, and evaluating vendor performance.

Users can create, update, and delete vendor profiles, monitor purchase orders, and assess vendor performance metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.

Features****</br>
User/Admin can add or remove vendors</br>
can get vender list</br>
can get information of specific vender</br>
Easy to use</br>
API endpoints can be checked using Django ORM</br>
No need of any tools is needed for API endpoints checking.</br>


****API Reference

Vendor Profile Management:</br>
  POST /api/vendors/: Create a new vendor.</br>
  GET /api/vendors/: List all vendors.</br>
  GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.</br>
  PUT /api/vendors/{vendor_id}/: Update a vendor's details.</br>
  DELETE /api/vendors/{vendor_id}/: Delete a vendor.</br>
</br>
Purchase Order Tracking:</br>
  POST /api/purchase_orders/: Create a purchase order.</br>
  GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.</br>
  GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.</br>
  PUT /api/purchase_orders/{po_id}/: Update a purchase order.</br>
  DELETE /api/purchase_orders/{po_id}/: Delete a purchase order</br>

****Technologies Used</br>
python ,django ,sqlite3</br>


Installation Process****</br>

python -m venv env_name</br>

source venv/Scripts/activate</br>

pip install django</br>

pip install djangorestframework</br>

python manage.py makemigrations </br>

python manage.py migrate</br>

python manage.py createsuperuser </br>

python manage.py runserver</br>

http://localhost:8000/vendors/  --for vendor list</br>

http://localhost:8000/admin  --for admin</br>



<b>Screenshots</b>

venderList
![Screenshot (317)](https://github.com/Rohitghate2001/multi-vender-management/assets/147127996/b05b4e47-75f8-44ab-81db-21ca84d833d5)


Specific vender details by vender id
![Screenshot (318)](https://github.com/Rohitghate2001/multi-vender-management/assets/147127996/ab00a998-320d-4968-88fc-4f2ae630dbbb)


purchase orderds
![Screenshot (316)](https://github.com/Rohitghate2001/multi-vender-management/assets/147127996/cf0937c6-a845-461d-8bbb-389d8bb0f261)


purchase order by specific order id
![Screenshot (319)](https://github.com/Rohitghate2001/multi-vender-management/assets/147127996/9cdeaa9a-d122-4301-beb2-467707c5aeca)









