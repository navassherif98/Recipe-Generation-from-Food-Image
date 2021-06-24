from flask import Flask

app = Flask(__name__,template_folder='Templates')


from Foodimg2Ing import routes