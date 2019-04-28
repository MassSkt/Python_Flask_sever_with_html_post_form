# About
This is a basic template for uploading jason value or files to Python flask sever through html form.
The result from python sever is displayed to the html form with Ajax.
Any data processing such as machine learning with Python can be added to the Python code.


# How to use

Launch Flask sever.
```
python flask_app.py
```

open html file.
 - js_ajax_file.html : This is for uploading image file to flask sever. The url should be http://localhost:5050/prediction-post-file
   After uploading. The flask saves the uploaded file as "test.jpg"
 - js_ajax_file.html : This is for posting values to flask server.The returned result is as is the posted values.
 