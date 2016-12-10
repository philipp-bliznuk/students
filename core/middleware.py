from django.db import connection


CONTENT_TYPES = ('text/plain', 'text/html')


class SqlRequests(object):
    def process_response(self, request, response):
        if request.META['CONTENT_TYPE'] not in CONTENT_TYPES:
            return response

        queries = connection.queries
        time = sum([float(query['time']) for query in queries])
        count = len(queries)

        res = '''<div class="container">
        <footer class="footer">
          <div class="container">
            <p class="text-center">
            Queries time: %(time)s sec. | Queries count: %(count)s
            </p>
          </div>
        </footer>
        </div>\n</body>''' % {'time': time, 'count': count}
        response.content = response.content.replace('</body>', res)
        return response
