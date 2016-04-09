"""
Majority judgement is a voting system that aims to produce a ranking of all
candidates (from here-on 'submissions'). For a horrible wiki-hole on voting
theory, please see: https://en.wikipedia.org/wiki/Majority_judgment

This is designed to provide basic tools to play around with this voting system.

It has been set up with assumed use in ranking submissions to a CFP hence the
slightly odd terminology. The following substitutions are used:
    - Submission < - > candidate
    - Reviewer   < - > voter
    - Rating     < - > rank

A submissions score is its particular combination of ratings from the reviewers
(e.g. if there are 3 reviewers who rate 1, 0, and 1 respectively the
submissions' score is 0-1-1).

The majority judgement algorithm is this:
    1. Sort all submissions' ratings (to produce a score)
    2. Find the median rating of the score
    3. Group submissions by their median rating
    4. For each member of a group remove one instance of that group's
       median rating from the member's score
    5. Repeat steps 2-4 until the submissions are sorted or each group is empty
"""

from random import choice
from collections import OrderedDict

_get_rating = lambda: choice([0, 1, 2])


def generate_scores(n_submissions, n_reviewers, get_score=_get_rating):
    """
    For each submission generate a set of scores for each reviewer.

    The scores for each submission are sorted.
    """
    return [sorted([get_score() for reviewer in range(n_reviewers)])
                                for submissions in range(n_submissions)]


def get_floor_median(values):
    """
    Return the middle element (rounding down) from a sorted list of values
    """
    if len(values) == 1:
        return values[0]
    elif len(values) == 0:
        raise Exception('Cannot find median of empty list')
    median_index = int((len(values) - 0.5) // 2)
    return values[median_index]


def group_by_median(submission_scores):
    """
    Group scored submissions by their median score.

    Returns an OrderedDict by score.
    """
    res = {}
    for score_set in submission_scores:
        key = get_floor_median(score_set)

        if key not in res:
            res[key] = []
        res[key].append(score_set)

    return OrderedDict(sorted(res.items(), key=lambda x: x[0]))


def remove_scoring_element(score, score_set):
    to_remove = score_set.index(score)
    score_set.pop(to_remove)
    return score_set


def rank_submissions(submissions, max_depth=4, _current_depth=0):
    """
    Rank submissions based on their score.

    Submissions are grouped by median score then ties are broken by removing
    an instance of that score from the submissions' scores and repeating the
    process. This is repeated until either all scores have been removed from a
    submission's score set or the maximum recursion depth is reached.
    """
    if not submissions:
        raise Exception('Cannot rank no submissions')
    # Stop recursion if...
    elif len(submissions[0]) == 0:
        # All scores have been removed from the score sets
        return len(submissions)
    elif _current_depth == max_depth:
        # Max depth reached, stop sorting
        return len(submissions)

    ranked_scores = group_by_median(submissions)

    res = {}
    _current_depth += 1
    # Split ties by removing one element of the score then re-ranking.
    for score, scored_submissions in ranked_scores.items():
        next_round = []
        for score_set in scored_submissions:
            next_round.append(remove_scoring_element(score, score_set))

        res[score] = rank_submissions(next_round, max_depth, _current_depth)
    return OrderedDict(sorted(res.items(), key=lambda x: x[0]))


def score_tree(tree, base=3):
    reversed_tree = tree[::-1]
    res = 0
    for power, node_value in enumerate(reversed_tree):
        res += node_value * base**power
    return res


def linearise_submissions(submissions, base=3):
    def _linearise_submissions(submissions, base=3, _score_tree=[]):
        if not submissions:
            raise Exception('Cannot flatten no submissions')

        res = []

        for node_score, scored_submissions in submissions.items():
            tree = _score_tree + [node_score]

            if type(scored_submissions) == int:
                total_score = score_tree(tree, base)
                res.append((total_score, scored_submissions))
            else:
                res += _linearise_submissions(scored_submissions, base, tree)

        return res

    res = _linearise_submissions(submissions, base)
    return OrderedDict(sorted(res, key=lambda x: x[0]))


def recursive_sum_dict(vals):
    if type(vals) == int:
        return vals

    res = sum([recursive_sum_dict(v) for v in vals.values()])
    return res


if __name__ == '__main__':
    scores = generate_scores(150, 15)
    res = rank_submissions(scores, max_depth=3)

    print(linearise_submissions(res))
