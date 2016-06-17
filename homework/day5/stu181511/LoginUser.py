import sys, os, configparser, json


class LoginUserAbs(object):
    def __init__(self):
        self.user_dic = dict()
        self.login_id = None
        self.admin_Flag = False

    def login(self):
        while 1:
            user_id = input('Please input user id:').strip()
            if user_id:
                passwd = input('Please input password:').strip()
                if self._login(user_id, passwd):
                    return True
            else:
                print('User id can\'t be empty')

    def _login(self, user_id, passwd):
        if user_id in self.user_dic and self.user_dic[user_id][0] == passwd:
            self.login_id = user_id
            # check whether this user is an administrator
            if self.user_dic.get(user_id)[1]:
                self.admin_Flag = True
            return True
        print('Wrong user id or password')
        return False

    def del_user(self):
        for uid, info in self.user_dic.items():
            print('User id: %s'%uid)
        while 1:
            del_user_id = input('Please input user id you wanner delete:').strip()
            if self._del_user(del_user_id):
                if del_user_id == self.login_id:
                    # You must login with anoter user id
                    # after you delete your own user id.s
                    print('Please login with another user id')
                    return True
                else:
                    break

    def _del_user(self, del_user_id):
        if self.admin_Flag:
            if del_user_id in self.user_dic:
                self._del_user_cfg(del_user_id)
            print('Delete user successfully')
            return True
        else:
            print('You are not administrator, so you can\'t delete user')
            return False

    def change_passwd(self):
        while 1:
            old_passwd = input('Please input your original password:').strip()
            if old_passwd and self.user_dic.get(self.login_id, [])[0] == old_passwd:
                self.user_dic[self.login_id][0] = self._get_passwd()
                self._change_user_cfg(self.login_id)
                print('Changed successfully ')
                return True
            else:
                print('Password is\'t correct')

    def _get_passwd(self):
        while 1:
            passwd = input('Please input new password:').strip()
            passwd_rep = input('Please repeat new password:').strip()
            if passwd == passwd_rep:
                return passwd
            else:
                print('The passwords you input are not the same')

    def register(self):
        while 1:
            user_id = input('Please input user id:').strip()
            if user_id:
                if self._register(user_id):
                    return True
            else:
                print('User id can\'t be empty')

    def _register(self, user_id):
        if user_id in self.user_dic:
            print('This user id is already used')
            return False
        else:
            self.user_dic[user_id] = [self._get_passwd(), 0]
            self._add_user_cfg(user_id)
            print('Registered successfully ')
            return True

    def _add_user_cfg(self, *args):
        pass

    def _del_user_cfg(self, *args):
        pass

    def _change_user_cfg(self, *args):
        pass


class LoginUserContxt(LoginUserAbs):
    def __init__(self, cfg_file, admin_cfg_file):
        self._cfg_file = cfg_file
        self._admin_cfg_file = admin_cfg_file
        self.user_dic = dict()
        self._set_user_dic(cfg_file, 0)
        self._set_user_dic(admin_cfg_file, 1)
        print('Initalize over')

    def _set_user_dic(self, cfg_file, admin_flag):
        with open(cfg_file, 'r') as f:
            for i in f:
                if '&' in i:
                    tmps = i.strip('\n').split('&')
                    self.user_dic[tmps[0]] = [tmps[1], admin_flag]

    def _add_user_cfg(self, user_id):
        self._update_cfg(self.user_dic[user_id][1])

    def _del_user_cfg(self, del_user_id):
        user_flag = self.user_dic[del_user_id][1]
        del self.user_dic[del_user_id]
        self._update_cfg(user_flag)

    def _change_user_cfg(self, user_id):
        self._update_cfg(self.user_dic[user_id][1])

    def _update_cfg(self, cfg_flag):
        cfg_file = self._cfg_file if cfg_flag is 0 \
            else self._admin_cfg_file
        with open(cfg_file, 'w') as f:
            f.writelines(['%s&%s\n' % (uid, info[0]) for uid, info \
                          in self.user_dic.items() if info[1] is cfg_flag])


class LoginUserConf(LoginUserAbs):
    def __init__(self, cfg_file):
        self._cfg_file = cfg_file
        self.user_dic = dict()
        self._conf = None
        self._set_user_dic(cfg_file)

        print('Initalize over')

    def _set_user_dic(self, cfg_file):
        self._conf = cf = configparser.ConfigParser()
        cf.read(cfg_file)
        for user_id in cf.sections():
            self.user_dic[user_id] = [cf.get(user_id,'password'),
                                      cf.getint(user_id,'admin_flag')]

    def _add_user_cfg(self, user_id):
        self._conf.add_section(user_id)
        self._conf.set(user_id, 'password', self.user_dic[user_id][0])
        self._conf.set(user_id, 'admin_flag', str(self.user_dic[user_id][1]))
        self._update_cfg()

    def _del_user_cfg(self, del_user_id):
        del self.user_dic[del_user_id]
        self._conf.remove_section(del_user_id)
        self._update_cfg()

    def _change_user_cfg(self, user_id):
        self._conf.set(user_id, 'password', self.user_dic[user_id][0])
        self._update_cfg()

    def _update_cfg(self):
        self._conf.write(open(self._cfg_file, "w"))


class LoginUserJson(LoginUserAbs):
    def __init__(self, cfg_file):
        self._cfg_file = cfg_file
        self.user_dic = dict()
        self._conf = None
        self._set_user_dic(cfg_file)
        print('Initalize over')

    def _set_user_dic(self, cfg_file):
        with open(cfg_file, 'r') as f:
            self.user_dic = json.load(f)

    def _add_user_cfg(self, user_id):
        self._update_cfg()

    def _del_user_cfg(self, del_user_id):
        del self.user_dic[del_user_id]
        self._update_cfg()

    def _change_user_cfg(self, user_id):
        self._update_cfg()

    def _update_cfg(self):
        dumped_cfg = json.dumps(self.user_dic)
        with open(self._cfg_file, 'w') as f:
            f.write(dumped_cfg)
