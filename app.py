from flask import Flask, request

app = Flask(__name__)

# הגדרנו את הנתיב כ- / (הנתיב הראשי) כדי למנוע שגיאות 404
@app.route('/', methods=['GET', 'POST'])
def yמות_bridge():
    # קבלת הקלט מימות המשיח
    user_input = request.values.get('msg', '')
    
    # ניקוי רווחים
    user_input = user_input.strip()

    # בדיקה אם הוקשו 4 ספרות
    if len(user_input) == 4 and user_input.isdigit():
        # הפורמט שביקשת עם & בסוף
        return f"id_list_message=m-{user_input}&"
    
    # אם אין קלט תקין, נבקש להקיש שוב (כדי שלא יתנתק)
    return "read=t-נא הקישו ארבע ספרות של הודעת המערכת.=&digits=4,4,7&"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
