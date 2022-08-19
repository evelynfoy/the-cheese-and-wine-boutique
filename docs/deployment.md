
## Local Development
### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/evelynfoy/the-cheese-and-wine-boutique)
2. Click the [Code](//docs/images/deployment/clone-button.png) button and then choose your method.
3. To clone the repository using HTTPS, under the "HTTPS" tab copy the link. You could also choose to open it with Github Destop, Visual Studio or download it as a zip file.
4. Open the command prompt on your computer
5. Go to the location where you want the clone to be created.
6. Type `git clone`, and then paste the URL you copied in Step 3.

  ```
  $ git clone https://github.com/evelynfoy/the-cheese-and-wine-boutique.git
  ```

7. Pressing `Enter` will create the clone.
8. This will create a folder which looks like [this](//docs/images/deployment/folder.png).

<br>

### Forking the GitHub Repository

Forking means making a copy of the original repository on your own GitHub account.     
This gives you your own version to make changes to without affecting the original repository.

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/evelynfoy/the-cheese-and-wine-boutique)
2. Locate the [Fork](//docs/images/deployment/fork.png) button at the top right of the github page.
3. Click this to see the `Create a new fork` page. Click `Create fork` and you should now have a copy of the original repository in your GitHub account.

<br>

### Setting up your local environment

1. Open the project in your choice of editor.
2. Create an `env.py` file. It needs to contain the following variables:

  * Database URL - This can be obtained from [heroku](https://dashboard.heroku.com/) once an app has been set up.    
    It is defaulted to the DATABASE_URL config var on the settings tab - see the `Deployment to Heroku` section below. 
  * Cloudinary URL - This can be obtained from your [cloudinary](https://cloudinary.com/) account  follow the steps on the website to register. 
  * Secret_key - This is the django secret key for the app. It can be anything you like or you can use [the django secret key generator](https://miniwebtool.com/django-secret-key-generator/). 


```import os
os.environ["DATABASE_URL"] = 'postgres://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
os.environ["CLOUDINARY_URL"] = 'cloudinary://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
os.environ["SECRET_KEY"] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

3. Install app requirements
```
pip3 install -r requirements.txt
```

4. Migrate the database models  
```
python3 manage.py migrate
```

5. Create a superuser and set up its credentials 
```
python3 manage.py createsuperuser
```

6. To run the application locally 
```
python3 manage.py runserver
```

### Getting Stripe keys
Login to [Stripe](https://dashboard.stripe.com). Create an account if you don't have one.    
Go to developers tab (button on right of page). On side menu you will find API keys.     
Copy `Publishable key` as STRIPE_PUBLIC_KEY and `Secret key` as STRIPE_SECRET_KEY.    
<br>
If you click on the Payments tab you will be able to see all your test payments once you have made some.

<br>

### Getting email variables from gmail

- Log into your gmail account or [create](https://mail.google.com) one if you don't have one. 
- Go to Settings and than [See all settings](//docs/images/deployment/gmail-settings.png)
- Then go to the `Accounts and Import` tab and click the `Other Google Accounts settings` [link](//docs/images/deployment/other-google-account-settings.png).
- Click the `Security` tab. 
- Turn on `2-Step Verification`: enter a phone number and follow the instructions.
- On the `Security` tab, click on App passwords
- App passwords - Select Mail, Select Device - Other, Django and click `GENERATE`. Copy the app password generated.

In Heroku 
Set the `EMAIL_HOST_PASS` in [Config vars](//docs/images/deployment/config-vars.png) to the password copied from above.
Set the `EMAIL_HOST_USER` is the gmail email address.

<br>

## Remote Deployment
This project was deployed using Heroku.    
If you don't have an account you can create one [here](https://dashboard.heroku.com/apps "Heroku").

<br>

### Deployment to Heroku

1.  Login to your Heroku account
2.  Create an new app - name must be different to `the-cheese-and-wine-boutique`
3.  Attach the database - Search for the Heroku POSTGres add-on in the [Resources](//docs/images/deployment/heroku-postgres.png) tab 
    - This will default a unique value to a variable called DATABASE URL in the convig vars on the Settings tab.
4.  Set up the following additional variables here also
    - CLOUDINARY_URL - See `Setting up your local environment` above
    - EMAIL_HOST_PASS - See `Getting email variables from gmail` above
    - EMAIL_HOST_USER - See `Getting email variables from gmail` above
    - SECRET_KEY - See `Setting up your local environment` above
    - STRIPE_PUBLIC_KEY - See `Getting Stripe keys` above
    - STRIBE_SECRET_KEY - See `Getting Stripe keys` above
5.  Go to your local clone folder and make sure it has a Procfile containing `web: gunicorn cheese_wine_boutique.wsgi:application`.    
6.  Open the folder from your editor and in settings.py add your Heroku appname to ALLOWED_HOSTS     
    e.g. `ALLOWED_HOSTS = ['the-cheese-and-wine-boutique.herokuapp.com', 'localhost']`
7. Commit your changes and push to github
8. Go back to Heroku and click the `Deploy` tab in the menu bar. 
9. Go down to `Deployment method` and choose [GitHub](//docs/images/deployment/deployment.png).
10. A new section will appear called `Connect to GitHub` giving you an entry box for the repository to connect to.
11. Enter the name of your repository and click the `search` button
12. If the repository you entered exists heroku will list it. Click `connect`
13. Now go down to the next section called `Automatic Deploys` .
14. Click `Enable automatic deploys` if you want changes pushed to github to be automaticaly deployed to heroku.
15. Click `Deploy branch`

You will see the progress of the deployment from messages displayed until finally it will say `Your app was successfully deployed`

16. Click the button `View` to open the website

<br>


## To run the application
- The application has been deployed to https://the-cheese-and-wine-boutique.herokuapp.com/.    
  It can be accessed there or through the github repository - https://github.com/evelynfoy/the-cheese-and-wine-boutique/