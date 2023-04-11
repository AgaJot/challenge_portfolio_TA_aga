# Task 1: Konfiguracja oprogramowania
## Subtask 1: Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?
Hej! Mam na imię Aga i zdecydowałam się na udział w challenge'u z kilku powodów:
- zależy mi na poznaniu i przećwiczeniu Pythona w testowaniu (od ponad roku szukam takiej możliwości!)
- chcę działać i robić jak najwięcej zadań praktycznych, aby ugruntować teorię i zaznajomić się z narzędziami (wiedziałam, że tutaj praktyki nie zabraknie 🙂)
- chcę być cały czas w temacie i marzy mi się rutyna (bo wydaje mi się, że bez ćwiczeń zdobyta dotąd wiedza maleje z każdym dniem)
- myślę nieśmiało o przebranżowieniu, stąd decyzja o challenge'owym treningu
- poza tym lubię uczyć się nowych rzeczy
## Subtask 3
komentarz: Summary mam pod innymi nazwami, bo zmiany do zdalnego repozytorium wysłałam, robiąc pierwsze zadanie. Dopiero później przeczytałam treść 3. zadania i właściwą instrukcję. Mam nadzieję, że nie namieszałam i w rezultacie niczego nie popsułam.
## Subtask 4
wynik: 8 poprawnych na 14 :disappointed:

# Task 2: Selektory
## Subtask 1: Nowy branch
![image](https://user-images.githubusercontent.com/116113886/230984521-b41735f7-866e-4de8-b45a-60f1e5cbe24a.png)
![image](https://user-images.githubusercontent.com/116113886/230984667-4071d291-e79f-48e8-a54d-a6f56d722e42.png)
## Subtask 2: Wyszukiwanie selektorów na stronie logowania
**Scouts_Panel_[Scouts Panel](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true)_xpath**
- //*[@id="__next"]/form/div/div[1]/h5
- //h5
- //*[text()='Scouts Panel']

**Login_[Scouts Panel](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true)_xpath**
- //*[@id="__next"]/form/div/div[1]/div[1]
- //*[@id="login-label"] 
- //*[contains(@id,"login")]

**Password_[Scouts Panel](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true)_xpath**
- //*[@id="__next"]/form/div/div[1]/div[2]
- //input[@name="password"]
- //div[@class="MuiFormControl-root MuiTextField-root jss56 MuiFormControl-marginNormal" and position()=2]

**Remind password_[Scouts Panel](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true)_xpath**
- //*[@id="__next"]/form/div/div[1]/a
- //*[contains(@class, "MuiLink")] 
- //child::div/a

**Language button_[Scouts Panel](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true)_xpath**
- //div[@role="button"]
- //*[text()="English"]
- //input[@value="en" or @value="pl"]

**Sign in button_[Scouts Panel](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true)_xpath**
- //child::div/button
- //*[contains(@class,"MuiButton")]
- /html/body/div/form/div/div[2]/button
