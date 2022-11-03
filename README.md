To-Do List App
Description
Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small
town, so the mayor had a bright idea to limit the number of cars a person may possess. One
person may have up to 3 vehicles. The vehicle, registered to a person, may have one color,
‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’.
Carford car shop want a system where they can add car owners and cars. Car owners may
not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the
system without owners.

Requirements

● Setup the dev environment with docker
○ Using docker-compose with as many volumes as it takes
● Use Python’s Flask framework and any other library
● Use any SQL database
● Secure routes
● Write tests

Activate virtual enviroment

1. FLASK_ENV=development
2. FLASK_APP=carford.app:create_app

3.
Commands:
  add-user     Adds a new user to the database
  create-db    Creates database
  drop-db      Cleans database
  populate-db  Populate db with sample data
  routes       Show the routes for the app.
  run          Run a development server.
  shell        Runs a shell in the app context.


FLASK_DEBUG=True flask 'command name'

4. FLASK_DEBUG=True flask add-user -u username -p password


5. Routes

Endpoint                       Methods    Rule
-----------------------------  ---------  --------------------------------------------
_debug_toolbar.static          GET        /_debug_toolbar/static/<path:filename>
admin.index                    GET        /admin/
admin.static                   GET        /admin/static/<path:filename>
bootstrap.static               GET        /static/bootstrap/<path:filename>
car.action_view                POST       /admin/car/action/
car.ajax_lookup                GET        /admin/car/ajax/lookup/
car.ajax_update                POST       /admin/car/ajax/update/
car.create_view                GET, POST  /admin/car/new/
car.delete_view                POST       /admin/car/delete/
car.details_view               GET        /admin/car/details/
car.edit_view                  GET, POST  /admin/car/edit/
car.export                     GET        /admin/car/export/<export_type>/
car.index_view                 GET        /admin/car/
debugtoolbar.save_template     POST       /_debug_toolbar/views/template/<key>/save
debugtoolbar.sql_select        GET, POST  /_debug_toolbar/views/sqlalchemy/sql_explain
debugtoolbar.sql_select        GET, POST  /_debug_toolbar/views/sqlalchemy/sql_select
debugtoolbar.template_editor   GET        /_debug_toolbar/views/template/<key>
debugtoolbar.template_preview  POST       /_debug_toolbar/views/template/<key>
restapi.caritemresource        GET        /api/v1/car/<car_id>
restapi.carresource            GET        /api/v1/car/
simplelogin.login              GET, POST  /login/
simplelogin.logout             GET        /logout/
static                         GET        /static/<path:filename>
user.action_view               POST       /admin/user/action/
user.ajax_lookup               GET        /admin/user/ajax/lookup/
user.ajax_update               POST       /admin/user/ajax/update/
user.create_view               GET, POST  /admin/user/new/
user.delete_view               POST       /admin/user/delete/
user.details_view              GET        /admin/user/details/
user.edit_view                 GET, POST  /admin/user/edit/
user.export                    GET        /admin/user/export/<export_type>/
user.index_view                GET        /admin/user/
webui.carview                  GET        /car/<car_id>
webui.index                    GET        /



