from prisonapp import *
from models import Comments
import datetime

@app.route('/comments/', methods=['POST'])
def comments():
    data = request.get_json()

    newComment = Comments(cid=data['cid'],vid=data['vid'],content=data['content'], date=datetime.datetime.now())
    db.session.add(newComment)
    db.session.commit()

    return jsonify({'message':'New comment created!'})
