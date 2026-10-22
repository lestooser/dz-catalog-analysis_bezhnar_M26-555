import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    if not movies:
        return 0.0
    total_rating = sum(movie["rating"] for movie in movies) / len(movies)
    return round(total_rating, 1)


def catalog_age_stats(movies, current_year=2026):
    if not movies:
        return ("No movies available", "No movies available", "No movies available")

    ages = [current_year - movie["year"] for movie in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    if minutes < 60:
        return f"{minutes}м"

    return f"{minutes // 60}ч {(minutes % 60)}м"


# ===== Этап 2. Условия и match (задачи 4–5) =====


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case x if x >= 2020:
            return "новые"
        case x if 2015 <= x < 2020:
            return "недавние"
        case _:
            return "старые"


# ===== Этап 3. Циклы (задачи 6–8) =====


def demo_skip_comedies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def demo_first_masterpiece(movies):
    i = 0
    current_movie = None
    while movies:
        if movies[i]["rating"] > 9.0:
            current_movie = movies[i]
            break
        i += 1
    else:
        return "Шедевров не найдено"

    return current_movie["title"]


def count_long_movies(movies, threshold=120):
    count_long_movie = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count_long_movie += 1

    return count_long_movie


# ===== Этап 4. Строки (задачи 9–11) =====


def normalize_title(title):
    words = str.split(title)  # задача 9

    result_list = []

    for word in words:
        new_word = word[0].upper() + word[1:]
        result_list.append(new_word)

    return " ".join(result_list)


def make_slug(title):
    return title.replace(" ", "-").lower()


def format_report_line(movie):
    return (
        f'"{movie["title"]}" ({movie["year"]}) — '
        f"{movie['rating']}/10, {duration_in_hours(movie['duration_min'])}, "
        f'жанры: {", ".join(movie["genres"])}"'
    )

