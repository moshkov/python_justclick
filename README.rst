python_justclick
================
https://github.com/moshkov/python_justclick

.. image:: https://img.shields.io/pypi/v/python_justclick.svg
    :target: https://pypi.python.org/pypi/python_justclick

.. image:: https://img.shields.io/pypi/dm/python_justclick.svg
    :target: https://pypi.python.org/pypi/python_justclick

.. image:: https://img.shields.io/pypi/l/python_justclick.svg
    :target: https://pypi.python.org/pypi/python_justclick


Зависимости
-----------

- Python 2.7+
- requests


Установка
---------

.. code-block:: bash

    $ pip install python_justclick

Если используется Django, то в настройках проекта можно указать JUSTCLICK_USERNAME и JUSTCLICK_API_KEY.


Описание
--------

*Python JustClick API*

Позволяет работать с API JustClick. В текущей версии реализовано добавление подписчика в группы (AddLeadToGroup) и проверка статуса членства подписчика в группах (GetLeadGroupStatuses).

- JustClick: http://justclick.ru/
- Описание API: http://help.justclick.ru/archives/category/api


Использование
-------------

.. code-block:: python

    from python_justclick.justclick import JustClickConnection

    justClickConnection = JustClickConnection('YOU_JUSTCLICK_USERNAME', 'YOU_JUSTCLICK_API_KEY')

    result = justClickConnection.add_lead_to_group(['group1', 'group2'], 'lead@email.local', {
        "doneurl2": "https://your-site.local/success",
        "lead_name": "Vasya Pupkin",
    })

    if result['error_code'] == 0:
        print 'success'

    ...

Для Django (если в настройках заданы JUSTCLICK_USERNAME и JUSTCLICK_API_KEY):

.. code-block:: python

    from python_justclick.python_justclick_django import justClickConnection

    result = justClickConnection.add_lead_to_group(['group1', 'group2'], 'lead@email.local', {
        "doneurl2": "https://your-site.local/success",
        "lead_name": "Vasya Pupkin",
    })

    if result['error_code'] == 0:
        return HttpResponseRedirect(reverse('thanks'))

    ...


TODO
----

1. Проверка отвера API на корректность
2. Остальной функционал API JustClick
3. Тесты
4. Документация
