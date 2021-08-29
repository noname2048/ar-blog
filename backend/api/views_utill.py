def obj_to_post(obj):
    post = dict(vars(obj))

    if obj.modify_dt:
        post['modify_dt'] = obj.modify_dt.strftime("%Y-%m-%d %H:%M")
    else:
        post['modify_dt'] = ""

    if obj.tags:
        post['tags'] = [tag.name for tag in obj.tags.all()]
    else:
        post["tags"] = []

    if obj.owner:
        post["owner"] = obj.owner.username
    else:
        post['owner'] = 'Anonymous'

    del post['_state']

    return post


def prev_next_post(obj):
    try:
        prev_obj = obj.get_prev()
        prev_dict = {"id": prev_obj.id, "title": prev_obj.title}
    except obj.DoesNotExist as e:
        prev_dict = {}

    try:
        next_obj = obj.get_next()
        next_dict = {"id": next_obj.id, "title": next_obj.title}
    except obj.DoesNotExist as e:
        next_dict = {}

    return prev_dict, next_dict


def make_tag_cloud(qs_tag):
    min_count = min(tag.count for tag in qs_tag)
    max_count = max(tag.count for tag in qs_tag)

    def get_weight_func(min_weight, max_weight):
        if min_count == max_count:
            factor = 1.0
        else:
            factor = (max_weight - min_weight) / (max_count - min_count)

        def func(count):
            weight = round(min_weight + factor * (count - min_count))
            return weight

        return func

    weight_func = get_weight_func(1, 3)
    tag_list = []
    for tag in qs_tag:
        weight = weight_func(tag.count)
        tag_list.append({
            "name": tag.name,
            "count": tag.count,
            "weight": weight,
        })

    return tag_list
