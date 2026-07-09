import asyncio,requests,re,subprocess
from desktop_notifier import DesktopNotifier

#reading data from primary selection...
#using wl-clipboard for wayland and xclip for x11...
this_session=subprocess.check_output("echo $XDG_SESSION_TYPE",shell=True,text=True)
if this_session=="wayland\n":
    cmd="wl-paste --primary"
else:
    cmd="xclip -sel p -o"
input_word=subprocess.check_output(cmd,shell=True,text=True)
word = re.sub(r'[^a-zA-Z0-9]', '', "".join(input_word.splitlines()).strip())            #removing special characters,blank spaces and newline
if len(word)>50 or len(word)==0 :
    exit()


#dictionary api integration
link=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
r=requests.get(url=link)
data=r.json()
found=False
for i in data:
    if i=='title':
        found=True
        break
if found==True:
    meaning=data['title']
else:
    meaning=data[0]['meanings'][0]['definitions'][0]['definition']


#notify
notifier = DesktopNotifier()

async def main():
    await notifier.send(title=input_word, message=meaning)

asyncio.run(main())
