#coding:utf-8
import sys
import os
sys.path.append(os.path.dirname(__file__))
import web
import datetime
import useragent
import whereisip

urls = (
        '/', 'index',
        '/hi', 'hi',
        '/(favicon.ico)', 'static',
        '/(.*.css)', 'static',
        '/whatsmyuseragent.*', 'useragent.useragent',
        '/whereisip.*', 'where_is_ip'
#        '/food', 'Food',
)

class index:
    def GET(self):
        dbpath = os.path.join(os.path.join(os.path.dirname(__file__), 'storage'), 'app.db')
        db = web.database(dbn='sqlite', db=dbpath)
        return render.apps(db.select('app', order='update_time DESC'))


class static:
    def GET(self, path):
        web.seeother('/static/'+path)

def error():
    return web.seeother('/static/error.html')

class hi:
    def GET(self):
        return 'hi,world!'

class where_is_ip:
    def GET(self):
        ip = web.ctx.env.get('REMOTE_ADDR')
        nation = whereisip.ip2nation.nation(ip)
        ip += ' - ' + str(nation[0][0])
        return render.whereisip(ip)

render = web.template.render(os.path.join(os.path.dirname(__file__), 'templates'))
app = web.application(urls, globals())

if __name__ == '__main__':
    web.config.debug = True
    app.run()
else:
    app.internalerror = error
    app.notfound = error
    application = app.wsgifunc()

