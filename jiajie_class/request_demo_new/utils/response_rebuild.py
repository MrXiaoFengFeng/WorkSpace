import json

import requests


class ResponseObject(object):

    def __init__(self, resp_obj):
        """ initialize with a requests.Response object
        Args:
            resp_obj (instance): requests.Response instance
        """
        self.resp_obj: requests.Response = resp_obj

    def __getattr__(self, key):
        try:
            if key == "json":
                value = self.resp_obj.json()
            elif key == "cookies":
                value = self.resp_obj.cookies.get_dict()
            elif key == "request_body":
                body = self.resp_obj.request.__dict__.get("body").decode("utf-8")
                value = json.loads(body)
            elif key == "request_cookies":
                cookie = dict(self.resp_obj.request.__dict__.get("_cookies"))
                value = cookie
            elif key == "request_headers":
                headers = self.resp_obj.request.__dict__.get("headers")
                value = headers
            else:
                value = getattr(self.resp_obj, key)

            self.__dict__[key] = value
            return value
        except AttributeError:
            err_msg = "ResponseObject does not have attribute: {}".format(key)
            # logger.log_error(err_msg)
            raise Exception(err_msg)