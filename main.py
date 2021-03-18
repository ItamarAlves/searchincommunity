import requests
import re
import json
##cria um layer, sobre poem a imagem. 

class InstagramScanner:

    def __init__(self, username):
        self.username = username

    def scanner(self):
        url = 'https://www.instagram.com/'+ self.username + '/'
        r = requests.get(url)

        # text = re.findall('(<script)(.*)(>)', str(r.text))
        respostaHtml = re.findall('config(.*)', str(r.text))
        respostaJson = "".join(respostaHtml)
        respostaJson = respostaJson.replace("</script>", '')
        respostaJson = respostaJson.replace(";", '')
        respostaJson = "{\"config"+respostaJson;
        # print(respostaJson)

        data = json.loads(respostaJson)

        listProfiles = data["entry_data"]
        
        for profile in listProfiles.get("ProfilePage"):
            print(profile.get("graphql")["user"]["id"])
            print(profile.get("graphql")["user"]["username"])
            print(profile.get("graphql")["user"]["biography"])
            print(profile.get("graphql")["user"]["external_url"])


        # arq = open('response.txt', 'w', encoding='utf8')
        # arq.write(text)
    

if __name__ == "__main__":
    ie = InstagramScanner("alves.sh");
    ie.scanner()

