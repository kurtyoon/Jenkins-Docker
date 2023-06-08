from flask import Flask, redirect,render_template,request 
 
app = Flask(__name__) 
 
result_list = list()
header = ['Name', 'Number', 'Major', 'Email', 'Gender', 'Languages'] 
def sort_list():                                     
   result_list.sort(key = lambda x: x['Number'])       


@app.route('/', methods = ['GET', 'POST'])  
def main():
   if request.method == 'POST':                      
        result_list.clear()                          
   return render_template('main.html')
 

@app.route('/result', methods = ['POST','GET']) 
def result(): 
   if request.method == 'POST': 
      result = dict()
      result['Name'] = request.form.get('name') 
      result['Number'] = request.form.get('number') 
      result['Major'] = request.form.get('major') 
      result['Email'] = request.form.get('email_id') + '@' + request.form.get('email_addr') 
      result['Gender'] = request.form.get('gender') 
      result['languages'] = ', '.join(request.form.getlist('chkbox')) 
      result_list.append(result) 
      sort_list()                                  
      return render_template("result.html", result = result_list, header = header) 
   if request.method == 'GET':
      tmp = request.args.getlist('delete')
      tmp.reverse()
      for i in tmp:
         result_list.pop(int(i))
      return render_template("result.html", result = result_list, header = header)


 
if __name__ == '__main__': 
   app.run('0.0.0.0', port=8000, debug = True)