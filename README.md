# Docs Convert

The **Docs Convert** is a web application for converting a document. It was built using [Django web framework](https://www.djangoproject.com/)

## Current Features

- Image to PDF converter
- Multiple Images to single PDF
- Document(.doc/.docx) to PDF
- No documents will be saved. It will be removed Once the user visits **Home Page**

## Upcoming Features

- PDF to Audio

## Screenshots

#### Home Page

![Home-Page](https://i.imgur.com/dBEfrGs.png)

#### Image to PDF convert Page

![Image-To-PDF-Page](https://i.imgur.com/zCQvAdj.png)

#### After successfull Image convertion to PDF

![Successfull-Image-Convertion-To-PDF](https://i.imgur.com/4uTiDEX.png)

## Run Locally

Clone the project

```bash
  git clone https://github.com/Gokulancv10/document-converter.git
```

Go to the project directory

```bash
  cd <folder_name>
```

Create a Virtual Environment

```bash
  virtualenv venv
```

Activating Virtual Environment

```bash
  venv\Scripts\activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```

## Tech Stack

**Client:** HTML5, CSS3

**Server:** Python-v3.9, Django-v3.2
