# Properties Editor Version 1

This is an application written in [Python](https://www.python.org/) 
with [wxPython](https://wxpython.org/) 
and [PythonCard](http://pythoncard.sourceforge.net/), 
which work only with **Python 2.7** (because of **PythonCard**).

Because **Python 2.7** is obsolete, [another version](https://github.com/icoman/PropertiesEditor_v2) 
(which work both with **Python 2.7** and **Python 3.x**) of this application will be released soon and will use 
[ged](https://github.com/icoman/ged) with
[wxPython Phoenix](https://wxpython.org/) instead 
of [PythonCard](http://pythoncard.sourceforge.net/).

This application was created from a need to have a config editor for 
an [Application Web Server](https://github.com/icoman/AppServer) written in 
[Python](https://www.python.org/).

## A screenshot of application

![Properties Editor Version 1](screenshot.jpg)

A document created with this application is a [JSON](https://json.org/) file 
with **data** section used as application properties 
(acces module, DSN, admin notes, user config, config menu, ...) 
and **fields** section used as information definition of content of **data** entries.

The information from **fields** section is used to render 
the **html web config form editor** of 
[Application Web Server](https://github.com/icoman/AppServer).

## The default config generated for a web application

```json
{
  "data": {
    "10": {
      "description": "Write here whatever you need to remember about this module",
      "name": "admin notes",
      "posturl": "",
      "type": "textarea",
      "value": ""
    },
    "20": {
      "description": "Data Source Name",
      "name": "DSN",
      "posturl": "",
      "type": "text",
      "value": "protocol://user:password@host/database"
    },
    "30": {
      "description": "Enable or disable module execution",
      "name": "module disabled",
      "posturl": "",
      "type": "checkbox",
      "value": ""
    },
    "40": {
      "description": "Enable acces to user json config file",
      "name": "user config",
      "posturl": "",
      "type": "checkbox",
      "value": ""
    },
    "50": {
      "description": "Show link to module config and user config",
      "name": "config menu",
      "posturl": "",
      "type": "checkbox",
      "value": "yes"
    },
    "60": {
      "description": "List of groups who has acces to module",
      "name": "access module",
      "posturl": "/auth/groups/all",
      "type": "mc",
      "value": [
        "1",
        "2"
      ]
    }
  },
  "fields": {
    "10": [
      "name",
      []
    ],
    "20": [
      "description",
      []
    ],
    "30": [
      "type",
      [
        "text",
        "textarea",
        "password",
        "checkbox",
        "select",
        "mc"
      ]
    ],
    "40": [
      "value",
      []
    ],
    "50": [
      "posturl",
      [
        "",
        "/auth/groups/all",
        "/post1",
        "/post2",
        "/post3"
      ]
    ]
  }
}
```

which will generate an **html web form** like this:

![Default Application Config](appconfig.jpg)

## The application can also generate a user config 

```json
{
  "data": {
    "10": {
      "description": "test property 1",
      "name": "prop1",
      "posturl": "",
      "type": "text",
      "value": ""
    },
    "20": {
      "description": "test property 2",
      "name": "prop2",
      "posturl": "",
      "type": "checkbox",
      "value": ""
    },
    "30": {
      "description": "test property 3",
      "name": "prop3",
      "posturl": "",
      "type": "textarea",
      "value": ""
    }
  },
  "fields": {
    "10": [
      "name",
      []
    ],
    "20": [
      "description",
      []
    ],
    "30": [
      "type",
      [
        "text",
        "textarea",
        "password",
        "checkbox",
        "select",
        "mc"
      ]
    ],
    "40": [
      "value",
      []
    ],
    "50": [
      "posturl",
      [
        "",
        "/auth/groups/all",
        "/post1",
        "/post2",
        "/post3"
      ]
    ]
  }
}
```

which will generate an **html web form** like this:

![Default User Config](userconfig.jpg)









