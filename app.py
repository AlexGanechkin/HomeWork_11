from flask import Flask, request, render_template
import utils

app = Flask(__name__)


@app.route('/')
def get_all_candidates():
    candidates = utils.load_candidates()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:candidate_id>')
def candidate_profile(candidate_id):
    candidate = utils.get_candidate_by_id(candidate_id)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_candidate(candidate_name):
    found_candidates = utils.get_candidates_by_name(candidate_name)
    number_candidates = len(found_candidates)
    return render_template('search.html', number=number_candidates, found_candidates=found_candidates)


@app.route('/skill/<skill_name>')
def search_candidate_by_skill(skill_name):
    found_candidates = utils.get_candidates_by_skill(skill_name)
    number_candidates = len(found_candidates)
    return render_template('skill.html', skill_name=skill_name,
                           number=number_candidates,
                           found_candidates=found_candidates)


if __name__ == "__main__":
    app.run()
