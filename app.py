from flask import Flask,render_template,request,redirect,url_for


#create instance from the Flask class

app = Flask(__name__,template_folder='templates')


tasks=[]

#Routing
@app.route('/')
def home():
    return render_template('index.html',tasks=tasks )


#Creating a new flask
@app.route('/add_task',methods=['POST','GET'])   #App decorator
def create_new_task():
    task = request.form.get("task")
    tasks.append(task)  #Adding task to our list
    return redirect(url_for("home"))

#Deleting task
app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for("home"))


#Enabling the debug mode
if __name__== "__main__":
    app.run(debug=True)