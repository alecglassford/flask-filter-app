from random import sample

from flask import Flask, abort, render_template, request

from foo import filtered_restaurants, map_display, fetch_detail

MAP_MAX = 500

app = Flask(__name__)

@app.route('/')
def index():
    query = request.args.get('query') or ''
    only_unsatisfactory = request.args.get('unsatisfactory') or False
    try:
        min_score = int(request.args.get('min_score'))
    except:
        min_score = 0
    restaurants = filtered_restaurants(query, min_score, only_unsatisfactory)
    map_list = map_display(restaurants)
    if len(map_list) > MAP_MAX:
        map_list = sample(map_list, MAP_MAX)
    return render_template('index.html', MAP_MAX=MAP_MAX, places=map_list,
                                         query=query, min_score=min_score,
                                         ou=only_unsatisfactory)

@app.route('/<r_name>/')
def detail(r_name):
    try:
        detail = fetch_detail(r_name)
    except:
        abort(404)
    return render_template('detail.html', d=detail)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
