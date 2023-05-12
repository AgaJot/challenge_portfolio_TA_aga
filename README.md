# Task 1: Konfiguracja oprogramowania
## Subtask 1: Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?
Hej! Mam na imię Aga i zdecydowałam się na udział w challenge'u z kilku powodów:
- zależy mi na poznaniu i przećwiczeniu Pythona w testowaniu (od ponad roku szukam takiej możliwości!)
- chcę działać i robić jak najwięcej zadań praktycznych, aby ugruntować teorię i zaznajomić się z narzędziami (wiedziałam, że tutaj praktyki nie zabraknie 🙂)
- chcę być cały czas w temacie i marzy mi się rutyna (bo wydaje mi się, że bez ćwiczeń zdobyta dotąd wiedza maleje z każdym dniem)
- myślę nieśmiało o przebranżowieniu, stąd decyzja o challenge'owym treningu
- poza tym lubię uczyć się nowych rzeczy
## Subtask 3
komentarz: Summary mam pod innymi nazwami, bo zmiany do zdalnego repozytorium wysłałam, robiąc pierwsze zadanie. Dopiero później przeczytałam treść 3. zadania i właściwą instrukcję.
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
- //*[@id="login"]
- //input[@id="login"] 
- //input[contains(@name,"login")]

**Password_field_xpath**
- //*[@id="password"]
- //input[@name="password"]
- //*[contains(@type,"password")]

**Remind_password_button_xpath**
- //*[@id="__next"]/form/div/div[1]/a
- //*[contains(@class, "MuiLink")] 
- //child::div/a

**Language_button_xpath**
- //div[@role="button"]
- //*[text()="en"]
- //input[@value="en" or @value="pl"]

**Sign_in_button_xpath**
- //child::div/button
- //*[contains(@class,"MuiButton")]
- /html/body/div/form/div/div[2]/button
- //*[text()="Sign in"]

## Subtask 3: Dodawanie selektorów do projektu
![image](https://user-images.githubusercontent.com/116113886/232256476-0e2554fb-b982-4475-a9ef-9be67d2cfd0b.png)

## Subtask 4: Dodanie nowego pliku
![image](https://user-images.githubusercontent.com/116113886/232256500-5a470911-1e99-4658-b4b5-dc5c7225178d.png)

## Subtask 5: Dodanie nowego pliku - add a match form
![image](https://user-images.githubusercontent.com/116113886/232256531-c8257b8c-543d-4fd7-b8b5-8add9fb16eac.png)

# Task 3: Pierwszy test i assert
## Subtask 1: Uzupełnienie strony logowania
![image](https://user-images.githubusercontent.com/116113886/232617262-54e33099-4a94-4925-b65e-4b8b19544666.png)

## Subtask 2: Nowy przypadek testowy
![image](https://user-images.githubusercontent.com/116113886/232806490-be19739c-2239-47e6-ab01-179d3b46ba92.png)

## Subtask 3: Assert
![image](https://user-images.githubusercontent.com/116113886/232853389-cd2b1a12-966d-4b34-a23e-792cf76aed76.png)

## Subtask 4: Powtórzenie tego, co już wiemy

![image](https://user-images.githubusercontent.com/116113886/233200939-5cdb73d4-a719-4925-bdb6-fe6f47f1367a.png)
![image](https://user-images.githubusercontent.com/116113886/233201230-244b3459-d6f6-4d86-be56-87cf4e8a5e50.png)
![image](https://user-images.githubusercontent.com/116113886/233201911-936a25a3-b29e-482b-8048-ede78515a359.png)
![image](https://user-images.githubusercontent.com/116113886/233202061-b0f47ad8-223c-4e72-a807-c2bd19a69144.png)

# Task 4: 
https://docs.google.com/spreadsheets/d/1JIFI09yHd2AU-mvYC0z-iIu0UshwraNHI14LwyKICPM/edit#gid=114028924

# Task 6: 
https://drive.google.com/drive/folders/1z1aZIO9vKAE_Ez6i0xgiWUe7BU0ZGokb

[Robot Framework](https://github.com/AgaJot/panelscout_robotframework)

komentarz: przy testach w środowisku produkcyjnym asercje w testach zagnieżdżonych zostały zakomentowane i nie miały wpływu na przebieg i wynik testów


