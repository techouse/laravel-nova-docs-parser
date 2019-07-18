# Laravel Nova docs parser

## Requirements:

- Python 3.4+
- Node.js
- Git

## Installation and usage
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
sh get_docs.sh
python parser.py
```

The above commands will make a virtual environment in a folder called `env` and install all the requirements listed in `requirements.txt` into that virtual environment.
Once that is done running `sh get_docs.sh` will `clone` the `git` repository of [laravel/nova-docs](https://github.com/laravel/nova-docs) and build the Laravel Nova HTML documentation using [vuejs/vuepress](https://github.com/vuejs/vuepress).
Then running `python parser.py` will parse that documentation.
It will output a file called `data.json` which you can later use to your avail.

The output JSON file looks like this:
```json
[
  {
    "version": 2.0,
    "id": "trix-field",
    "title": "Trix Field",
    "permalink": "https://nova.laravel.com/docs/2.0/resources/fields.html#trix-field",
    "categories": [
        "Fields"
    ],
    "content": "The Trix field provides a Trix editor for its associated field. Typically, this field will correspond to a TEXT column in your database. The Trix field will store its corresponding HTML within the associated database column:"
  }
]
```
