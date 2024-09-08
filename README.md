# SAM Python Lambda Layers Template

An empty SAM template project integrated with the python project structure allowing seemless local development and remote deployment.

## HOW TO USE THIS TEMPLATE

> **DO NOT FORK**  **[Use the template](https://github.com/m6freeman/python_project_template/generate)** 

### What is included on this template?

```sh 
 .
 ├── events                           # Files for simulated events
 │  └── response.json
 ├── hello_world                      # Each Lambda function handler in it's own directory
 │  ├── app.py                        # The function handler itself
 │  └── requirements.txt              # Dependancies of the function hander
 ├── layers
 │  ├── bin                           # Deployed as a separate Layer
 │  │  └── requirements.txt           # Imports all project service dependancies
 │  └── project_layer
 │     └── python
 │        └── project_modules         # Built as a pyproject for local development
 │           ├── module.py
 │           └── requirements.txt     # Dependencies for project_modules
 ├── tests
 │  ├── unit                          # Functional Unit tests
 │  │  └── test_handler.py
 │  └── requirements.txt
 ├── pyproject.toml                   # Install layers as pyproject for local development
 ├── README.md
 ├── requirements.txt                 # Local development dependencies and imports layers/bin/requirements.txt
 └── template.yaml                    # Define your SAM resources
```

### Installation

Create new SAM project by cloning template into a new local project repository.

```sh git
git clone https://github.com/m6freeman/sam-python-lambda-layer-template my_sam_project
cd my_sam_project; rm -rf .git; git init
```

---

# project_name

project_description

## Usage

### Establish project virtual environment

```sh
python -m venv .venv
. ./.venv/bin/activate
pip install -r requirements.txt
```

### Manage layers project and install layers as a pyproject for local development

```toml pyproject.toml
[tool.setuptools.packages.find]
where = ["layers/project_layer/python/"]
include = ["project_modules"]

[project]
name = "project_modules"
```

```sh
pip install -e .
```

### Manage SAM Resources

```yaml template.yaml
HelloWorldFunction:
  Type: AWS::Serverless::Function
  Properties:
    Handler: app.lambda_handler
    CodeUri: hello_world
    Description: Hello World function
    Architectures:
      - x86_64
    Tracing: Active
    Layers:
      - !Ref ProjectLayer
      - !Ref ProjectLibraryLayer
```

### Manage local project dependancies

```txt requirements.txt
-r layers/bin/requirements.txt
aws-sam-cli
...
```

### Manage deployed project dependancies

```txt layers/bin/requirements.txt
-r layers/project_layer/python/project_modules/requirements.txt
-r hello_world/requirements.txt
```

### Build and Deploy

```sh
sam build
sam deploy --guided
```

