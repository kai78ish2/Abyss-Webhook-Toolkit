import requests,time, json

print("Loading Abyss Webhook Toolkit")

time.sleep(0.5)

print("Loaded.")

def main():
    while True:
        print("Command list:")
        option = input('''
        [0] Sets the webhook URL
        [1] Webhook message spammer
        [2] Delete webhook
        [3] Show webhook info
        [4] Change webhook name
        [5] Say one message
        [6] Checks the version
        [7] Posts an ad for this webhook console
        [8] Gnome the chat
        ==> ''')

        version = "V1.1"

        if option == "0":
            hook = input("Webhook URL: ")
            data = {"content": ""}
            headers = {"content-type": "application/json"}
            print("Setting the webhook url to: ",hook)
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Success Connected to the webhook: ",hook)

        
        if option == "1":
            message = input("Message to spam: ")
            amount = int(input("Amount to spam: "))
            wait = float(input("Message delay: "))

            headers = {"content-type": "application/json"}
            data = {"content": message}
            time.sleep(wait)
            print("Starting...")
            print("Started")

            for _ in range(amount):
                r = requests.post(hook, json=data,headers=headers)
                
                if r.status_code == 200:
                    print("Done")

        if option == "2":
           
            requests.delete(hook)
            print("Deleting...")
            time.sleep(0.5)
            print("The requested webhook has been deleted.\n") 

        if option == "3":
            r = requests.get(hook)
            print("Getting webhook info...")
            time.sleep(0.5)
            print(r.content)
                
        if option == "4":
            wbname = input("Set name: ")
            print("Processing...")
            time.sleep(0.5)
            requests.patch(hook, json={"name": wbname})
            print("Succsesfully changed webhook name to: ",wbname)

        if option == "5":
            message = input("Message to say: ")
            headers = {"content-type": "application/json"}
            data = {"content": message}
            print("Sending...")
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Sent!")
        
        if option == "6":
            print("Loading version...")
            time.sleep(0.5)
            print("Version: ",version," (You may need to download the latest version at https://github.com/kai78ish2/Abyss-Webhook-Toolkit")

        if option == "7":
            data = {"content": "Get Abyss Webhook Toolkit At: https://github.com/kai78ish2/Abyss-Webhook-Toolkit"}
            headers = {"content-type": "application/json"}
            print("Posting ad...")
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Posted")

        if option == "8":
            data = {"content": "Free Discord Nitro! https://media.discordapp.net/attachments/257902725327618058/527149504395476992/nitro_gift.png"}
            headers = {"content-type": "application/json"}
            print("Sending gnomage")
            time.sleep(0.5)
            r = requests.post(hook, json=data,headers=headers)
            print("Sent")    

if __name__ == "__main__":
  main()
