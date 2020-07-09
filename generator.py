import os
import json

_SRC_DATA_PATH = 'src_data'
_TEMPLATE_DATA_PATH = 'templates'
_OUTPUT_DATA_PATH = 'Magiclysm-MagicBulletsMod'

_BULLET_WHITELIST = frozenset(['556'])

def extract_first_sentence(description):
    sentence_index = description.find('. ') + 1
    return description[:sentence_index if sentence_index > 0 else len(description)].strip()

def extract_bullet_data(filename):
    with open(filename) as f:
        data = json.load(f)

    base_bullets = []

    for bullet_info in data:
        if 'copy-from' not in bullet_info or bullet_info['id'] in _BULLET_WHITELIST:
            base_bullets.append(bullet_info)

    return base_bullets

def process_bullet_file(filename, item_templates, recipe_templates):
    datum = extract_bullet_data(os.path.join(_SRC_DATA_PATH, filename))

    item_defs = []
    recipe_defs = []

    for data in datum:
        # Make sure fields exist or else error here.
        data_id = data['id']
        data_name = data['name']['str']
        data_description = data.get('description', '')
        sentence = extract_first_sentence(data_description)

        for template in item_templates:
            item_defs.append(template.format(id=data_id, name=data_name, sentence=sentence))

        for template in recipe_templates:
            recipe_defs.append(template.format(id=data_id))

    return item_defs, recipe_defs

def process_all_bullets(item_templates, recipe_templates):
    files = os.listdir(_SRC_DATA_PATH)

    for bullet_file in files:
        item_defs, recipe_defs = process_bullet_file(bullet_file, item_templates, recipe_templates)

        # Write items out since we don't need to combine.
        with open(os.path.join(_OUTPUT_DATA_PATH, 'items', 'ammo', bullet_file), 'w') as f:
            f.write('[{}]'.format(','.join(item_defs)))

        # Write out final recipe.
        with open(os.path.join(_OUTPUT_DATA_PATH, 'recipes', bullet_file), 'w') as f:
            f.write('[{}]'.format(','.join(recipe_defs)))

def gather_templates(directory):
    templates = []

    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename)) as f:
            # Python's .format templating language requires { and } to be {{ and }} to be escaped.
            # This is probably still better than looping through and .formating per field.
            templates.append(f.read().replace('{', '{{').replace('}', '}}').replace('<', '{').replace('>', '}'))

    return templates

def main():
    item_templates = gather_templates(os.path.join(_TEMPLATE_DATA_PATH, 'ammo'))
    recipe_templates = gather_templates(os.path.join(_TEMPLATE_DATA_PATH, 'recipes'))

    process_all_bullets(item_templates, recipe_templates)

if __name__ == '__main__':
    main()