import requests
import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.parse import quote

# Настройка стиля графиков
sns.set(style="whitegrid")


def get_user_input():
    """Получение входных данных от пользователя"""
    print("Введите язык программирования (например, Python, JavaScript, Go):")
    language = input().strip()

    print("Выберите период анализа (7 или 30 дней):")
    period = input().strip()
    while period not in ['7', '30']:
        print("Пожалуйста, выберите 7 или 30 дней:")
        period = input().strip()
    period = int(period)

    print("Введите минимальное количество звёзд (или нажмите Enter для пропуска):")
    min_stars = input().strip()
    min_stars = int(min_stars) if min_stars.isdigit() else 0

    return language, period, min_stars


def get_trending_repos(language, period, min_stars):
    """Получение трендовых репозиториев через GitHub API"""
    # Рассчитываем дату начала периода
    end_date = datetime.datetime.now()
    start_date = end_date - relativedelta(days=period)
    date_query = f"created:>{start_date.strftime('%Y-%m-%d')}"

    # Формируем запрос
    query = f"language:{quote(language)} {date_query}"
    if min_stars > 0:
        query += f" stars:>{min_stars}"

    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 10  # Ограничимся топ-10 для примера
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get('items', [])
    except requests.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return []


def process_repo_data(repos):
    """Обработка данных репозиториев"""
    repo_data = []
    for repo in repos:
        repo_info = {
            'name': repo['name'],
            'author': repo['owner']['login'],
            'stars': repo['stargazers_count'],
            'forks': repo['forks_count'],
            'language': repo['language'],
            'description': repo['description'] or "Нет описания",
            'url': repo['html_url']
        }
        repo_data.append(repo_info)
    return repo_data


def visualize_trends(repo_data, language, period):
    """Визуализация трендов"""
    if not repo_data:
        print("Нет данных для визуализации")
        return

    # Подготовка данных для графика
    names = [repo['name'] for repo in repo_data[:5]]  # Топ-5
    stars = [repo['stars'] for repo in repo_data[:5]]

    # Создание графика
    plt.figure(figsize=(10, 6))
    sns.barplot(x=stars, y=names, hue=names, palette="viridis", legend=False)

    plt.title(f"Топ-5 популярных {language} репозиториев за последние {period} дней")
    plt.xlabel("Количество звёзд")
    plt.ylabel("Репозиторий")

    # Сохранение графика
    filename = f"trending_{language.lower()}.png"
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
    print(f"График сохранён как {filename}")


def print_report(repo_data, language, period):
    """Вывод отчёта"""
    print(f"\nАнализируем популярные репозитории на {language} за последние {period} дней...")
    print("ТОП-5 самых быстрорастущих проектов:")

    for i, repo in enumerate(repo_data[:5], 1):
        print(f"{i}. **{repo['name']}** (+{repo['stars']} ⭐) - {repo['description']}")
        print(f"   Автор: {repo['author']}, Форков: {repo['forks']}, URL: {repo['url']}")


def main():
    # Получение пользовательского ввода
    language, period, min_stars = get_user_input()

    # Получение данных
    print("Получаем данные с GitHub...")
    repos = get_trending_repos(language, period, min_stars)

    if not repos:
        print("Не удалось получить данные. Проверьте подключение или параметры.")
        return

    # Обработка данных
    repo_data = process_repo_data(repos)

    # Вывод отчёта
    print_report(repo_data, language, period)

    # Визуализация
    visualize_trends(repo_data, language, period)


if __name__ == "__main__":
    main()
