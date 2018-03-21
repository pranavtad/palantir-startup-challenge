from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def answer():
    q = request.args.get("q", "")
    #print(q)
    #print(q[10:])
    array = [int(s) for s in q.split() if s.isdigit()]
    print(array)
    #print(array)
    
    if "plus" in q:
        print(sum(array))
        return str(sum(array))
    if "multiplied" in q:
        print (array[0] * array[1])
        return str(array[0] * array[1])
    
    if "largest" in q:
        return str(array[array.index(max(array))])
    
    else:
        return "69"


if __name__ == "__main__":
    app.run(host='0.0.0.0')

