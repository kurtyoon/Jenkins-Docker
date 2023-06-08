from flask import Flask, render_template, request

app = Flask(__name__)

result_list = list()
header = ['Name', 'Number', 'Major', 'Email', 'Gender', 'Languages'] # table의 header 부분에 들어갈 header 설정

def sort_list():
   result_list.sort(key = lambda x: x['Number']) # lambda를 사용해 Number를 기준으로 정렬
 
@app.route('/', methods = ['GET', 'POST'])  # default URL
def main():
   if request.method == 'POST': # POST 일 경우 HOME 버튼을 누름
      result_list.clear() # list 초기화
   return render_template('main.html')

@app.route('/result', methods = ['POST','GET'])
def result():
   if request.method == 'POST': # POST 일 경우 main.html에서 submit 버튼을 누름
      result = dict()

      result['Name'] = request.form.get('name')
      result['Number'] = request.form.get('number')
      result['Major'] = request.form.get('major')
      result['Email'] = request.form.get('email_id') + '@' + request.form.get('email_addr')
      result['Gender'] = request.form.get('gender')
      result['languages'] = ', '.join(request.form.getlist('chkbox'))

      result_list.append(result) # dictionary를 list에 추가
      sort_list() # 정렬하여 rendering
      return render_template("result.html", result = result_list, header = header)
   if request.method == 'GET': # GET을 통해 들어온 경우 DELETE 버튼을 누름
      tmp = request.args.getlist('delete') # request.args.getlist로 인자를 받아옴
      for i in tmp:
         result_list.pop(int(i)) # result.html에서 loop문의 인덱스를 넘겼으므로 해당 인덱스를 pop
      return render_template("result.html", result = result_list, header = header)

if __name__ == '__main__':
   app.run('0.0.0.0', port=8000, debug = True)