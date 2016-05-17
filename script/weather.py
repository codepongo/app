import sys
import os
import web
import weatherbroadcast
class broadcast:
    def GET(self):
        render = web.template.render(os.path.join(os.path.dirname(__file__), 'templates'))
        return render.weather(weatherbroadcast.baidu())
    def POST(self):
        render = web.template.render(os.path.join(os.path.dirname(__file__), 'templates'))
        return render.weather(weatherbroadcast.baidu(web.input().city.encode('utf8')))
