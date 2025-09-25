# How to make it work for the first time
> A very simple and non-proffesional guide

---

### 1. Install docker

You know this. Just use https://docs.docker.com/desktop/setup/install/windows-install/ and install it. We will run the databases (all three of them) using docker. 

### 2. Download the project using git
Ye

### 3. Copy the env files
Navigate to the "BTH-AI-CHATBOT" folder you just installed using cd. 

Then run:
```
cp .env.example .env.local
cp .env.docker.secrets.example .env.docker.secrets
```

Now you will have your own env files, yippie. However make sure to keep to the names provided in the lines above since otherwise it all becomes hell.
In you .env.local, make sure to generate the ```AUTH_SECRET``` key by pressing the link that can be found in the comment above. 

### 4. Install npm and bun
Install npm on the following link: https://nodejs.org/en/download/ if you are a filthy mac/windows user.

Install bun by using the newly downloaded npm with the following command:

```
npm install -g bun
```

> [!WARNING]
> On windows, do not use powershell! Caused some issues with npm for Sebbe so make sure to use the normal control panel.

### 5. Get the servers to work
First run:
```
npm run db:start
```
Now you should have three containers running if you make a quick check with ```docker ps```
Then run:

```
npm run db:migrate
```

which is a command that I am sure is really important. 

### 6. Moment of truth

Now it is time. First install all the necessary packages with:
```
npm install
```
which reads the packages.json file and installs everything from there.
At last:
```
npm run dev
```

after which you should be able to go to localhost:3000 on your browser and you see the magic work.

> [!TIP]
> When debugging you can run the flag ```--loglevel``` with either ```verbose```  or ```silly```. So in total it would look something like:
> 
> ```
> npm run --loglevel silly
> ```
---

> [!NOTE]
> Does all of this look easy? That is because Albin and Sebbe has made some changes to the github that we are not proud of
