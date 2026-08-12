from flask import Flask, request

app = Flask(__name__)

@app.route('/yמות')
def yמות_format():
    # קבלת מספר ההודעה מהפרמטר msg ב-URL
    message_id = request.args.get('msg', '')
    
    # בדיקה שהוכנסו בדיוק 4 ספרות
    if len(message_id) == 4 and message_id.isdigit():
        return f"id_list_message=m-{message_id}"
    else:
        return "error=invalid_message_id"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
