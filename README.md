# Django Server

## Overview
This project is a Django-based web server that provides a RESTful API for managing products and users. It leverages Django's powerful ORM and the Django REST framework to create a robust and scalable backend. The server includes endpoints for creating, retrieving, updating, and deleting products and users, with support for filtering and querying.

## Core Technology
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST framework**: A powerful and flexible toolkit for building Web APIs.
- **Gunicorn**: A Python WSGI HTTP Server for UNIX, used to serve the Django application.
- **psycopg2-binary**: A PostgreSQL database adapter for Python.
- **python-dotenv**: Reads key-value pairs from a `.env` file and can set them as environment variables.
- **djangorestframework-simplejwt**: A JSON Web Token authentication backend for the Django REST Framework.
- **django-cors-headers**: A Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS).

## Postman
View and test API collection in postman, run:

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://god.gw.postman.com/run-collection/27476393-6cbfa15f-ff21-4478-84d9-8e664647425a?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D27476393-6cbfa15f-ff21-4478-84d9-8e664647425a%26entityType%3Dcollection%26workspaceId%3D82c53f50-c768-4ae4-8f30-f9cfdaffd9d9#?env%5BProduction%5D=W3sia2V5IjoidG9rZW4iLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0Iiwic2Vzc2lvblZhbHVlIjoiIiwiY29tcGxldGVTZXNzaW9uVmFsdWUiOiIiLCJzZXNzaW9uSW5kZXgiOjB9LHsia2V5IjoiY29sbGVjdGlvbk5hbWUiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0Iiwic2Vzc2lvblZhbHVlIjoiIiwiY29tcGxldGVTZXNzaW9uVmFsdWUiOiIiLCJzZXNzaW9uSW5kZXgiOjF9LHsia2V5IjoiY29sbGVjdGlvblNjaGVtYVVybCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQiLCJzZXNzaW9uVmFsdWUiOiIiLCJjb21wbGV0ZVNlc3Npb25WYWx1ZSI6IiIsInNlc3Npb25JbmRleCI6Mn0seyJrZXkiOiJhY2Nlc3NLZXkiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0Iiwic2Vzc2lvblZhbHVlIjoiIiwiY29tcGxldGVTZXNzaW9uVmFsdWUiOiIiLCJzZXNzaW9uSW5kZXgiOjN9LHsia2V5Ijoid29ya3NwYWNlSWQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0Iiwic2Vzc2lvblZhbHVlIjoiIiwiY29tcGxldGVTZXNzaW9uVmFsdWUiOiIiLCJzZXNzaW9uSW5kZXgiOjR9LHsia2V5IjoiY29sbGVjdGlvbklkIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCIsInNlc3Npb25WYWx1ZSI6IiIsImNvbXBsZXRlU2Vzc2lvblZhbHVlIjoiIiwic2Vzc2lvbkluZGV4Ijo1fSx7ImtleSI6InJlZnJlc2hfdG9rZW4iLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0Iiwic2Vzc2lvblZhbHVlIjoiIiwiY29tcGxldGVTZXNzaW9uVmFsdWUiOiIiLCJzZXNzaW9uSW5kZXgiOjZ9LHsia2V5IjoiYWNjZXNzX3Rva2VuIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCIsInNlc3Npb25WYWx1ZSI6IiIsImNvbXBsZXRlU2Vzc2lvblZhbHVlIjoiIiwic2Vzc2lvbkluZGV4Ijo3fSx7ImtleSI6ImVudlNldCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQiLCJzZXNzaW9uVmFsdWUiOiJwcm9kdWN0aW9uIiwiY29tcGxldGVTZXNzaW9uVmFsdWUiOiJwcm9kdWN0aW9uIiwic2Vzc2lvbkluZGV4Ijo4fV0=)