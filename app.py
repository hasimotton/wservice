# ライブラリのインポート
from flask import Flask, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
# Flaskクラスのインスタンス化
app = Flask(__name__)

# オブジェクト変更追跡システム無効設定
SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemyでデータベースに接続する
db_uri = 'sqlite:///test3.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

# オブジェクト名
user_name = ""


class Comment(db.Model):
    """[テーブルの定義を行うクラス]
    Arguments:
        db {[Class]} -- [ライブラリで用意されているクラス]
    """

    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.Text())
    comment = db.Column(db.Text())
    category = db.Column(db.Text())

    def __init__(self, pub_date, name, comment, category):
        """[テーブルの各カラムを定義する]
        [Argument]
            id_ -- 投稿番号(プライマリキーなので、自動で挿入される)
            pub_date -- 投稿日時
            name -- 投稿者名
            comment -- 投稿内容
        """

        self.pub_date = pub_date
        self.name = name
        self.comment = comment
        self.category = category


try:
    db.create_all()
except Exception as e:
    print(e.args)
    pass

# index.htmlに投稿データを渡す


@app.route("/")
def index():
    # テーブルから投稿データをSELECT文で引っ張ってくる
    text = Comment.query.all()
    return render_template("index.html", lines=text, user_name=user_name)


# お洒落
@app.route("/fashion")
def fashion():
    menu_name = "お洒落"
    info = "お洒落"
    genre = "fashion"
    text = Comment.query.filter_by(category="fashion").all()
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info, lines=text, genre=genre)


# 音楽
@app.route("/music")
def music():
    menu_name = "音楽"
    info = "音楽"
    genre = "music"
    text = Comment.query.filter_by(category="music").all()
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info, lines=text, genre=genre)

# ゲーム


@app.route("/game")
def game():
    menu_name = "ゲーム"
    info = "ゲーム"
    genre = "game"
    text = Comment.query.filter_by(category="game").all()
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info, lines=text, genre=genre)

# バイト


@app.route("/ptjob")
def ptjob():
    menu_name = "バイト"
    info = "バイト"
    genre = "ptjob"
    text = Comment.query.filter_by(category="ptjob").all()
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info, lines=text, genre=genre)

# スポーツ


@app.route("/sport")
def sport():
    menu_name = "スポーツ"
    info = "スポーツ"
    genre = "sport"
    text = Comment.query.filter_by(category="sport").all()
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info, lines=text, genre=genre)

# 授業


@app.route("/lecture")
def lecture():
    menu_name = "授業"
    info = "授業"
    genre = "lecture"
    text = Comment.query.filter_by(category="lecture").all()
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info, lines=text, genre=genre)

# 大学


@app.route("/university")
def university():
    menu_name = "大学"
    info = "大学"
    genre = "university"
    text = Comment.query.filter_by(category="university").all()
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info, lines=text, genre=genre)

# 買い物


@app.route("/shopping")
def shopping():
    menu_name = "買い物"
    info = "買い物"
    genre = "shopping"
    text = Comment.query.filter_by(category="shopping").all()
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info, lines=text, genre=genre)

# 映画


@app.route("/movie")
def movie():
    menu_name = "映画"
    info = "映画"
    genre = "movie"
    text = Comment.query.filter_by(category="movie").all()
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info, lines=text, genre=genre)

# 娯楽


@app.route("/amenity")
def amenity():
    menu_name = "娯楽"
    info = "娯楽"
    genre = "amenity"
    text = Comment.query.filter_by(category="amenity").all()
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info, lines=text, genre=genre)

# 何でも


@app.route("/anything")
def anything():
    menu_name = "何でも"
    info = "何でも"
    genre = "anything"
    text = Comment.query.filter_by(category="anything").all()
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info, lines=text, genre=genre)

# その他


@app.route("/other")
def other():
    menu_name = "その他"
    info = "その他"
    genre = "other"
    text = Comment.query.filter_by(category="other").all()
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info, lines=text, genre=genre)


# 投稿の送信とデータベース追加
@app.route("/", methods=["POST"])
def result():
    # 現在時刻　投稿者名　投稿内容を取得
    date = datetime.now()
    comment = request.form["comment_data"]
    name = request.form["name"]
    category = request.form["category"]
    # テーブルに格納するデータを定義する
    comment_data = Comment(pub_date=date, name=name,
                           comment=comment, category=category)
    # テーブルにINSERTする
    db.session.add(comment_data)
    # テーブルへの変更内容を保存
    db.session.commit()
    return render_template("index.html", comment=comment, name=name, now=date, category=category)


# 実行
if __name__ == "__main__":
    app.run(host="localhost", debug=True)
