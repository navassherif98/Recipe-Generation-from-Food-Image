from flask import render_template ,url_for,flash,redirect,request
from Foodimg2Ing import app
from Foodimg2Ing.output import output


@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/',methods=['POST','GET'])
def predict():
    imagefile=request.files['imagefile']
    image_path="F:/PROJECTS/Flask Projects/Recipe Generation from Food Image/Foodimg2Ing/static/images/demo_imgs/"+imagefile.filename
    imagefile.save(image_path)
    img="/images/demo_imgs/"+imagefile.filename
    title,ingredients,recipe = output(image_path)
    print(image_path)
    return render_template('predict.html',title=title,ingredients=ingredients,recipe=recipe,img=img)

@app.route('/<samplefoodname>')
def predictsample(samplefoodname):
    imagefile="F:/PROJECTS/Flask Projects/Recipe Generation from Food Image/Foodimg2Ing/static/images/"+str(samplefoodname)+".jpg"
    img="/images/"+str(samplefoodname)+".jpg"
    print("{athnavas"+samplefoodname)
    title,ingredients,recipe = output(imagefile)
    
    return render_template('predict.html',title=title,ingredients=ingredients,recipe=recipe,img=img)