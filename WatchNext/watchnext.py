from datetime import datetime, timedelta

movies = [
    {"title": "Inception", "genre": "Sci-Fi", "language": "English", "views": 120},
    {"title": "Interstellar", "genre": "Sci-Fi", "language": "English", "views": 200},
    {"title": "3 Idiots", "genre": "Comedy", "language": "Hindi", "views": 300},
    {"title": "The Dark Knight", "genre": "Action", "language": "English", "views": 180},
    {"title": "Dangal", "genre": "Drama", "language": "Hindi", "views": 250},
    {"title": "Avatar", "genre": "Sci-Fi", "language": "English", "views": 400},
    {"title": "Your Name", "genre": "Romance", "language": "Japanese", "views": 300},
    {"title": "Parasite", "genre": "Thriller", "language": "Korean", "views": 380},
    {"title": "Suzume", "genre": "Romance", "language": "Japanese", "views": 280},
    {"title": "Shutter Island", "genre": "Thriller", "language": "English", "views": 350},
    {"title": "Soulmate", "genre": "Drama", "language": "Korean", "views": 280},
]
watched_history = []
view_history = []

def display_movies():
    print("\n========== MOVIE COLLECTION ==========")

    for movie in movies[:5]:
        print(movie["title"], "-", movie["genre"], "-", movie["language"])

    print("\nShowing 5 titles out of", len(movies), "movies.")
    print("======================================")

def show_menu():
    print("\n========== WATCHNEXT ==========")
    print("1. View all titles")
    print("2. Add a new title")
    print("3. Record watched title")
    print("4. View genre preferences")
    print("5. Get recommendations")
    print("6. View trending titles")
    print("7. Exit")
    print("================================")
        
def add_movie():
    print("\n========== ADD NEW TITLE ==========")

    title = input("Enter title name: ")
    genre = input("Enter genre: ")
    language = input("Enter language: ")

    movie = {
        "title": title,
        "genre": genre,
        "language": language,
        "views": 0
    }

    movies.append(movie)

    print("\nTitle added successfully!")
def mark_watched():
    print("\n========== RECORD WATCHED TITLE ==========")

    display_movies()

    title = input("\nEnter the movie title you watched: ")

    for movie in movies:
        if movie["title"].lower() == title.lower():

            rating = float(input("Give your rating (1-5): "))

            if rating < 1 or rating > 5:
                print("Please enter a rating between 1 and 5.")
                return

            watched_history.append({
                "title": movie["title"],
                "genre": movie["genre"],
                "rating": rating
            })

            movie["views"] += 1
            view_history.append({
                "title": movie["title"],
                "date": datetime.now()
            })

            print("\nWatched title recorded successfully!")
            print("Your rating:", rating, "/5")
            return

    print("\nMovie not found!")

def genre_preferences():
    print("\n========== GENRE PREFERENCE SCORES ==========")

    genre_scores = {}

    for item in watched_history:
        genre = item["genre"]
        rating = item["rating"]

        if genre not in genre_scores:
            genre_scores[genre] = {
                "total": 0,
                "count": 0
            }

        genre_scores[genre]["total"] += rating
        genre_scores[genre]["count"] += 1

    if not genre_scores:
        print("No ratings available yet!")
        return

    for genre, data in genre_scores.items():
        average = data["total"] / data["count"]

        print(genre, ":", round(average, 2), "/ 5")

def recommend_movies():
    print("\n========== TOP 5 RECOMMENDATIONS ==========")

    genre_scores = {}

    for item in watched_history:
        genre = item["genre"]

        if genre not in genre_scores:
            genre_scores[genre] = []

        genre_scores[genre].append(item["rating"])

    for genre in genre_scores:
        genre_scores[genre] = sum(genre_scores[genre]) / len(genre_scores[genre])

    recommendations = []

    for movie in movies:
        watched = False

        for item in watched_history:
            if movie["title"].lower() == item["title"].lower():
                watched = True

        if not watched and movie["genre"] in genre_scores:
            recommendations.append(movie)

    recommendations.sort(
        key=lambda x: genre_scores[x["genre"]],
        reverse=True
    )

    if not recommendations:
        print("No recommendations available!")
        return

    for movie in recommendations[:5]:
        print(movie["title"], "-", movie["genre"])
        print("Reason: Based on your genre preference score of", 
              round(genre_scores[movie["genre"]], 2), "/5")
        
def trending_titles():
    print("\n========== TRENDING TITLES ==========")

    recent_date = datetime.now() - timedelta(days=7)

    trending = {}

    for view in view_history:
        if view["date"] >= recent_date:
            title = view["title"]
            trending[title] = trending.get(title, 0) + 1

    if not trending:
        print("No views recorded in the last 7 days!")
        return

    trending = sorted(trending.items(),
                      key=lambda x: x[1],
                      reverse=True)

    for title, count in trending:
        print(title, "-", count, "views")

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        display_movies()
    elif choice == "7":
        print("Thank you for using WatchNext!")
        break
    elif choice == "2":
        add_movie()
    elif choice == "3":
        mark_watched()
    elif choice == "4":
        genre_preferences() 
    elif choice == "5":
        recommend_movies() 
    elif choice == "6":
        trending_titles()          
    else:
        print("This option is not available yet.")  

    