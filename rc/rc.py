import click
import json
import requests
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/home/aj/git/convox/sample-api-app/convox.log',
                    filemode='w')


class RequestError(Exception):
    pass


class RestAPI:
    def __init__(self, base_url, headers={}):
        self.url = base_url

    def get(self, params):

        logging.debug("getting: {}... ".format(self.url + params))
        url = "{}".format(self.url + params)

        req = requests.get(self.url + params, headers=self.headers)
        if req.ok:
            return json.loads(req.content)

        raise RequestError("{} // {}/{}"
                           .format(url, req.status_code, req.reason))

    def post(self, data, params):
        """ send a POST request """
        url = "{}".format(self.url + params)
        click.secho("posting: {} ".format(url), fg='blue', nl=False)

        try:
            req = requests.request('post',
                                   url,
                                   json=data,
                                   headers=self.headers)

            if req.ok:
                click.secho("OK", fg='green')
                return json.loads(req.content)
            else:
                click.secho("NOK: {}".format(req.reason), fg='red')
                return json.loads(req.content)

        except requests.exceptions.ConnectionError, m:
            click.secho("NOK: {}".format(m), fg='red')

        raise RequestError("{} // {}/{}"
                           .format(url, req.status_code, req.reason))

