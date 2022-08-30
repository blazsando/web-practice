# Web practice project


## Tasks

1. Change the root route design. Instead of a plain text, render a predefined html template
- Use render template

2. Introduce template inheritance
- Make new template: home.html
- modify index template that the content in the section is a content block
- load the originial content from indexgit  with content block in home.html

3. Welcome visitor with name
- Add new route to home method '/home/<user>'
- use route param
- pass route param to render template
- display user name with jinja syntax

4. New button on page displaying shop categories
- add new button in navbar using the url-for syntax
- on the new template display a button for each shop category from the data.py file

5. Add a form that has all the brands listed that can be found in the given category
- use input select and options
- use list and dictionary functions (keys, values, items etc)