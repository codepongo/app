import sys
import os
sys.path.append(os.path.dirname(__file__))
import web
class useragent:
    def GET(self):
        print 'hello'
        render = web.template.render(os.path.join(os.path.dirname(__file__), 'templates'))
        return render.whatsmyuseragent(web.ctx.env.get('HTTP_USER_AGENT'))
