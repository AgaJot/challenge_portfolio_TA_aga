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

**Scouts_Panel_xpath**
- //*[@id="__next"]/form/div/div[1]/h5
- //h5
- //*[text()='Scouts Panel']

**Login_field_xpath**
- //*[@id="__next"]/form/div/div[1]/div[1]
- //*[@id="login-label"] 
- //*[contains(@id,"login")]

**Password_field_xpath**
- //*[@id="__next"]/form/div/div[1]/div[2]
- //input[@name="password"]
- //div[@class="MuiFormControl-root MuiTextField-root jss56 MuiFormControl-marginNormal" and position()=2]

**Remind_password_button_xpath**
- //*[@id="__next"]/form/div/div[1]/a
- //*[contains(@class, "MuiLink")] 
- //child::div/a

**Language_button_xpath**
- //div[@role="button"]
- //*[text()="English"]
- //input[@value="en" or @value="pl"]

**Sign_in_button_xpath**
- //child::div/button
- //*[contains(@class,"MuiButton")]
- /html/body/div/form/div/div[2]/button
- //*[text()="Sign in"]

## Subtask 3: Dodawanie selektorów do projektu
![image](https://user-images.githubusercontent.com/116113886/231213759-3f88a6b7-e359-4dd0-903f-9c7a42d88837.png)

## Subtask 4: Dodanie nowego pliku
![image](https://user-images.githubusercontent.com/116113886/231265784-bddfe2ca-4565-49c1-b594-8d32a4c285a2.png)

## Subtask 5: Dodanie nowego pliku - add a match form
![image](https://user-images.githubusercontent.com/116113886/231282175-fd2733a0-9ae0-4a85-a3d5-9f2d8bc4fcd1.png)



