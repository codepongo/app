import os
import urllib2
import datetime
def urlopen(url):
    f = urllib2.urlopen(url)
    html = f.read()
    f.close()
    return html

def from_github():
    paths = []
# https://api.github.com/users/codepongo/repos
# the list repositories api can not all user's repositories.
# so enumerate them.
    repos = ['index',
            'diary',
            'blog',
            'cook',
            'zjdict',
            'aboutme',
            'zReader',
            'zvim',
            'zshellext',
            'CNWeatherForecast',
            'bjfoodprice',
            'zjrssbucket',
            'zjruler',
            ]
    for r in repos:
        now = datetime.datetime.now()
        path = os.path.join(os.path.join(os.path.dirname(__file__), 'storage'), 'github_%s_%02d%02d%02d.json' % (r, now.year, now.month, now.day))
        paths.append(path)
        if os.path.isfile(path):
            continue
        repos =urlopen('https://api.github.com/repos/codepongo/%s' % (r))
        with open(path, 'wb') as f:
            f.write(repos)
    return paths

if __name__ == '__main__':
    from_github()


