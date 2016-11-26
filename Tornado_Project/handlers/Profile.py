# coding:utf-8

import logging
import config

from .BaseHandler import BaseHandler
from utils.image_storage import storage
from utils.common import require_logined
from utils.response_code import RET


class AvatarHandler(BaseHandler):
    """头像"""
    @require_logined
    def post(self):
        user_id = self.session.data["user_id"]
        try:
            avatar = self.request.files["avatar"][0]["body"]
        except Exception as e:
            logging.error(e)
            return self.write(dict(errno=RET.PARAMERR, errmsg="参数错误"))
        try:
            img_name = storage(avatar)
        except Exception as e:
            logging.error(e)
            img_name = None
        if not img_name:
            return self.write({"errno":RET.THIRDERR, "errmsg":"qiniu error"})
        try:
            ret = self.db.execute("update ih_user_profile set up_avatar=%s where up_user_id=%s", img_name, user_id)
        except Exception as e:
            logging.error(e)
            return self.write({"errno":RET.DBERR, "errmsg":"upload failed"})
        img_url = config.image_url_prefix + img_name

        self.write({"errno":RET.OK, "errmsg":"OK", "url":img_url})

class InfoHandler(BaseHandler):
    """"""
    @require_logined
    def get(self):
        res = self.get_current_user()
        
        self.write({"errno":RET.OK, "errmsg":"OK","mobile":res["mobile"],"name":res["name"],"url":config.image_url_prefix+res["avatar"],"real_name":res.get("real_name",None),"id_card":res.get("id_card",None)})

class NameHandler(BaseHandler):
    """docstring for NameHandler"""
    @require_logined
    def post(self):
        user_id = self.session.data["user_id"]
        username = self.json_args.get("username")

        try:
            ret = self.db.execute("update ih_user_profile set up_name=%s where up_user_id=%s", username, user_id)
            self.session.data['name'] = username
            self.session.save()
        except Exception as e:

            logging.error(e)
            return self.write({"errno":RET.DBERR, "errmsg":"upload failed"})
        self.write({"errno":RET.OK, "errmsg":"OK", "username":username})

class RealnameHandler(BaseHandler):
    """docstring for RealnameHandler"""
    @require_logined
    def post(self):
        user_id = self.session.data["user_id"]
        realname = self.json_args.get("real_name")
        idcard = self.json_args.get("id_card")
        try:
            ret = self.db.execute("update ih_user_profile set up_real_name=%s,up_id_card=%s where up_user_id=%s", realname, idcard, user_id)
            self.session.data['real_name'] = realname
            self.session.data['id_card'] = idcard
            self.session.save()
        except Exception as e:
            logging.error(e)
            return self.write({"errno":RET.DBERR, "errmsg":"upload failed"})
        self.write({"errno":RET.OK, "errmsg":"OK", "real_name":realname,"id_card":idcard})
