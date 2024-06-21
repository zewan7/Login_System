import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))  
text_file_path = os.path.join(script_dir, 'text.txt')  

class RandomSymbol:
    def __init__(self):
        self.list_symbol = []
        self.str_all = open(text_file_path, 'r', encoding='utf-8').read().split('\n')

    def random_symbol(self):

        string2 = f"""  
        
        
    ╭ ╯╭ ╯╭ ╯
    ╭ ╯╭ ╯╭ ╯
  ╔╩═══╗╔══════╗╔══════╗╔═══════╗
  ‖ □ □  ╠╣           
  ‖        ╠╣ {random.choice(self.str_all)}
  ╚⊙══⊙╝╚◎════◎╝╚◎════◎╝╚◎═════◎╝
  
  """
        string3 = f"""
        
        
         ◢◤◢◤
　　　　　◢████◤
　　　⊙███████◤
　●████████◤ {random.choice(self.str_all)}
　　▼　　～◥███◤
　　▲▃▃◢███　●　　●　　●　　●　　●　　●　　●　　●　
　　　　　　███／█　／█　／█　／█　／█　／█　／█　／█
　　　　　　█████████████████████████████◤

  """
        string4 = f"""
        
        
        
  ．∵ ∴★．∴∵∵ ╭ ╯╭ ╯╭ ╯╭ ╯∴
   ☆．∵∴∵．∵∵∵∴▍▍ ▍▍ ▍▍ ▍▍☆ ★∵∴
  ▍█．∴∵∴∵∵∴▅███████████☆ ★∵∴
  ◥█▅▅▅▅█▅█▅█▅█▅█▅█▅█▅█▅█▅█▅▅█◤
  ． ◥███ {random.choice(self.str_all)}       
  ．.．◥█████████████████████◤	
  
  """
        string5 = f"""
    ◢▅▅▅▅▅◣　　　     ◢▅▅▅▅▅◣
  ◢◤　　　　　◥◣　　　　◢◤　　 　 　◥◣
  ◤　　　　　　　◥◣　　◢◤　　　 　 　　◥
  ▎　　　◢█◣　　◥◣◢◤　  ◢█◣　      ▎
  ◣　　◢◤  ◥◣　　　 　 　◢◤  ◥◣    ◢　
  ◥██◤　 　◢◤　　　　 　 ◥◣   ◥██◤　
             █　◕　　　　　◕｡　█          
             █　〃　　◕　　〃　█      
             ◥◣　 . ☺　   ◢◤{random.choice(self.str_all)}
               ◥█▃　▃ ▃█◤
               ◢◤　　　◥◣
                █　　　　　█
              ◢◤ ▎　 　▎◥◣
              ▕▃◣◢▅▅◣◢▃▕
              
  """
        string6 = f"""
                .-\"""-.
               / .===. \\
               \/ 6 6 \/
               ( \___/ )
  _________ooo__\_____/_____________
  
  {random.choice(self.str_all)}
  _______________________ooo________
                |  |  |
                |_ | _|
                |  |  |
                |__|__|
                /- Y -\\
               (__/ \__)
               
  """
        self.list_symbol.append(string2)
        self.list_symbol.append(string3)
        self.list_symbol.append(string4)
        self.list_symbol.append(string5)
        self.list_symbol.append(string6)
        return random.choice(self.list_symbol)

if __name__ == '__main__':

    s = RandomSymbol()
    print(s.random_symbol())
