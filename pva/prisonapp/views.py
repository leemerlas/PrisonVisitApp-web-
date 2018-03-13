from prisonapp import *
from models import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify ({'message':'token is missing!'}), 401

        try:
            data=jwt.decode(token, app.config['SECRET_KEY'])

            current_user=User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated



@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):

    if current_user.role_id != '0':
        return jsonify ({'message':'Cannot perform that function!'})

    users = User.query.all()
    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['username'] = user.username
        user_data['password'] = user.password_hash
        user_data['role_id'] = user.role_id
        output.append(user_data)

    return jsonify({'users':output})

@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'user does not exist'})

    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['username'] = user.username
    user_data['password'] = user.password_hash
    user_data['role_id'] = user.role_id

    return jsonify({'user':user_data})

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(public_id=str(uuid.uuid4()), username=data['username'], password_hash=hashed_password, role_id=2, status=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message':'New user created!'})

@app.route('/login/', methods=['GET'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate':'Basic realm = "Login required!"'})

    user = User.query.filter_by(username=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm = "Login required!"'})

    if check_password_hash(user.password_hash, auth.password):
        token = jwt.encode({'public_id':user.public_id, 'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        print 'Token generated!'
        return jsonify({'status':'ok', 'token': token.decode('UTF-8'), 'role_id':user.role_id, 'message':'login successful!'})







