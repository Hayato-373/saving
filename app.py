from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # 初期値
    goal = 0
    current = 0
    add_amount = 0
    new_total = 0
    remaining = 0
    message = ""

    if request.method == 'POST':
        try:
            # フォームから値を取得
            goal = int(request.form.get('goal', 0))
            current = int(request.form.get('current', 0))
            add_amount = int(request.form.get('add_amount', 0))
            
            # 計算
            new_total = current + add_amount
            remaining = goal - new_total
            
            if remaining <= 0:
                message = "おめでとう！目標達成です！"
                remaining = 0
            else:
                message = f"目標まであと {remaining}円 です。"
                
        except ValueError:
            message = "数値を正しく入力してください。"

    return render_template('index.html', 
                           total=new_total, 
                           remaining=remaining, 
                           message=message,
                           goal=goal)

if __name__ == '__main__':
    app.run(debug=True)