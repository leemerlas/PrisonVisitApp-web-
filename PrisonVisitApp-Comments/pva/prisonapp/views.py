from prisonapp import *
from models import Comments

@app.route('/comments/', methods=['POST'])
def comments():
    data = request.get_json()

    newComment = Comments(cid=data['cid'],vid=data['vid'],content=data['content'], date=data['date'])
    db.session.add(newComment)
    db.session.commit()

    return jsonify({'message':'New comment created!'})
