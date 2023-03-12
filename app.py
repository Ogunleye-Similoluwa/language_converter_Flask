# from flask import Flask, request, render_template
# from googletrans import Translator
#
# app = Flask(__name__)
#
#
# @app.route('/', methods=["POST"])
# def hello_world():
#     f = open('static/templates/file.html')
#     page = f.read()
#     f.close()
#     # if request.method == "POST":
#     #     sentence = request.form["sentence"]
#     #     language = request.form['inputvalue']
#     #     output = Translator().translate(sentence, dest=language)
#     #     return f"{  request.form['sentence']}"
#     # else:
#     #     return render_template(page)
#
#     @app.route("/", methods=["GET", "POST"])
#     def home():
#         if request.method == "POST":
#             t_sentence = request.form["sentence"]
#             language = request.form['inputvalue']
#             output = Translator().translate(t_sentence, dest=language)
#         else:
#             return render_template("file.html")
#         return render_template('file.html', output=output, sentence=t_sentence)
#
#
# if __name__ == '__main__':
#     app.run()

from googletrans import Translator

output = Translator().translate('my name is simi', dest='hi')
print(output)