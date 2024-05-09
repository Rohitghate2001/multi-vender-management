Multi vender Management system

<b>Introduction:</b>

The multi Vendor Management System, developed using Django,django_rest_framework is a web application.

It encompasses functionalities for managing vendor profiles, tracking purchase orders, and evaluating vendor performance.

Users can create, update, and delete vendor profiles, monitor purchase orders, and assess vendor performance metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.

Features****
User/Admin can add or remove vendors
can get vender list
can get information of specific vender
Easy to use
API endpoints can be checked using Django ORM
No need of any tools is needed for API endpoints checking.


****API Reference

Vendor Profile Management:
  POST /api/vendors/: Create a new vendor.
  GET /api/vendors/: List all vendors.
  GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
  PUT /api/vendors/{vendor_id}/: Update a vendor's details.
  DELETE /api/vendors/{vendor_id}/: Delete a vendor.

Purchase Order Tracking:
  POST /api/purchase_orders/: Create a purchase order.
  GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
  GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
  PUT /api/purchase_orders/{po_id}/: Update a purchase order.
  DELETE /api/purchase_orders/{po_id}/: Delete a purchase order

****Technologies Used
python ,django ,sqlite3


Installation Process****

python -m venv env_name

source venv/Scripts/activate

pip install django

pip install djangorestframework

python manage.py makemigrations 

python manage.py migrate

python manage.py createsuperuser 

python manage.py runserver

http://localhost:8000/vendors/  --for vendor list

http://localhost:8000/admin  --for admin



<b>Screenshots</b>

venderList
![Screenshot (317)](https://github.com/Rohitghate2001/multi-vender-management/assets/147127996/b05b4e47-75f8-44ab-81db-21ca84d833d5)


Specific vender details by vender id
![Screenshot (318)](https://github.com/Rohitghate2001/multi-vender-management/assets/147127996/ab00a998-320d-4968-88fc-4f2ae630dbbb)


purchase orderds
![Screenshot (316)](https://github.com/Rohitghate2001/multi-vender-management/assets/147127996/cf0937c6-a845-461d-8bbb-389d8bb0f261)


purchase order by specific order id
![Screenshot (319)](https://github.com/Rohitghate2001/multi-vender-management/assets/147127996/9cdeaa9a-d122-4301-beb2-467707c5aeca)









