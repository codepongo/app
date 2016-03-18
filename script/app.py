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
        '/(.*.ico)', 'static',
        '/(.*.png)', 'static',
        '/whatsmyuseragent.*', 'useragent.useragent',
        '/whereisip.*', 'where_is_ip'
        #        '/food', 'Food',
        )

class index:
    def GET(self):
        self.repos = [
                'stockcalculator',
                'doubanpachong',
                'app',
                'cook',
                'blog',
                'stbipy',
                'zjdict',
                'weixin',
                'imagresizer',
                'resumerefresher',
                'aboutme',
                'loudspeaker',
                'zshellext',
                'zjruler',
                'bjfoodprice',
                'CNWeatherForecast',
        ]
        briefs = []
        path = os.path.join(os.path.dirname(__file__), 'storage')
        for name in self.repos:
            name = name + '.htm'
            p = os.path.join(path, name)
            if os.path.isfile(p) and os.path.splitext(p)[1] == '.htm':
                with open(os.path.join(p), 'rb') as f:
                    briefs.append(f.read())
        return render.apps(briefs)


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

