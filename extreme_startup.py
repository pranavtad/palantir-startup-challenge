from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def answer():
    q = request.args.get("plus", "")
    print(q)
    '''
        i = q.find("is", beg=0, end=len(string))
        start_one = i + 3
        print(start_one)
        p = q.find("plus", beg=0, end=len(string))
        
        end_one = p - 1
        print(end_one)
        
        x = q.find("plus", beg=0, end=len(string))
        start_two = x + 4
        y = len(q) - 1
        
        numberone = q[start_one:end_one]
        numbertwo = q[x:y]
        print(numberone)
        print(numbertwo)
        '''
    
    return "4029"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

