from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# CP 彩票 → Lottery
@app.route('/lottery')
def lottery():
    return render_template('lottery.html')

# DM 代码 → Code
@app.route('/code')
def code():
    return render_template('code_tool.html')

# GY 关于应用 → About
@app.route('/about')
def about():
    return render_template('about.html')

# JZ 家长 → Parent
@app.route('/parent')
def parent():
    return render_template('parent.html')

# KY 开源 → OpenSource
@app.route('/opensource')
def opensource():
    return render_template('open_source.html')

# SJ 升级 → Upgrade
@app.route('/upgrade')
def upgrade():
    return render_template('upgrade.html')

# SS 搜索 → Search
@app.route('/search')
def search():
    return render_template('search.html')

# WD 我的 → Profile
@app.route('/profile')
def profile():
    return render_template('profile.html')


# 404页面处理
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)