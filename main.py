from flask import Flask
from flask import request




app = Flask(__name__)


def javascript_open():
    javascript = ''
    with open('code.js', 'r', encoding='utf-8') as f:
        javascript = f.read()

    # f.close()
    return javascript

def file_save(text_line):

    with open('save.txt', 'w', encoding='utf-8') as f:
        f.write(text_line)
    # f.close()

def file_open():
    text = ''
    with open('save.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    # f.close()
    return text

# / <- root
@app.route("/save")
def save():
    asdfadfs = request.args.get('data')
    # print(asdfadfs)
    file_save(asdfadfs)
    return ''

@app.route("/load")
def load():
    return file_open()


@app.route("/admin/user/code.js")
def javascript():
    javascript = javascript_open()
    return javascript


@app.route("/admin/user/app.yhd")
def hello():

    html = ''' 
    <!DOCTYPE html>
    <head>

    </head>
    
    <body>
    
        <input type="text" 
                name="값의 이름" 
                value="" />    
        <button>SAVE</button>
        <button>LOAD</button>
        <div> 
            default   
        </div>
    
        <script src = "code.js">
    
        </script>
    
    </body>

    
    '''

    # html = html.replace('{{value}}', file_open())

    # html_list=html.split()
    # html_list[10] = file_open()
    # html=' '.join(html_list)
    return html


if __name__ == '__main__':
    # file_save('111')



    app.run('127.0.0.1', port=5000, debug=True)

