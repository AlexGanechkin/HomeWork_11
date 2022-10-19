import json


def load_candidates():
    """
    Загружаем кандидиатов из файла
    Входящие данные: path - путь к файлу с кандидатами
    Исходящие данные: список словарей с кандидатами
    """

    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def get_candidate_by_id(candidate_id):
    """
    Выбираем кандидата по его ID и формируем ответ
    Входящие данные: candidate_id - номер кандидиата
    Исходящие данные: словарь с найденным кандидатом / False - если не найден
    """

    candidates = load_candidates()

    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return False


def get_candidates_by_name(candidate_name):
    """
    Выбираем кандидата по его имени и формируем ответ
    Входящие данные: candidate_name - имя кандидиата (регистр не имеет значения)
    Исходящие данные: список словарей с найденными кандидатами / None - если не найден
    """

    candidates = load_candidates()
    searched_candidates = []

    for candidate in candidates:
        candidates_name = candidate['name'].split()
        if candidate_name.lower() == candidates_name[0].lower():
            searched_candidates.append(candidate)
    return searched_candidates


def get_candidates_by_skill(skill_name):
    """
     Выбираем кандидата по его имени и формируем ответ
     Входящие данные: candidate_name - имя кандидиата (регистр не имеет значения)
     Исходящие данные: список словарей с найденными кандидатами / None - если не найден
     """

    candidates = load_candidates()
    skilled_candidates = []

    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower().split(", "):
            skilled_candidates.append(candidate)
    return skilled_candidates
