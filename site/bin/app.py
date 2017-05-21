import web
import subprocess

urls = (
  '/trigger', 'Index'
)


app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        form = web.input(scriptname="Nobody")
        scriptname = str(form.scriptname)
        subprocess.call("scripts/%s.sh" % form.scriptname) 
        return render.index(scriptname = scriptname)

if __name__ == "__main__":
    app.run()