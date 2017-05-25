import web
import subprocess





urls = (
  '/trigger', 'trigger','/aircon', 'aircon', "/killapp", "killapp"
)


app = web.application(urls, globals())

render = web.template.render('templates/')

class trigger(object):
    def GET(self):
        form = web.input(scriptname=None)
        if form.scriptname:
            scriptname = str(form.scriptname)
            subprocess.call("scripts/%s.sh" % form.scriptname) 
            return render.trigger(scriptname = scriptname)
        else:
            return render.trigger(scriptname = None)


class aircon(object):
    def GET(self):
        form = web.input(power=None,mode=None,fan=None,temp=None,abstemp=None)
        varcount = 1
        if form.power:
            varcount = None
            subprocess.call("irsend SEND_ONCE aircon KEY_POWER", shell=True)
        if form.mode:
            varcount = None
            mode = int(form.mode)
            for _ in range(mode):
                subprocess.call("irsend Send_Once aircon KEY_MODE", shell=True)
        if form.fan:
            varcount = None
            fan = int(form.fan)
            for _ in range(fan):
                subprocess.call("irsend Send_Once aircon KEY_F", shell=True)
        if form.temp:
            varcount = None
            temp = int(form.temp)
            if temp < 0:
                for _ in range(abs(temp) + 1):
                    subprocess.call("irsend SEND_ONCE aircon KEY_DOWN", shell=True)
            if temp > 0:
                for _ in range(temp + 1):
                    subprocess.call("irsend SEND_ONCE aircon KEY_UP", shell=True)
        if form.abstemp:
            varcount = None
            for _ in range(16):
                subprocess.call("irsend SEND_ONCE aircon KEY_DOWN", shell=True)
            for _ in range(int(form.abstemp) - 64):
                subprocess.call("irsend SEND_ONCE aircon KEY_UP", shell=True)                

        return render.aircon(power=form.power,mode=form.mode,fan=form.fan,temp=form.temp,abstemp=form.abstemp,error=varcount)


#Currently doesn't work, doesn't actually exit program
class killapp(object):
    def GET(self):
        #close()
        return "Triggered the Kill proccess (it has not nessiarily worked though)."

if __name__ == "__main__":
    app.run()




#Negitive accepting fan and mode code (Does Not work)
'''
            if mode < 0:
                #print mode
                negmode = abs(mode) + 1
                #print negmode
                for _ in range(negmode):
                    subprocess.call("irsend Send_Once aircon KEY_MODE", shell=True)
            if mode > 0:
                for _ in range(mode):
                    subprocess.call("irsend Send_Once aircon KEY_MODE", shell=True)
        if form.fan:
            fan = int(form.fan)
            if fan < 0:
                #print fan
                negfan = abs(fan) + 2
                #print negfan
                for _ in range(negfan):
                    subprocess.call("irsend Send_Once aircon KEY_F", shell=True)
            if fan > 0:
                for _ in range(fan):
                    subprocess.call("irsend Send_Once aircon KEY_F", shell=True)
        return render.aircon()
'''
