## Django things



- `reverse` from `django.urls.reverse` used to create a dynamic url for any route

- `redirect` from `django.urls.redirect` used to redirect to anyy given url 



Must return 404 response when some error rendering a error template may work but it will return the 200 response.

django provide us a method to convert template as a string and return it as `HttpResponseNotFound` error.

```python
from django.template.loader import render_to_string
rendered = render_to_string('my_template.html', {'foo': 'bar'})
```

## Linking CSS files into Django Template
