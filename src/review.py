import re

import automatic_code_review_commons as commons


def __is_pattern(patterns, name):
    for pattern in patterns:
        if re.match(pattern, name):
            return True

    return False


def review(config):
    merge = config['merge']

    comments = []
    rules = config['rules']

    for change in merge['changes']:
        if change['deleted_file']:
            continue

        new_path = change['new_path']
        if "/" in new_path:
            filename = new_path[new_path.rindex('/') + 1:]
        else:
            filename = new_path

        for rule in rules:
            if not re.match(rule['name'], new_path):
                continue

            if __is_pattern(rule['pattern'], filename):
                continue

            comment_description = rule['comment']
            comment_description = comment_description.replace("${FILE_PATH}", new_path)

            comments.append(commons.comment_create(
                comment_id=commons.comment_generate_id(comment_description),
                comment_path=new_path,
                comment_description=comment_description,
                comment_snipset=False,
                comment_end_line=1,
                comment_start_line=1,
                comment_language="",
            ))

    return comments
