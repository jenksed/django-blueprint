# Django-Blueprint

A Django 2.0+ project template to kickstart any development project, and get up and running quickly.

### Prerequisites & Setup

* [Python](https://www.python.org/downloads/) - Python 3.4 or newer
* [PIP](https://pip.pypa.io/en/stable/installing/) - Python package manager

1. Create a virtual environment
```
python3 -m venv /path/to/your/virtualenv/<name_of_venv>
```
2. Activate the virtual environment
   - Linux / Mac
```
source /path/to/your/virtualenv/<name_of_venv>/bin/activate
```
3. Install Django
```
pip3 install django
```
4. Start a new project
```
django-admin.py startproject --template=https://github.com/SquirrelBrain/django-blueprint/archive/master.zip --extension=py,html name_of_project
cd name_of_project
```
### License

Django-Blueprint is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) for more information.