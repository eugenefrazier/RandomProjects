import names
import string
import random
import pandas as pd
import datetime

class fake_identity_generator():

    def generate_birthday(self):
        self.day = random.randint(0,28)
        self.month = random.randint(1,12)
        self.year =  random.randint(1970,2000)

    def generate_random_name(self):
        gender = ["male","female"]
        self.select_gender  = gender[random.randint(0,1)]
        self.name_first = names.get_first_name(gender=self.select_gender)
        self.name_last =  names.get_last_name()

    def generate_random_email(self):
        email_provider_arr = ["gmail","outlook","protonmail","aol","zoho","icloud","yahoo","yandex"]
        self.email_provider = email_provider_arr[random.randint(0,len(email_provider_arr)-1)]

    def generate_random_password(self):
        ## length of password from the user
        length = self.pass_length

        # Do seeting for 
        ## characters to generate password from
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

        ## shuffling the characters
        random.shuffle(characters)
        
        ## picking random characters from the list
        password = []
        for i in range(int(length)):
            password.append(random.choice(characters))

        ## shuffling the resultant password
        random.shuffle(password)

        ## converting the list to string
        ## printing the list
        self.output_password = "".join(password)

    def export_to_csv(self):
        date = datetime.datetime.now()

        data ={
            "email":self.email_arr,
            "password":self.pass_arr,
            "first_name":self.first_name_arr,
            "last_name":self.last_name_arr,
            "birthday":self.bday_arr,
            "gender":self.gender_arr
        }

        df = pd.DataFrame(data)
        self.out_file = "{}_fake_identity_{}.csv".format(self.account_num,date.strftime('%d_%m_%Y')) 
        
        df.to_csv(self.out_file,index=False)

    def start_generate(self):

        __header__ = """ 
            /$$$$$$$ /$$   /$$/$$      /$$   /$$       /$$$$$$/$$$$$$$ /$$$$$$$$/$$   /$$/$$$$$$$$/$$$$$$/$$$$$$$$/$$     /$$      
            | $$__  $| $$  | $| $$     | $$  /$$/      |_  $$_| $$__  $| $$_____| $$$ | $|__  $$__|_  $$_|__  $$__|  $$   /$$/      
            | $$  \ $| $$  | $| $$     | $$ /$$/         | $$ | $$  \ $| $$     | $$$$| $$  | $$    | $$    | $$   \  $$ /$$/       
            | $$$$$$$| $$  | $| $$     | $$$$$/          | $$ | $$  | $| $$$$$  | $$ $$ $$  | $$    | $$    | $$    \  $$$$/        
            | $$__  $| $$  | $| $$     | $$  $$          | $$ | $$  | $| $$__/  | $$  $$$$  | $$    | $$    | $$     \  $$/         
            | $$  \ $| $$  | $| $$     | $$\  $$         | $$ | $$  | $| $$     | $$\  $$$  | $$    | $$    | $$      | $$          
            | $$$$$$$|  $$$$$$| $$$$$$$| $$ \  $$       /$$$$$| $$$$$$$| $$$$$$$| $$ \  $$  | $$   /$$$$$$  | $$      | $$          
            |_______/ \______/|________|__/  \__/      |______|_______/|________|__/  \__/  |__/  |______/  |__/      |__/          
            /$$$$$$ /$$$$$$$$/$$   /$$/$$$$$$$$/$$$$$$$  /$$$$$$ /$$$$$$$$/$$$$$$ /$$$$$$$                    /$$                 
            /$$__  $| $$_____| $$$ | $| $$_____| $$__  $$/$$__  $|__  $$__/$$__  $| $$__  $$                 /$$$$                 
            | $$  \__| $$     | $$$$| $| $$     | $$  \ $| $$  \ $$  | $$ | $$  \ $| $$  \ $$       /$$    /$|_  $$                 
            | $$ /$$$| $$$$$  | $$ $$ $| $$$$$  | $$$$$$$| $$$$$$$$  | $$ | $$  | $| $$$$$$$/      |  $$  /$$/ | $$                 
            | $$|_  $| $$__/  | $$  $$$| $$__/  | $$__  $| $$__  $$  | $$ | $$  | $| $$__  $$       \  $$/$$/  | $$                 
            | $$  \ $| $$     | $$\  $$| $$     | $$  \ $| $$  | $$  | $$ | $$  | $| $$  \ $$        \  $$$/   | $$                 
            |  $$$$$$| $$$$$$$| $$ \  $| $$$$$$$| $$  | $| $$  | $$  | $$ |  $$$$$$| $$  | $$         \  $/   /$$$$$$               
            \______/|________|__/  \__|________|__/  |__|__/  |__/  |__/  \______/|__/  |__/          \_/   |______/                                                                                                                                                                                                                                                                                                                                                                     
        """   
                                                                                                                  
        print(__header__)

        self.email_arr = []
        self.first_name_arr = []
        self.last_name_arr = []
        self.pass_arr = []
        self.bday_arr = []
        self.gender_arr = []

        self.account_num = input("[!] Enter Number of Account Generated ? eg. 1~10000 :")
        self.pass_length = 12

        for i in range(int(self.account_num)):
            self.generate_random_email()
            self.generate_random_name()
            self.generate_random_password()
            self.generate_birthday()
            
            first_name_initial = self.name_first.lower().lower()[0]
            last_name_initial = self.name_last.lower()[0]

            email_out = "{}{}.{}{}{}@{}.com".format(first_name_initial,last_name_initial,self.name_first,self.name_last,self.year,self.email_provider)
            name_out ="{} {}".format(self.name_first,self.name_last)
            pass_out = "{}".format(self.output_password)
            bday_out = "{}/{}/{}".format(self.day,self.month,self.year)
            gender_out = "{}".format(self.select_gender)
            
            self.email_arr.append(email_out)
            self.first_name_arr.append(self.name_first)
            self.last_name_arr.append(self.name_last)
            self.pass_arr.append(pass_out)
            self.bday_arr.append(bday_out)
            self.gender_arr.append(gender_out)

            print("[{}] Email : {} , Password : {} , Name : {} , Birthday : {} , Gender : {} ".format(i,email_out,pass_out,name_out,bday_out,gender_out))
        
        print("[!] Finish generating {} emails".format(self.account_num))
        self.export_to_csv()
        print("[!] Saving to CSV as {}".format(self.out_file))
        print("[!] Exiting Script !")


fake_identity_generator().start_generate()