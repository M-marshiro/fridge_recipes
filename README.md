# Web dev - Project

This is a intro project for webdev. We will make a website that is like this: [https://www.myfridgefood.com/](https://www.myfridgefood.com/) - a website that gives you recipes based on the ingredients you have. (but in vietnamese, maybe). On the way, we will probably learn about some helpful dev tools. If it's optional, you dont have to do it, but I strongly recommend it.

## Week 1 - Setting up environment

You might have done/learned some parts of this, that's fine, just make sure you have the whole thing set up. This is to ensure we all have the same starting point.

***NOTE:*** rule of thumb - looks for answers online if you're stuck. if you cant find the answer after 20 minutes, ask.

### 1. Set up WSL (Windows subsystem for linux) 

-> [HOW TO](https://learn.microsoft.com/en-us/windows/wsl/install)

### 2. Install editor:

- install VS Code
- install WSL extension.
- install Python Extension.

Make sure you can open and edit files in wsl in VSCode. This is your editor. (You dont have to if you're planning on to use something else).

To Open files in wsl in vscode:

- Click the bottom left button. Select "Connect to WSL".
- Click "File" on top left. Select "Open Folder" or "Open file".

### 3. install TMUX [Optional]

- To install, use command: `sudo apt install tmux`
- What is this? A very useful session manager.
> tmux is a program which runs in a terminal and allows multiple other terminal programs to be run inside it. Each program inside tmux gets its own terminal managed by tmux, which can be accessed from the single terminal where tmux is running - this called multiplexing and tmux is a terminal multiplexer.
- What does that mean? that means if i want to get a new terminal, I dont have to open up a new one and ssh/login again. I can just open new "window" or split panes. - very useful once you get used to the few basic commands.
- `Ctrl + b` and then `%` for example to split vertically.
- every command has `Ctrl + b` prefix. [Cheat Sheet for commands](https://tmuxcheatsheet.com/)
- [DOCS](https://github.com/tmux/tmux/wiki/Getting-Started)
- Try to use it. It might be slow at first but it is great.

### 4. Install zsh [Optional]

- To install, use command: `sudo apt install zsh` and then `chsh -s $(which zsh)` to set it as default.
- What is this? A modern powerful teminal shell. You will need to get used to a terminal and a modern one is better.
- ^ The above should have been enough. But if you really want to use it to the power that it can: read and follow [THIS](https://github.com/ohmyzsh/ohmyzsh?tab=readme-ov-file#basic-installation)
- Choose a theme you like: [HERE](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)
- Choose plugins you want: [HERE](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins). (There's a lot) Here are the ones I recommend: `(history git npm nvm pip python)`

### 5. Install Python

- in WSL, install Python 3.12 -> [GUIDE](https://www.debugpoint.com/install-python-3-12-ubuntu/)

### 6. VirtualEnv

- in WSL: `pip install virtualenv` -> [Docs](https://virtualenv.pypa.io/en/latest/). Why do we need it? Here:
> The basic problem being addressed is one of dependencies and versions, and indirectly permissions. Imagine you have an application that needs version 1 of LibFoo, but another application requires version 2. How can you use both these libraries? If you install everything into your host python (e.g. python3.8) it’s easy to end up in a situation where two packages have conflicting requirements.

> Or more generally, what if you want to install an application and leave it be? If an application works, any change in its libraries or the versions of those libraries can break the application. Also, what if you can’t install packages into the global site-packages directory, due to not having permissions to change the host python environment?

> In all these cases, virtualenv can help you. It creates an environment that has its own installation directories, that doesn’t share libraries with other virtualenv environments (and optionally doesn’t access the globally installed libraries either).

- make a new virtual environment in this directory: `virtualenv venv`
- activate the virtual environment: `source venv/bin/activate` - `source` is just the command to execute the file in the current shell.
- install Django: `pip install 'Django>=5.0'`

### 7. Git

- install git on WSL: `sudo apt install git-all` -> [DOCS](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- set up your ssh key on github: [GUIDE](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=webui)

## Week 2 - Django and DRF.

All of the below should be done in a branch of your own. Create a branch and commit and push to that branch so that I can read and review.

### 1. Use virtual env

- `virtualenv venv`
- To activate the venv, do: `source venv/bin/activate`
- Install Django and django-rest-framework: `pip install django djangorestframework`

What is Django? A framework for API dev that is used for convenience. It is a "battery-included" type of framework. Described as a "shark" - old but powerful and reliable.

Django Rest Framework (DRF): A powerful toolkit for building Web APIs with Django. It provides components like serializers, viewsets, and routers to simplify API development.

#### Understanding RESTful API

REST (Representational State Transfer) is an architectural style for designing networked applications. It uses HTTP requests to perform CRUD operations on resources, which are represented as URLs. REST APIs are stateless and leverage standard HTTP methods:

- GET: Retrieve data.
- POST: Create new data.
- PUT: Update existing data.
- DELETE: Remove data.

### 2. Start new project

```bash
django-admin startproject fridge_recipes .
python manage.py runserver
```

- Open the fridge_recipes directory in vs code.
- Use browser to see the starting page at `http://localhost:8000/` (You might see some warning. Ignore that for now.)

Add the App to Your Project: Open `fridge_recipes/settings.py` and add `fridge_recipes` (or whatever name you chose) and `rest_framework` to the INSTALLED_APPS list:

```python
INSTALLED_APPS = [
    ...
    "fridge_recipes",
    'rest_framework',
]
```

### 3. Define models

#### Concept Explanation

Django ORM (Object-Relational Mapping): Django’s ORM allows you to interact with your database using Python code instead of raw SQL queries. The ORM translates Python code into SQL queries and helps you manage database records as Python objects. This also helps in that we can skip learning SQL for now.

**Models**: In Django, a model is a Python class that defines the structure of a database table. Each model class represents a table in the database, and the attributes of the class represent columns in that table. Django’s ORM handles the interaction with the database for you. [READ MORE HERE](https://docs.djangoproject.com/en/5.1/topics/db/models/).

**Migrations**: Migrations are Django’s way of propagating changes you make to your models into the database schema. They are a way to keep your database schema synchronized with your models. This mean

**Fields**: Django models use various field types to represent different kinds of data. Examples include:
- CharField: For short text.
- TextField: For long text.
- DateTimeField: For date and time.

**Relationships**: Models can define relationships with other models using fields like:
- ForeignKey: Links one model to another, creating a many-to-one relationship.
- ManyToManyField: Allows for many-to-many relationships.
- OneToOneField: Creates a unique relationship between models.

**Methods**: You can define methods on models to add custom behavior. The __str__ method is commonly used to return a readable string representation of the model instance.

#### Model design and implementation

What do we need to design? Think about the following requirements and decide. We need:

- recipes
- recipe has ingredient and amount required for that ingredient
- recipe requires equipment (sometimes)

You can think about other attributes/requirements that you would want in this app. May be we want recipe to be split by cuisine types. That kind of thing, go on and think. Implement your models in `fridge_recipes/models.py`.

Here is an example `models.py` of a blog api.

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
```

#### Migrations

After defining your models, you need to create and apply migrations.

- What Are Migrations?: Migrations are files that describe changes to your models and how to apply these changes to the database schema. They are like version control for your database schema.
- `makemigrations` Command: This command generates migration files based on the changes you made to your models. These files are stored in the migrations directory of your app and describe the operations to be performed on the database (e.g., creating tables, adding fields). `python manage.py makemigrations fridge_recipes`
- What Is Applying Migrations?: Applying migrations updates the database schema to match the current state of your models. It executes the operations described in the migration files.
- `migrate` Command: This command applies any unapplied migrations to the database. It ensures that the schema is in sync with your models by executing the necessary SQL commands. `python manage.py migrate`


### 4. Define Serializers

This is a **DRF** concept. What is a Serializer for? Validating and converting data between Python objects and JSON. 

```
db -> python -> serializer -> json
json -> serializer -> python -> db
```

Create a serializer for each of your models. Example, for the blog api like above. This should be in `fridge_recipes/serializers.py`.

```python
from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'comments']
```

Explanation: 
- `Meta` means this is information about the class itself (in this case, the PostSerializer for example.)
- `model` is the model we use this serializer for
- `fields` is the list of fields we want to serialize

When in doubt, [read the documentation.](https://www.django-rest-framework.org/api-guide/serializers/)

### 5. Create API Views with ViewSets

What is a ViewSet?: A ViewSet is a special class in DRF that provides a way to handle CRUD operations for a model with minimal code. It combines common view functionalities into a single class, allowing you to handle list, create, retrieve, update, and delete operations. [READ MORE HERE](https://www.django-rest-framework.org/api-guide/viewsets/).

Benefits: ViewSets reduce boilerplate code and are often used with DRF’s routers, which automatically generate URLs for the CRUD operations provided by the ViewSet.

ModelViewSet: Provides default implementations for the typical CRUD operations. It’s a commonly used viewset that integrates well with DRF’s routers.

Example, for the blog api:

```python
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
```

Explanation:

- `ModelViewSet`: Inherits from ModelViewSet, which provides default implementations for list, create, retrieve, update, and delete actions.
- `queryset`: Specifies the set of Post objects to be used.
- `serializer_class`: Specifies the PostSerializer to handle serialization and deserialization of Post instances.

As before, make a viewset for each model you have, put them in `fridge_recipes/viewsets.py`. Once you have that ready, let's configure urls with routers.
In `fridge_recipes/urls.py`, configure the router like:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```
Explanation of Example:

- `DefaultRouter`: Automatically generates URL patterns for the registered viewsets.
- `register`: Registers the PostViewSet and CommentViewSet with the router. The URLs will be automatically generated for list, create, retrieve, update, and delete actions.
- `include(router.urls)`: Includes the generated URL patterns in the app’s URL configuration.

Now when you run `python manage.py runserver` and go to `http://localhost:8000/`, you should see all the endpoint you created. You can try to create some data using the forms there.
