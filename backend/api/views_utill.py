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
