# APT Spring 2016: Assignment 1

## Assignment:

We will be working on simple web project. Your task is to write a small
web app that will fetch currency data from http://public.mig.kz/ and return
in JSON format.

### Setup:

 * Create GitHub account.
 * Save ssh key to GitHub <https://github.com/settings/ssh>:
   - if you do not have `~/.ssh/id_rsa.pub` file, generate ssh key using ssh-keygen
   - `cat ~/.ssh/id_rsa.pub`
 * Fork the https://github.com/giAtSDU/apt_spring_2016_hw1 repository
 * Create virtual environment using `pyvenv-3 venv`
 * If `pip` is not available by default, install it using these instructions https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py 
 * Activate your environment and install dependencies using pip `pip install bottle requests beautifulsoup4`
 * Install git if it is not available on your linux maching: `sudo apt-get install git`


### Tasks:
 * Clone your forked repository to your local machine
 * Run the server: `python server.py`
 * Make sure that it works: goto <http://localhost:5000>; It should return dummy static data `{"eur": 415, "rub": 4.82, "usd": 378}`. 
 * Open the `server.py` file and see its contents.
 * Change `index` method so that it will fetch real data from http://public.mig.kz site.
 * You can see an example that fetches forks counter from this github repository. Run the server using `python server.py` and open http://localhost:5000/forks in your browser to test it. 
 * Use git commit to commit your change. Use a meaningful message like "."
 * Use git push to send your change to your forked repository.
 * Look online to see if your change has been pushed.
 * Once you have finished upload the link of your forked repository to google classroom.

### For those who wants more:
 * Deploy your application to heroku
 * Create an account on heroku.com
 * See the tutorial <https://devcenter.heroku.com/articles/getting-started-with-python-o>
 * Download the heroku toolbelt
 * Create heroku application using `heroku create`. Run it inside the project folder. Heroku toolbelt will crate a remote in your git project. See `git remote -v`
 * Deploy the project using `git push heroku master` 
 * Open an url that heroku generated for you

## Git commands you might need

 * git help
 * git clone REPO
 * git add FILE
 * git status
 * git commit
 * git commit -m "MESSAGE"
 * git log | less
 * git push
 * git pull

## Documentation on libraries you need

 * http://bottlepy.org/docs/dev/index.html
 * http://docs.python-requests.org/en/latest/
 * http://www.crummy.com/software/BeautifulSoup/bs4/doc/

## Troubleshooting

 * https://stackoverflow.com/questions/4565700/specify-private-ssh-key-to-use-when-executing-shell-command-with-or-without-ruby
 * https://superuser.com/questions/232373/how-to-tell-git-which-private-key-to-use
