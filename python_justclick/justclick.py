# -*- coding: utf-8 -*-

import urllib
import hashlib
import requests
import collections


def http_build_data(data):
    dct = collections.OrderedDict()

    for key, value in data.iteritems():
        if isinstance(value, basestring):
            dct[key] = unicode(value).encode('utf-8')
        elif isinstance(value, list):
            for index, v in enumerate(value):
                dct['{0}[{1}]'.format(key, index)] = unicode(v).encode('utf-8')

    return dct


class JustClickConnection(object):

    _api_key = None
    _api_username = None
    _api_url = None

    def __init__(self, api_username, api_key):
        self._api_username = api_username
        self._api_key = api_key
        self._api_url = "http://%s.justclick.ru/api/" % api_username

    def _get_hash(self, data):
        """Формирует контрольную сумму

        md5("{$params}::{$user_id}::{$secret}")

        :param data: передаваемые данные
        :return: MD5 контрольная сумма
        """
        data_string = u"%s::%s::%s" % (urllib.urlencode(data), self._api_username, self._api_key)
        return hashlib.md5(data_string).hexdigest()

    def _build_url(self, path):
        return "%s%s" % (self._api_url, path)

    def _send_request(self, url, data):
        """ Отправляет запрос с API и получает ответ

        http://support.justclick.ru/index.php?/Knowledgebase/Article/View/37/5/obshhie-principy-rboty-s-api-servis-dzhstklik
        http://support.justclick.ru/index.php?/Knowledgebase/Article/View/34/5/sttusy-otvet-api-servis-ikh-kody-i-opisnija

        :param url: URL на кототорый отправляем запрос
        :param data: передаваемые данные
        :return: словарь с ответом от сервера
        """

        data.update({
            'hash': self._get_hash(data)
        })

        r = requests.post(url, data=data)

        return r.json()

    def add_lead_to_group(self, rids, lead_email, extra=None):
        """Добавление подписчика в группы (AddLeadToGroup)

        http://support.justclick.ru/index.php?/Knowledgebase/Article/View/36/5/dobvlenie-podpischik-v-gruppy-funkcija-api-servis-addleadtogroup

        :param rids: список групп
        :param lead_email: e-mail подписчика
        :param extra: дополнительные параметры (подробнее в документации к API)
        :return: словарь с ответом сервера
        """
        url = self._build_url('AddLeadToGroup')

        data = collections.OrderedDict()
        data.update({
            'rid': rids,
            'lead_email': lead_email,
        })

        if extra is not None:
            data.update(extra)

        data = http_build_data(data)

        return self._send_request(url, data)
