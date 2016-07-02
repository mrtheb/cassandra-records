cassandra-records
=================

**cassandra-records is a very simple, but powerful, library for making raw CQL queries
to Cassandra (and only Cassandra).**

*It is obviously a blatant copy of the very competent Records library by Kenneth Reitz*


☤ The Basics
------------
We know how to write CQL, so let's send some to our database:

.. code:: python

    import records

    db = records.Database(hosts="10.2.3.4,10.2.3.5", username='cassandra', password='cassandra')
    rows = db.query('select * from active_users')    # or db.query_file('cqls/active-users.cql')


Grab one row at a time:

.. code:: python

    >>> rows[0]
    <Record {"username": "model-t", "active": true, "name": "Henry Ford", "user_email": "model-t@gmail.com", "timezone": "2016-02-06 22:28:23.894202"}>

Or iterate over them:

.. code:: python

    for r in rows:
        print(r.name, r.user_email)

Values can be accessed many ways: ``row.user_email``, ``row['user_email']``, or ``row[3]``.

Fields with non-alphanumeric characters (like spaces) are also fully supported.

Or store a copy of your record collection for later reference:

.. code:: python

    >>> rows.all()
    [<Record {"username": ...}>, <Record {"username": ...}>, <Record {"username": ...}>, ...]

Other options include ``rows.as_dict()`` and ``rows.as_dict(ordered=True)``.

☤ Features
----------

- Iterated rows are cached for future reference.
- Convenience ``Database.get_table_names`` method.
- Command-line `cassanrda-records` tool for exporting queries.
- Safe parameterization: ``Database.query('life=:everything', everything=42)``
- Queries can be passed as strings or filenames, parameters supported.

Records is powered by the `Datastax Cassandra driver <http://datastax.github.io/python-driver/>`_
and `Tablib <http://docs.python-tablib.org/en/latest/>`_.

☤ Data Export Functionality
---------------------------

Records also features full Tablib integration, and allows you to export
your results to CSV, XLS, JSON, HTML Tables, or YAML with a single line of code.
Excellent for sharing data with friends, or generating reports.

.. code:: pycon

    >>> print(rows.dataset)
    username|active|name      |user_email       |timezone
    --------|------|----------|-----------------|--------------------------
    model-t |True  |Henry Ford|model-t@gmail.com|2016-02-06 22:28:23.894202
    ...

**Comma Separated Values (CSV)**

.. code:: pycon

    >>> print(rows.export('csv'))
    username,active,name,user_email,timezone
    model-t,True,Henry Ford,model-t@gmail.com,2016-02-06 22:28:23.894202
    ...

**YAML Ain't Markup Language (YAML)**

.. code:: python

    >>> print(rows.export('yaml'))
    - {active: true, name: Henry Ford, timezone: '2016-02-06 22:28:23.894202', user_email: model-t@gmail.com, username: model-t}
    ...

**JavaScript Object Notation (JSON)**

.. code:: python

    >>> print(rows.export('json'))
    [{"username": "model-t", "active": true, "name": "Henry Ford", "user_email": "model-t@gmail.com", "timezone": "2016-02-06 22:28:23.894202"}, ...]

**Microsoft Excel (xls, xlsx)**

.. code:: python

    with open('report.xls', 'wb') as f:
        f.write(rows.export('xls'))

You get the point. All other features of Tablib are also available,
so you can sort results, add/remove columns/rows, remove duplicates,
transpose the table, add separators, slice data by column, and more.

See the `Tablib Documentation <http://docs.python-tablib.org/en/latest/>`_
for more details.

☤ Installation
--------------

Not published on pypi, not sure if it will ever be. Install with `pip` from this repo.

☤ Thank You
-----------

Thanks for checking this library out! I hope you find it useful.

Of course, there's always room for improvement. Feel free to `open an issue <https://github.com/mrtheb/cassanrda-records/issues>`_ so we can make it better, stronger, faster.


